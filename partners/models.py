from django.db import models

class PartnerApplication(models.Model):
    PARTNER_TYPES = [
        ('BDA', 'BDA Partner'),
        ('Store', 'Store Partner'),
        ('Studio', 'Studio Partner'),
        ('Delivery', 'Delivery Partner'),
    ]

    name = models.CharField(max_length=255)  # Ensure field name matches
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)  # Ensure field name matches
    partner_type = models.CharField(max_length=20, choices=PARTNER_TYPES)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    partner_type = models.CharField(max_length=50, default="general")


    def __str__(self):
        return self.name
