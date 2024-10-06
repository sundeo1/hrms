from django.db import models
import random
import string
from datetime import *
from django.utils import timezone
from django.core import signing
from django.contrib.auth.models import AbstractUser

class HrmsUser(AbstractUser):
    mobile_number = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    otp = models.CharField(max_length=255, null=True, blank=True)
    otp_expiry_time = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        'self', models.DO_NOTHING, null=True, blank=True, related_name="%(app_label)s_%(class)s_updated_by", db_column='updated_by')
   
    USERNAME_FIELD = "mobile_number"
    

    class Meta:
        ordering = ("-id",)

    def generate_otp(self, minutes=2):
        """
        Generate a 10-digit code, store it in the 'otp_code' field, and set 'otp_expiry_time' based on the specified minutes.
        """
        _otp = ''.join(random.choices(string.digits, k=10))  # Generate a 10-digit OTP
        self.otp = signing.dumps(_otp)  # Encrypt and store the OTP
        self.otp_expiry_time = timezone.now() + timedelta(minutes=minutes)
        self.save()

        return _otp
    
    def is_otp_valid(self, user_otp):
        """
        Verify if the provided OTP matches the stored OTP and has not expired.
        """
        if self.otp and self.otp_expiry_time:
            current_time = timezone.now()
            if current_time <= self.otp_expiry_time:
                decrypted_otp = signing.loads(self.otp)
                if user_otp == decrypted_otp:
                    return True
        return False
