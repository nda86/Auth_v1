"""
Обрабатывает входящие запросы на /role/*
"""

from flask import Blueprint, Response
from flask_jwt_extended import jwt_required

from schemas import (AssignRoleSchema, CreateRoleSchema, DeleteRoleSchema,
                     UnassignRoleSchema, UpdateRoleSchema)
from services import RoleService
from utils import RequestValidator, admin_required

role_bp = Blueprint("role", __name__, url_prefix="/roles")


@role_bp.route("", methods=["POST"])
@jwt_required()
@admin_required
@RequestValidator.validate_body(CreateRoleSchema)
def create_role(data, role_service: RoleService) -> Response:
    """Запрос на создание роли
    data это словарь данных возвращаемым декоратором @validate_request.
    ---
    post:
      description: Создание роли
      security:
        - jwt_token: []
      requestBody:
        content:
          application/json:
            schema: CreateRoleSchema
      responses:
        200:
          description: Роль успешно создана
          content:
            application/json:
              schema: RoleResponseSchema
        400:
          description: Некорректный запрос
        401:
          description: Требуется авторизация
        403:
          description: Недостаточно прав для выполнения данного запроса
      tags:
        - Роли пользователя
    """

    return role_service.create_role(data)


@role_bp.route("", methods=["GET"])
@jwt_required()
@admin_required
def list_roles(role_service: RoleService) -> Response:
    """Запрос на список все ролей в бд
    ---
    get:
      description: Поучение списка ролей
      security:
        - jwt_token: []
      responses:
        200:
          description:
            type: array
            items:
              type: string
        401:
          description: Требуется авторизация
        403:
          description: Недостаточно прав для выполнения данного запроса
      tags:
        - Роли пользователя
    """
    return role_service.list_roles()


@role_bp.route("/<role_id>", methods=["DELETE"])
@jwt_required()
@admin_required
@RequestValidator.validate_view_args(schema=DeleteRoleSchema)
def delete_role(role_id: str, role_service: RoleService) -> Response:
    """Запрос на удаление роли
    ---
    delete:
      description: Удаление роли
      security:
        - jwt_token: []
      parameters:
      - name: role_id
        in: path
        description: идентификатор удаляемой роли
        required: true
        schema: DeleteRoleSchema
      responses:
        200:
          description: Роль успешно удалена
        401:
          description: Требуется авторизация
        403:
          description: Недостаточно прав для выполнения данного запроса
        404:
          description: Роль не найдена в бд
      tags:
        - Роли пользователя
    """
    return role_service.delete_role(role_id)


@role_bp.route("", methods=["PUT"])
@jwt_required()
@admin_required
@RequestValidator.validate_body(schema=UpdateRoleSchema)
def update_role(data, role_service: RoleService) -> Response:
    """Запрос на обновление роли
    data - провалидированные данные
    ---
    put:
      description: Редактирование роли
      security:
        - jwt_token: []
      content:
        application/json:
          schema: UpdateRoleSchema
      responses:
        200:
          description: Роль успешно изменена
          content:
            application/json:
              schema: RoleResponseSchema
        400:
          description: Некорректный запрос
        401:
          description: Требуется авторизация
        403:
          description: Недостаточно прав для выполнения данного запроса
      tags:
        - Роли пользователя
    """
    return role_service.update_role(data)


@role_bp.route("/assign", methods=["POST"])
@jwt_required()
@admin_required
@RequestValidator.validate_body(schema=AssignRoleSchema)
def assign_role(data, role_service: RoleService) -> Response:
    """Запрос на добавление роли
    data - провалидированные данные
    ---
    post:
      description: Добавление роли пользователю
      security:
        - jwt_token: []
      content:
        application/json:
          schema: AssignRoleSchema
      responses:
        200:
          description: Роль успешно назначена
        400:
          description: Некорректный запрос
        401:
          description: Требуется авторизация
        403:
          description: Недостаточно прав для выполнения данного запроса
      tags:
        - Роли пользователя
    """
    return role_service.assign_role(data)


@role_bp.route("/unassign", methods=["POST"])
@jwt_required()
@admin_required
@RequestValidator.validate_body(schema=UnassignRoleSchema)
def unassign_role(data, role_service: RoleService) -> Response:
    """Запрос на удаление роли у пользователя
    data - провалидированные данные
    ---
    post:
      description: Удаление роли у пользователя
      security:
        - jwt_token: []
      content:
        application/json:
          schema: UnassignRoleSchema
      responses:
        200:
          description: Роль успешно отозвана
        400:
          description: Некорректный запрос
        401:
          description: Требуется авторизация
        403:
          description: Недостаточно прав для выполнения данного запроса
      tags:
        - Роли пользователя
    """
    return role_service.unassign_role(data)
