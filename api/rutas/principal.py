from fastapi import APIRouter
router=APIRouter()

@router.get("/default")
def read_root():
    return {"mensaje":"hola mundo"}