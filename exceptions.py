class ApiException(Exception):
    http_equivalent_status = 500
    include_details = True
    default_public_error_message = "Internal Server Error"

class NotFoundError(ApiException):
    http_equivalent_status = 404
    include_details = True
    default_public_error_message = "Not found"

class BadRequestError(ApiException):
    http_equivalent_status = 400
    include_details = True
    default_public_error_message = "Bad request"

class CompanyNotExistsError(NotFoundError):
    default_public_error_message = "Company does not exist"

class CompanyWithSameNameExistError(BadRequestError):
    default_public_error_message = "A company with that name already exists "
