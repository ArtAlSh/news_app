from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator


# Create your models here.
class CustomUser(AbstractUser):
    # age = models.CharField(max_length=2, null=True, blank=True, help_text='Enter your age.')
    age = models.PositiveIntegerField(null=True,
                                      blank=True,
                                      help_text='Enter your age.',
                                      )
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Changed text"
        ),
        validators=[UnicodeUsernameValidator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
