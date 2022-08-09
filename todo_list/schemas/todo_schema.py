from ninja import ModelSchema
from ..models.todo_models import Todo


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


class TodoForm(ModelSchema):
    class Config:
        model = Todo
        model_fields = ["description", "finished", "category"]
