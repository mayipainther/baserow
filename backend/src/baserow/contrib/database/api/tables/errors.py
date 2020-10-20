from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND


ERROR_TABLE_DOES_NOT_EXIST = (
    'ERROR_TABLE_DOES_NOT_EXIST',
    HTTP_404_NOT_FOUND,
    'The requested table does not exist.'
)
ERROR_INVALID_INITIAL_TABLE_DATA = (
    'ERROR_INVALID_INITIAL_TABLE_DATA',
    HTTP_400_BAD_REQUEST,
    'The provided table data must at least contain one row and one column.'
)