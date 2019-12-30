from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from commons.constrain import CUSTOMER, ADMIN

USER_TYPE = ((CUSTOMER, 'CUSTOMER'),
             (ADMIN, 'ADMIN'),
             )
GENDER = ((1, 'MALE'),
          (2, 'FEMALE'),
          (3, 'OTHER'),
          )


class User(AbstractUser):
    username = models.CharField(max_length=64, null=False, validators=[MinLengthValidator(10)])
    email = models.EmailField(max_length=64, null=False, unique=True, validators=[MinLengthValidator(8)])
    password = models.CharField(max_length=128, null=False, validators=[MinLengthValidator(6)])
    gender = models.SmallIntegerField(choices=GENDER, null=False, blank=False, default=1)
    birthday = models.DateField(null=False, blank=False)
    address = models.CharField(max_length=100, null=False, validators=[MinLengthValidator(10)])
    phone_number = models.CharField(max_length=13, null=False, blank=False, validators=[MinLengthValidator(10)])
    user_type = models.SmallIntegerField(choices=USER_TYPE, null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'birthday', 'address', 'phone_number', 'user_type']

    def __str__(self):
        return '{}____{}'.format(self.username, USER_TYPE[self.user_type - 1][1]).upper()
