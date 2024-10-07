from rest_framework import serializers

from hrms_auth.models import HrmsUser
from hrms_staff.models import Staff

class StaffSerializer(serializers.ModelSerializer):
    staff_id = serializers.CharField(read_only=True)
    mobile_number = serializers.CharField(write_only=True, required=True)
    otp = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = Staff
        fields = '__all__'

    def validate(self, attrs):

        request = self.context.get('request')  
        if request and request.method == 'PATCH':
        # Skip validation for PATCH requests
            return attrs
        
        mobile_number = attrs.get('mobile_number')  
        otp = attrs.get('otp')
        
       
        user = HrmsUser.objects.filter(mobile_number=mobile_number).first()  
        if user is None:  
            raise serializers.ValidationError({'mobile_number': "Mobile number has not requested for verification code"})

       
        if not user.is_otp_valid(otp):
            raise serializers.ValidationError({'otp': "Verification code is invalid"})

        
        if Staff.objects.filter(user=user).exists():
            raise serializers.ValidationError({'user': "This number is already associated with a staff record."})

        
        attrs['user'] = user
        return attrs

    def create(self, validated_data):
        
        validated_data.pop('mobile_number')
        validated_data.pop('otp')
        
        
        staff = Staff.objects.create(**validated_data)
        
        
        staff.user = validated_data.get('user')  
        staff.save()
        
        return staff

