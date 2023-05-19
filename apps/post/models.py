from django.db import models
from django.contrib.auth import get_user_model
from apps.core.models import TimeStampMixin, PrimaryKeyAsUUIDMixin


# Create your models here.
class Post(TimeStampMixin, PrimaryKeyAsUUIDMixin):
    body = models.TextField(null=True, blank=True)
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.CASCADE, related_name="post"
    )
