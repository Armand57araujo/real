from fastapi import APIRouter, UploadFile, HTTPException
from backend.ai_detection import predict_ai_text, predict_ai_image, predict_ai_behavior

router = APIRouter(prefix="/ai-detection")

@router.post("/text")
async def detect_ai_text(text: str):
    result = predict_ai_text(text)
    return {"result": result, "message": f"This text is {result}."}

@router.post("/image")
async def detect_ai_image(file: UploadFile):
    try:
        result = predict_ai_image(file.file)
        return {"result": result, "message": f"This image is {result}."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/behavior")
async def detect_ai_behavior(behavior_text: str):
    result = predict_ai_behavior(behavior_text)
    return {"result": result, "message": f"This behavior is {result}."}
