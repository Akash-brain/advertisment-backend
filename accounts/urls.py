from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterUserView, PartnerApplyView, HelpRequestView,LoginView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='user-register'),
    path('Login/', LoginView.as_view(), name='login'),
    path('partner-apply/', PartnerApplyView.as_view(), name='partner-apply'),
    path('help/', HelpRequestView.as_view(), name='help-request'),

    # JWT Authentication Routes
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
