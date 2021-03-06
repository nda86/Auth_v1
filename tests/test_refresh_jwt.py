from http import HTTPStatus

from .validation.schema import JWTResponseSchema
from .validation.validator import Validator


def test_refresh_process(test_db, make_refresh_token, make_refresh_request):
    """Проверяем процесс получения новой пары токенов(access и refresh) взамен одного refresh tokena"""
    rv = make_refresh_request(make_refresh_token)

    assert rv.status_code == HTTPStatus.OK
    assert Validator.validate_response(rv, JWTResponseSchema)


def test_refresh_process_only_one(test_db, make_refresh_token, make_refresh_request):
    """Проверяем что по одному и тому же refresh токену нельзя получить access повторно"""
    refresh_token = make_refresh_token
    make_refresh_request(refresh_token)
    rv = make_refresh_request(refresh_token)

    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert (
        rv.json.get("description")
        == "Refresh token not found or was stolen. Please make sign-in and logout all other devices"
    )
