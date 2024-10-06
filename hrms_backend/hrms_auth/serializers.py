from rest_framework import serializers

from hrms_auth.models import HrmsUser

class HrmsUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HrmsUser
        exclude = ("groups","user_permissions",)
        extra_kwargs = {
            "otp": {'write_only': True, "required": False},
            "otp_expiry_time": {'write_only': True, "required": False},
            "date_joined": {'read_only': True},
            "is_staff": {'read_only': True},
            "is_active": {'read_only': True},
            "last_login": {'read_only': True},
        }

    def save(self, **kwargs):
        if self.instance:
            if self.instance.pk:
                self.instance.updated_by = self.get_current_user()
                self.instance.author = self.get_current_user()
            if 'password' in self.validated_data:
                self.instance.set_password(self.validated_data.pop('password'))
            self.instance.save()
        return super().save(**kwargs)
    
class VerifyOtpSerializer(serializers.Serializer):
    mobile_number = serializers.CharField(write_only=True, required=True, min_length=9)
    otp = serializers.CharField(write_only=True, required=True, min_length=10, max_length=10)

class RequestOtpSerializer(serializers.Serializer):
    mobile_number = serializers.CharField(write_only=True, required=True, min_length=9)