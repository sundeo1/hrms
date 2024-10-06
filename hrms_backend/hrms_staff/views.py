from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny
from hrms_auth.helpers import DEFAULT_FILTER_BACKENDS
from hrms_staff.models import Staff
from hrms_staff.serializers import StaffSerializer

class StaffViewSet(ListModelMixin, RetrieveModelMixin, CreateModelMixin, GenericViewSet):
    """
        A viewset for managing staff information, including personal details such as surname, other names, 
        date of birth, and an ID photo.

        This viewset provides the following actions:

        - `list`: Retrieve a list of all staff members.
        - `retrieve`: Retrieve detailed information about a specific staff member by their ID.
        - `create`: Create a new staff member record with personal details.


        **Endpoints:**
        - `GET /api/accounts/staff/`: Retrieve a list of all staff members.
        - `GET /api/accounts/staff/{id}/`: Retrieve detailed information about a specific staff member by their ID.
        - `POST /api/accounts/staff/`: Create a new staff record with the provided personal details.

        **Examples:**

        - **List Staff Members:**
        ```
        GET /api/accounts/staff/
        ```

        - **Retrieve a Staff Member:**
        ```
        GET /api/accounts/staff/{id}/
        ```

        - **Create a New Staff Member:**
        ```
        POST /api/accounts/staff/
        {
            "surname": "Doe",
            "other_name": "John",
            "date_of_birth": "1990-01-01",
            "id_photo": "path/to/photo.jpg"
            "mobile_number": "4567890876"
            "otp": "9865678976"
        }
        ```

        **Response Examples:**

        - **List Example:**
        ```
        [
            {
                "id": 1,
                "surname": "Doe",
                "other_name": "John",
                "date_of_birth": "1990-01-01",
                "id_photo": "url/to/photo1.jpg"
            },
            {
                "id": 2,
                "surname": "Smith",
                "other_name": "Jane",
                "date_of_birth": "1985-05-15",
                "id_photo": "url/to/photo2.jpg"
            }
        ]
        ```

        - **Retrieve Example:**
        ```
        {
            "id": 1,
            "surname": "Doe",
            "other_name": "John",
            "date_of_birth": "1990-01-01",
            "id_photo": "url/to/photo.jpg"
        }
        ```

        - **Create Example:**
        ```
        {
            "id": 3,
            "surname": "Johnson",
            "other_name": "Mike",
            "date_of_birth": "1992-12-12",
            "id_photo": "url/to/photo3.jpg"
        }
        ```

        **Notes:**
        - This viewset allows for listing, retrieving, and creating staff members with the required fields (`surname`, `other_name`, `date_of_birth`, `id_photo`).
        
    """
    
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    filter_backends = DEFAULT_FILTER_BACKENDS
    permission_classes = (AllowAny, )
