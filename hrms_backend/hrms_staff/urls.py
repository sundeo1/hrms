from django.urls import include, re_path
from rest_framework.routers import DefaultRouter

from hrms_staff.views import StaffViewSet

router = DefaultRouter()

# user accounts
router.register(r'staff', StaffViewSet, basename='Staff')

urlpatterns = [
    re_path('accounts/', include(router.urls)),
]