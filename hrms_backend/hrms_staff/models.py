from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

class Staff(models.Model):
    surname = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    id_photo = models.ImageField(upload_to=settings.PHOTO_URL)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        get_user_model(), models.DO_NOTHING, null=True, blank=True, related_name="%(app_label)s_%(class)s_updated_by")
    created_by = models.ForeignKey(
        get_user_model(), models.DO_NOTHING, null=True, blank=True, related_name="%(app_label)s_%(class)s_created_by")
    
    user = models.OneToOneField(
        get_user_model(), models.DO_NOTHING, null=True, blank=True, related_name="staff")
    
    class Meta:
        ordering = ("-id",)
