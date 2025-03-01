from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
import json
from .models import User, PartnerApplication, HelpRequest
from .serializers import UserSerializer, PartnerApplicationSerializer, HelpRequestSerializer

# User Registration API (With Debugging)
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            print("Received Data:", request.data)  # Log incoming request data

            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()

                # Return a success response after saving
                return Response(
                    {"message": "User registered successfully!", "user": serializer.data},
                    status=status.HTTP_201_CREATED
                )
            else:
                print("Validation Errors:", serializer.errors)  # Log validation errors
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print("Error:", str(e))  # Log unexpected errors
            return Response({"message": "Something went wrong!", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# User Login API
class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(username=email, password=password)
        if user:
            return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# Partner Application API (With Debugging)
class PartnerApplyView(generics.CreateAPIView):
    queryset = PartnerApplication.objects.all()
    serializer_class = PartnerApplicationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Validation Errors:", serializer.errors)  # Debugging output
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Help Request API (Allow GET & POST)
class HelpRequestView(generics.ListCreateAPIView):  # ListCreateAPIView allows GET & POST
    queryset = HelpRequest.objects.all()
    serializer_class = HelpRequestSerializer
    permission_classes = [AllowAny]
