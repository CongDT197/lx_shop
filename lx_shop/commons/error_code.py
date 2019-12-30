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
        'message': 'Entered email is invalid',
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
    'IDENTITY_CARD_MAX_LENGTH': {
        'message': 'Ensure identity card field has no more than 9 characters.',
        'code': 315
    },
    'IDENTITY_CARD_MIN_LENGTH': {
        'message': 'Ensure identity card field has at least 9 characters',
        'code': 316
    },
    'IDENTITY_CARD_REQUIRED': {
        'message': 'The identity card is required',
        'code': 317
    },
    'IDENTITY_CARD_UNIQUE': {
        'message': 'The identity card is available',
        'code': 318
    },
    'IDENTITY_CARD_MUST_BE_STRING_NUMBER': {
        'message': 'The identity card mus be string number',
        'code': 319
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
    'NOT_ENOUGH_WORKING_AGE': {
        'message': 'Ensure your employee enough working age',
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
        'code': 332
    },
    'ADDRESS_REQUIRED': {
        'message': 'The address field is required',
        'code': 333
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
    'POSITION_ID_REQUIRED': {
        'message': 'Position id field is required',
        'code': 350
    },
    'POSITION_ID_DOES_NOT_EXIST': {
        'message': 'Position id is not exist',
        'code': 351
    },
    'POSITION_ID_INCORRECT_TYPE': {
        'message': 'Position id is incorrect type',
        'code': 352
    },
    'DEPARTMENT_ID_DOES_NOT_EXIST': {
        'message': 'Department id is not exist',
        'code': 355
    },
    'DEPARTMENT_ID_INCORRECT_TYPE': {
        'message': 'Department id is incorrect type',
        'code': 356
    },
    'DEPARTMENT_MUST_ONLY_1_LEADER': {
        'message': 'Ensure you input have only 1 leader',
        'code': 357
    },
    'USER_DEPARTMENT_REQUIRED': {
        'message': 'Ensure you input have user_department',
        'code': 358
    },
    'DEPARTMENT_IS_DELETED_BY_ANOTHER_ADMIN': {
        'message': 'This department is not exist or deleted by another admin',
        'code': 359
    },
    'USER_IS_DELETED_BY_ANOTHER_ADMIN': {
        'message': 'This User is not exist or deleted by another admin',
        'code': 360
    },
    'SET_ID_CANT_BLANK': {
        'message': 'You must input user id to delete',
        'code': 365
    },
    'USER_ID_MUST_BE_INTEGER': {
        'message': 'User id must be in number',
        'code': 370
    },
    'USER_ID_DOES_NOT_EXIST': {
        'message': 'This user is not exist',
        'code': 371
    },
    'USER_ID_INCORRECT_TYPE': {
        'message': 'User id must be number',
        'code': 372
    },
    'DELETE_FAILED': {
        'message': 'Delete processing failed',
        'code': 375
    },
    'SHEET_NAME_INCORRECT': {
        'message': 'Ensure your file have name is "New_Staff"',
        'code': 390
    },
    'DEPARTMENT_NAME_MIN_LENGTH': {
        'message': 'Ensure your department name is great than 5 char',
        'code': 600
    },
    'DEPARTMENT_NAME_MAX_LENGTH': {
        'message': 'Ensure your department name is less than 64 character"',
        'code': 601
    },
    'DEPARTMENT_NAME_BLANK': {
        'message': 'Department name cannot be blank',
        'code': 602
    },
    'DEPARTMENT_NAME_REQUIRED': {
        'message': 'Ensure you have department_name field',
        'code': 603
    },
    'DEPARTMENT_USER_MUST_ONLY_1_VALUE': {
        'message': 'Department_user must only 1 value',
        'code': 604
    },
    'LEADER_MUST_HAVE_LEADER_PERMISSION': {
        'message': 'Leader of department must have leader permission!',
        'code': 605
    },
    'LEAVE_TYPE_MAX_LENGTH': {
        'message': 'Leave_type is less than 200 character',
        'code': 615
    },
   'LEAVE_TYPE_BLANK': {
        'message': 'Leave_type cannot be blank',
        'code': 616
    },
   'DESCRIPTION_MAX_LENGTH': {
        'message': 'Description is less than 200 character',
        'code': 617
    },
   'DESCRIPTION_BLANK': {
        'message': 'Description cannot be blank',
        'code': 618
    },
   'LEAVE_TYPE_IS_DELETED_BY_ANOTHER_ADMIN': {
        'message': 'This leave type is not exist or deleted by another admin',
        'code': 619
    },
    'PARSE_JSON_FAIL': {
        'message': 'Json ParseError,incorrect format',
        'code': 909
    },
    'FILE_UNSUPPORTED': {
        'message': "Unsupported this file's type",
        'code': 910
    },
    'INCORRECT_FORMAT_FILE_IMPORT': {
        'message': "Ensure your first row is header label",
        'code': 911
    },
    'INCORRECT_FORMAT_FILE_IMPORT_HEADER': {
        'message': "Ensure your header is correct label",
        'code': 912
    },
    'NOT_ENOUGH_PERMISSION': {
        'message': "you not enough permission for this action!",
        'code': 915
    },
    'UNKNOWN_ERROR': {
        'message': 'Unknown error',
        'code': 991
    },

    'NEW_PASSWORD_MAX_LENGTH': {
        'message': 'Ensure new password field has no more than 32 characters',
        'code': 1020
    },
    'NEW_PASSWORD_MIN_LENGTH': {
        'message': 'Ensure new password field has no less than 6 characters',
        'code': 1021
    },
    'NEW_PASSWORD_REQUIRED': {
        'message': 'new password field is required',
        'code': 1022
    },
    'NEW_PASSWORD_BLANK': {
        'message': 'new password field is not blank',
        'code': 1023
    },
    'NEW_PASSWORD_NULL': {
        'message': 'new password field may not be null.',
        'code': 1024
    },
    'NEW_PASSWORD_INVALID': {
        'message': 'new password field not a valid string.',
        'code': 1025
    },

    'VERIFIED_PASSWORD_MAX_LENGTH': {
        'message': 'Ensure verified password field has no more than 32 characters',
        'code': 1030
    },
    'VERIFIED_PASSWORD_MIN_LENGTH': {
        'message': 'Ensure verified password field has no more less 6 characters',
        'code': 1031
    },
    'VERIFIED_PASSWORD_REQUIRED': {
        'message': 'verified password field is required',
        'code': 1032
    },
    'VERIFIED_PASSWORD_BLANK': {
        'message': 'verified password field is not blank',
        'code': 1033
    },

    'VERIFIED_PASSWORD_NULL': {
        'message': 'verified password field may not be null.',
        'code': 1034
    },
    'VERIFIED_PASSWORD_INVALID': {
        'message': 'verified password field not a valid string.',
        'code': 1035
    },

    'EMAIL_BLANK': {
        'message': 'Email field is not blank',
        'code': 1040
    },
    'EMAIL_NULL': {
        'message': 'Email field may not be null.',
        'code': 1041
    },
    'EMAIL_MIN_LENGTH': {
        'message': 'Ensure email field has at least 8 characters.',
        'code': 1042
    },

    'PASSWORD_BLANK': {
        'message': 'Password field is not blank',
        'code': 1050
    },
    'PASSWORD_INVALID': {
        'message': 'password not a valid string',
        'code': 1051
    },
    'PASSWORD_NULL': {
        'message': 'password field may not be null.',
        'code': 1052
    },

    'TOKEN_REQUIRED': {
        'message': 'Authentication credentials were not provided',
        'code': 1060
    },
    'TOKEN_FORMAT': {
        'message': 'Invalid token header. No credentials provided.',
        'code': 1061
    },
    'TOKEN_INCORRECT': {
        'message': 'Incorrect authentication credentials.',
        'code': 1062
    },
    'TOKEN_IS_EXPIRED': {
        'message': 'Token has expired',
        'code': 1063
    },
    'EMAIL_PASSWORD_INVALID': {
        'message': 'Email/password invalid',
        'code': 1070
    },
    'PASSWORD_NOT_MATCH': {
        'message': 'Your passwords didnt match.',
        'code': 1071
    },
    'USERNAME_NOT_EXISTS': {
        'message': 'Email is not exists',
        'code': 1072
    },

    'FILE_INVALID': {
        'message': 'The submitted data was not a file. Check the encoding type on the form',
        'code': 1080
    },
    'FILE_MAX_LENGTH': {
        'message': 'size file must < 2MB',
        'code': 1081
    }
}
