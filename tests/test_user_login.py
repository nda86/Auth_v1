from http import HTTPStatus

from .validation.schema import JWTResponseSchema
from .validation.validator import Validator


def test_wrong_username(test_db, create_user, login_user):
    """Проверка попытки входа с неверным username"""
    create_user(data=dict(username="admin", password="admin", email="lol@mail.com"))
    rv = login_user(data=dict(username="wrong_username", password="admin"))

    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert rv.json.get("description") == "Wrong username or password"


def test_wrong_password(test_db, create_user, login_user):
    """Проверка попытки входа с неверным паролем"""
    create_user(data=dict(username="admin", password="admin", email="lol@mail.com"))
    rv = login_user(data=dict(username="admin", password="wrong_password"))

    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert rv.json.get("description") == "Wrong username or password"


def test_success_login(test_db, create_user, login_user):
    """Проверка ответа при успешном входе.
    Проверяется формат ответа, он должен соответсвовать заранее определённой структуре
    """
    create_user(data=dict(username="admin", password="adminadmin", email="lol@mail.com"))
    rv = login_user(data=dict(username="admin", password="adminadmin"))

    assert rv.status_code == HTTPStatus.OK
    assert Validator.validate_response(rv, JWTResponseSchema)
