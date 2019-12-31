import datetime

from commons.error_code import ValidationError
from user_management.models import User


def validate_set_id(value):
    if value.__len__() == 0:
        raise ValidationError('SET_ID_CANT_BLANK')
    for item in value:
        if not isinstance(item, int):
            raise ValidationError('USER_ID_MUST_BE_INTEGER')


def validate_unique_email(instance, email):
    user_list = User.objects.filter(email=email)
    for user in user_list:
        if user.is_active == True and instance.id != user.id:
            raise ValidationError('EMAIL_UNIQUE')
        elif user.is_active == False:
            user.delete()
