from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=True)
    def __str__(self):
        return self.username
    
class Patient(models.Model):
    # Define fields for the patient, for example:
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    # Add any additional fields you need

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
from django.db import models
from django.conf import settings

class Prediction(models.Model):
    # Optionally, link to a user if you have a custom user model
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    symptoms = models.TextField(help_text="Symptoms used for prediction, e.g., comma-separated list")
    predicted_disease = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.predicted_disease} predicted on {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
