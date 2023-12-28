import logging
import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db import models

from core.managers import UserManager
from core.mixins import ModifiableMixin
from django.utils.translation import gettext_lazy as _


logger = logging.getLogger(__name__)


class User(
    AbstractBaseUser,
    PermissionsMixin,
    ModifiableMixin,
):
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, blank=True, null=True)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = "user"
        app_label = "users"

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
