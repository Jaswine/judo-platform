from django.http import JsonResponse


def create_response(message: str,
                    status_code: int) -> JsonResponse:
    """
        Формирует успешный ответ API
    """
    status = "info"

    positive_status_codes, bad_status_codes = [200, 201, 202, 203], [400, 401, 402, 403, 404, 405]

    if status_code in positive_status_codes:
        status = "success"
    if status_code in bad_status_codes:
        status = "error"

    return JsonResponse({
        'status': status,
        'message': message
    }, status=status_code)
