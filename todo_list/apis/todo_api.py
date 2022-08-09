from ninja import Router
from ..schemas.todo_schema import TodoDTO, TodoForm
from ..models.todo_models import Todo
from typing import List

router = Router()


@router.get("", response=List[TodoDTO])
def hello(_request):
    todos = Todo.objects.all()
    return todos


@router.post("", response=TodoDTO)
def create_todo(_request, todo_form: TodoForm):
    todo = Todo(**todo_form.dict())
    todo.save()
    return todo
