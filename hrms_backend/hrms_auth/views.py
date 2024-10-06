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
        """
            Verify if the OTP provided by the user is valid.

            This endpoint allows users to verify a one-time password (OTP) sent to their mobile number. 
            The user must provide a valid mobile number and the OTP they received. The system checks 
            if the OTP is correct and returns a corresponding response.

            **Request Parameters:**
            - `mobile_number`: The mobile number of the user (last 9 digits are used for verification).
            - `otp`: The one-time password sent to the user for verification.

            **Responses:**
            - `200 OK`: If the OTP is valid.
            - `403 Forbidden`: If the OTP is invalid.
            - `404 Not Found`: If no user is associated with the provided mobile number.

            **Example:**
            ```
            GET /api/accounts/users/verify-otp/
            {
                "mobile_number": "1234567890",
                "otp": "123456"
            }
            ```

            **Response Example (Success):**
            ```
            {
                "message": "OTP is valid"
            }
            ```

            **Response Example (Error - Invalid OTP):**
            ```
            {
                "error": "Invalid OTP"
            }
            ```

            **Response Example (Error - User Not Found):**
            ```
            {
                "error": "User with this mobile number does not exist"
            }
            ```
        """
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
        """
            Request a One-Time Password (OTP) for mobile number verification.

            This endpoint allows users to request an OTP to be sent to their mobile number. 
            If the mobile number is not associated with an existing user, a new user record 
            is created with the provided number. The OTP is then generated and sent to the user's phone.

            **Request Parameters:**
            - `mobile_number`: The mobile number to which the OTP should be sent (only the last 9 digits are used for matching).

            **Behavior:**
            - If the mobile number already exists in the system, an OTP is generated for that user.
            - If the mobile number does not exist, a new user is created with that number, and an OTP is generated for the newly created user.

            **Responses:**
            - `200 OK`: OTP has been successfully generated and sent to the mobile number provided.
            - `400 Bad Request`: If the mobile number is not provided or is in an invalid format.

            **Example:**
            ```
            GET /api/accounts/users/request-otp/
            {
                "mobile_number": "1234567890"
            }
            ```

            **Response Example (Success):**
            ```
            {
                "message": "Check your phone for your One Time Password"
            }
            ```

            **Response Example (Error - Invalid Input):**
            ```
            {
                "error": "Invalid mobile number"
            }
            ```

            **Notes:**
            - The OTP is sent via an external service (e.g., SMS), which is triggered within the system by the `send_otp` function.
            - Only the last 9 digits of the mobile number are used for validation to support various number formats.
        """
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
