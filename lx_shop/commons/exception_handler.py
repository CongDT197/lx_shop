from rest_framework.exceptions import ErrorDetail
from rest_framework.status import HTTP_200_OK
from rest_framework.views import exception_handler
from commons.error_code import ErrorCode


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    response.status_code = HTTP_200_OK
    data = {'status': False}
    if response is not None:
        if exc.__class__.__name__ == 'ParseError':
            data['message'] = ErrorCode['PARSE_JSON_FAIL']['message']
            data['ErrorCode'] = ErrorCode['PARSE_JSON_FAIL']['code']
        else:
            try:
                error_code = get_error(exc.detail)
                print("error_code:",error_code)
                if error_code is None:
                    error_code = "UNKNOWN_ERROR"
            except:
                error_code = "UNKNOWN_ERROR"
            data['message'] = ErrorCode[error_code]['message']
            data['ErrorCode'] = ErrorCode[error_code]['code']
        response.data = data
    return response


def get_error(detail):
    if isinstance(detail, ErrorDetail):
        return detail
    if isinstance(detail, dict):
        for k, v in detail.items():
            a = get_error(v)
            if isinstance(a, ErrorDetail):
                return '{}_{}'.format(k, a.code).upper()
            elif a is not None:
                return a
    if isinstance(detail, list):
        for item in detail:
            s = get_error(item)
            if s is not None:
                return s
    return None
