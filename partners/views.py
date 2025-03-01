from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import PartnerApplication
from .serializers import PartnerApplicationSerializer

class PartnerApplicationView(APIView):  # ✅ Changed name for consistency
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        print("📩 Incoming Data:", request.data)  # Debugging: Log incoming request data
        
        # ✅ Allowed partner types
        valid_partner_types = ['BDA', 'Store', 'Studio', 'Delivery']
        partner_type = request.data.get("partner_type", "").strip()  # Trim spaces
        
        if partner_type not in valid_partner_types:
            print("❌ Invalid partner_type:", partner_type)  # Debugging: Log invalid type
            return Response(
                {"error": f"Invalid partner_type '{partner_type}'. Choose from {valid_partner_types}."}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PartnerApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("✅ Data Saved Successfully")  # Debugging: Confirm data was saved
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("⚠️ Validation Errors:", serializer.errors)  # Debugging: Log validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
