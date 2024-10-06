from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from hrms_auth.helpers import DEFAULT_FILTER_BACKENDS, send_otp
from hrms_auth.models import HrmsUser
from hrms_auth.permissions import HasValidOtp
from hrms_auth.serializers import HrmsUserSerializer, RequestOtpSerializer, VerifyOtpSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class HrmsUserViewSet(ReadOnlyModelViewSet):
    queryset = HrmsUser.objects.all()
    serializer_class = HrmsUserSerializer
    filter_backends = DEFAULT_FILTER_BACKENDS
    permission_classes = (AllowAny, )

    @action(
        methods=["get"],
        detail=False,
        url_path="verify-otp",
        url_name="verify-otp",
        permission_classes=[AllowAny],
        serializer_class=VerifyOtpSerializer
    )
    def verify_otp(self, request, *args, pk=None, **kwargs):
        serializer = VerifyOtpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile_number = serializer.validated_data['mobile_number']
        otp = serializer.validated_data['otp']

        try:
            user = HrmsUser.objects.get(mobile_number__endswith=mobile_number[-9:])
        except HrmsUser.DoesNotExist:
            return Response(
                {'error': 'User with this mobile number does not exist'},
                status=status.HTTP_404_NOT_FOUND
            )

        if user.is_otp_valid(otp):
            return Response(
                {'message': 'OTP is valid'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'error': 'Invalid OTP'},
                status=status.HTTP_403_FORBIDDEN
            )
        
    @action(
        methods=["get"],
        detail=False,
        url_path="request-otp",
        url_name="request-otp",
        permission_classes=[AllowAny],
        serializer_class=RequestOtpSerializer
    )
    def request_otp(self, request, *args, pk=None, **kwargs):
        serializer = RequestOtpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile_number = serializer.validated_data['mobile_number']
        

        try:
            user = HrmsUser.objects.get(mobile_number__endswith=mobile_number[-9:])
        except HrmsUser.DoesNotExist:
            user = HrmsUser.objects.create(
                mobile_number = mobile_number
            )

        otp = user.generate_otp()
        
        if otp is not None:
            send_otp(otp, mobile_number)
        return Response(
            {'message': 'Check your phone for your One Time Password'},
            status=status.HTTP_200_OK
        )
