from ninja import ModelSchema, Schema
from ..models.todo_models import Todo
from typing import Literal


class TodoDTO(ModelSchema):
    class Config:
        model = Todo
        model_fields = [
            "id",
            "description",
            "finished",
            "category",
            "created_at",
        ]


class TodoForm(Schema):
    description: str
    category: Literal["W", "L"]


class TodoUpdateForm(Schema):
    description: str
    finished: bool
    category: Literal["W", "L"]


class TodoFinishUpdateDTO(Schema):
    finished: bool
