from django.urls import include, re_path
from rest_framework.routers import DefaultRouter

from hrms_auth.views import HrmsUserViewSet


router = DefaultRouter()

# user accounts
router.register(r'users', HrmsUserViewSet, basename='Accounts')

urlpatterns = [
    re_path('accounts/', include(router.urls)),
]