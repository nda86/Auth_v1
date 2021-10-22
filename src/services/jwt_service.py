from flask_jwt_extended import create_access_token, create_refresh_token


class JWTService:
    """Сервис для работы с JWT"""

    def gen_access_token(self, user: object) -> str:
        """Генерирует и возвращает access token"""
        access_token = create_access_token(identity=user)
        return access_token

    def gen_refresh_token(self, user: object) -> str:
        """Генерирует и возвращает access token"""
        refresh_token = create_refresh_token(user)
        return refresh_token
