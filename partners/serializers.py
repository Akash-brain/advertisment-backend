from rest_framework import serializers
from .models import PartnerApplication

class PartnerApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerApplication
        fields = '__all__'

    def validate_partner_type(self, value):
        # Mapping display names to database values
        partner_type_mapping = {
            "BDA Partner": "BDA",
            "Store Partner": "Store",
            "Studio Partner": "Studio",
            "Delivery Partner": "Delivery"
        }

        # Convert the frontend value to the correct database value
        if value in partner_type_mapping:
            return partner_type_mapping[value]
        
        # If the value is already in the correct format, return it
        if value in partner_type_mapping.values():
            return value
        
        # Raise an error if the value is invalid
        raise serializers.ValidationError(f"Invalid partner_type: {value}")
