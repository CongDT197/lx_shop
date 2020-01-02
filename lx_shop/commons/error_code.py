from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_200_OK


class ValidationError(APIException):
    status_code = HTTP_200_OK

    def __init__(self,
                 detail=None,
                 code=None):
        self.code = code
        super().__init__(detail=detail,
                         code=code)


class AuthenticationFailed(APIException):
    status_code = HTTP_200_OK

    def __init__(self,
                 detail=None,
                 code=None):
        self.code = code
        super().__init__(detail=detail,
                         code=code)


ErrorCode = {
    'SAVE_SUCCESS': {
        'message': 'User created success',
        'code': 200
    },
    'USERNAME_REQUIRED': {
        'message': 'The username field is required',
        'code': 300
    },
    'USERNAME_MIN_LENGTH': {
        'message': 'Ensure username field has at least 10 characters.',
        'code': 301
    },
    'USERNAME_MAX_LENGTH': {
        'message': 'Ensure username field has at no more than 64 characters.',
        'code': 302
    },
    'PASSWORD_REQUIRED': {
        'message': 'The password field is required',
        'code': 305
    },
    'PASSWORD_MIN_LENGTH': {
        'message': 'Ensure password field has at least 6 characters.',
        'code': 306
    },
    'PASSWORD_MAX_LENGTH': {
        'message': 'Ensure password field has at no more than 128 characters.',
        'code': 307
    },
    'EMAIL_INVALID': {
        'message': 'Entered email is invalid format',
        'code': 310
    },
    'EMAIL_MAX_LENGTH': {
        'message': 'Ensure email field has at least 8 characters.',
        'code': 311
    },
    'EMAIL_REQUIRED': {
        'message': 'The email field is required',
        'code': 312
    },
    'EMAIL_UNIQUE': {
        'message': 'This email is available',
        'code': 313
    },
    'GENDER_INVALID_CHOICE': {
        'message': 'Gender choice is invalid',
        'code': 320
    },
    'GENDER_REQUIRED': {
        'message': 'Gender field is required',
        'code': 321
    },
    'BIRTHDAY_INVALID': {
        'message': 'BirthDate has wrong format. Use one of these formats instead: YYYY-MM-DD.',
        'code': 325
    },
    'BIRTHDAY_REQUIRED': {
        'message': 'The birthday field is required',
        'code': 326
    },
    'NOT_ENOUGH_AGE': {
        'message': 'You are not enough age',
        'code': 327
    },
    'ADDRESS_BLANK': {
        'message': 'Address field cannot be blank',
        'code': 330
    },
    'ADDRESS_MIN_LENGTH': {
        'message': 'Ensure address field has at least 10 characters',
        'code': 332
    },
    'ADDRESS_MAX_LENGTH': {
        'message': 'Ensure address field has no more than 100 characters',
        'code': 333
    },
    'ADDRESS_REQUIRED': {
        'message': 'The address field is required',
        'code': 334
    },
    'PHONE_NUMBER_MIN_LENGTH': {
        'message': 'Ensure phone number field has at least 10 characters',
        'code': 335
    },
    'PHONE_NUMBER_MAX_LENGTH': {
        'message': 'Ensure phone number field has no more than 13 characters',
        'code': 336
    },
    'PHONE_NUMBER_BLANK': {
        'message': 'Phone number field cannot be blank',
        'code': 337
    },
    'PHONE_NUMBER_REQUIRED': {
        'message': 'The phone number field is required',
        'code': 338
    },
    'PHONE_NUMBER_MUST_BE_STRING_NUMBER': {
        'message': 'The phone number must be string number',
        'code': 339
    },
    'BANK_NUMBER_MIN_LENGTH': {
        'message': 'Ensure bank number field has at least 10 characters',
        'code': 340
    },
    'BANK_NUMBER_MAX_LENGTH': {
        'message': 'Ensure bank number field has no more than 32 characters',
        'code': 341
    },
    'BANK_BRANCH_MAX_LENGTH': {
        'message': 'Ensure bank branch field has no more than 64 characters',
        'code': 342
    },
    'BANK_BRANCH_MIN_LENGTH': {
        'message': 'Ensure bank branch field has at least 10 characters',
        'code': 343
    },
    'BANK_NUMBER_MUST_BE_STRING_NUMBER': {
        'message': 'Ensure bank number is number',
        'code': 344
    },
    'USER_TYPE_INVALID_CHOICE': {
        'message': 'User type choice is invalid',
        'code': 345
    },
    'USER_TYPE_REQUIRED': {
        'message': 'User type field is required',
        'code': 346
    },

    'USER_IS_DELETED_BY_ANOTHER_ADMIN': {
        'message': 'This User is not exist or deleted by another admin',
        'code': 350
    },
    'SET_ID_CANT_BLANK': {
        'message': 'You must input user id to delete',
        'code': 351
    },
    'DELETE_FAILED': {
        'message': 'Delete processing failed',
        'code': 352
    },
    'QUANTITY_INVALID': {
        'message': 'Quantity must be number',
        'code': 353
    },
    'QUANTITY_MIN_VALUE': {
        'message': 'Quantity must be great than 0',
        'code': 354
    },
    'QUANTITY_MAX_VALUE': {
        'message': 'Quantity cannot be great than 10000',
        'code': 355
    },
    'PRODUCT_TYPE_INVALID_CHOICE': {
        'message': 'Product type is incorrect',
        'code': 356
    },

    'COLOR_INVALID_CHOICE': {
        'message': 'Color is incorrect',
        'code': 357
    },

    'SIZE_INVALID_CHOICE': {
        'message': 'Size is incorrect',
        'code': 358
    },
    'NAME_MIN_LENGTH': {
        'message': 'Name field must great than 5 character',
        'code': 359
    },
    'NAME_MAX_LENGTH': {
        'message': 'Name field must less than 40 character',
        'code': 360
    },
    'DESCRIPTION_MIN_LENGTH': {
        'message': 'Description field must great than 5 character',
        'code': 361
    },
    'DESCRIPTION_MAX_LENGTH': {
        'message': 'Description field must less than 200 character',
        'code': 362
    },
    'PRICE_MIN_VALUE': {
        'message': 'Price must great than 0 value',
        'code': 363
    },
    'PRICE_INVALID': {
        'message': 'Price must be number',
        'code': 364
    },

    'ADDRESS_RECEIVE_MIN_LENGTH': {
        'message': 'Address receive must great than 10 character',
        'code': 365
    },
    'PAY_TYPE_INVALID_CHOICE': {
        'message': 'Pay type is invalid',
        'code': 370
    },

    'STATUS_INVALID_CHOICE': {
        'message': 'Status is invalid',
        'code': 372
    },

    'USER_ID_DOES_NOT_EXIST': {
        'message': 'This user is not exist or deleted',
        'code': 375
    },
    'PRODUCT_INFO_ID_DOES_NOT_EXIST': {
        'message': 'This product is not exist or deleted',
        'code': 377
    },
    'PRODUCT_ID_DOES_NOT_EXIST': {
        'message': 'This product is not exist or deleted',
        'code': 378
    },
    'ENOUGH_PRODUCT_QUANTITY': {
        'message': 'Not enough product in store',
        'code': 380
    },
    'CART_CANNOT_CHANGE': {
        'message': 'Your cart is confirmed, cannot change',
        'code': 381
    },
    'PRODUCT_INFO_REQUIRED': {
        'message': 'you must provide product info',
        'code': 382
    },

    'PARSE_JSON_FAIL': {
        'message': 'Json ParseError,incorrect format',
        'code': 909
    },
    'NOT_ENOUGH_PERMISSION': {
        'message': "you not enough permission for this action!",
        'code': 915
    },
    'UNKNOWN_ERROR': {
        'message': 'Unknown error',
        'code': 991
    }
}
