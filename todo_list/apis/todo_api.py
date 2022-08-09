from ninja import Router

router = Router()


@router.get("/")
def hello(_request):
    return {"message": "Hello, World!"}
