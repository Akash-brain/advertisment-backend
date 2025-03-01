from django.contrib import admin
from .models import PartnerApplication, HelpRequest, User  # Import HelpRequest model

# Register PartnerApplication model
admin.site.register(PartnerApplication)

# Register HelpRequest model
admin.site.register(HelpRequest)

admin.site.register(User)