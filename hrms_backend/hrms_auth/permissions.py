from rest_framework.permissions import BasePermission

class HasValidOtp(BasePermission):
    """
    Allows access only to users who have valid otp.
    """

    def has_permission(self, request, view):
        return request.user.is_otp_valid(request.user.otp)