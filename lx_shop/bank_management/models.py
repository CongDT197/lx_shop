from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from django.db.models import CASCADE

from user_management.models import User


class Bank(models.Model):
    bank_code = models.CharField(max_length=20, null=False, validators=[MinLengthValidator(3)])
    bank_name = models.CharField(max_length=120, null=False, validators=[MinLengthValidator(7)])
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{}_{}'.format(self.bank_code, self.bank_name)


class UserBank(models.Model):
    user_id = models.ForeignKey(User, null=False, on_delete=CASCADE)
    bank_id = models.ForeignKey(Bank, null=False, on_delete=CASCADE)
    bank_number = models.CharField(max_length=32, blank=False, null=False, validators=[MinLengthValidator(10)])
    # bank_branch = models.CharField(max_length=64, blank=True, null=True, validators=[MinLengthValidator(10)])
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{}_{}'.format(self.user_id, self.bank_id)
