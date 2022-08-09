from ninja import NinjaAPI
from todo_list.apis.todo_api import router as todo_router 

api = NinjaAPI()

api.add_router("/todo", todo_router)