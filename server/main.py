from fastapi import FastAPI, Response
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

images_folder_path = ""
json_path = ""

class Settings(BaseModel):
    images_folder_path: str
    json_path: str

@app.get("/image/{image_type}/{image_name}")
async def get_image(image_type: str, image_name: str):
    global images_folder_path
    image_bytes = b''
    try:
        image_path = os.path.join(images_folder_path, image_type, image_name)
            
        with open(image_path, 'rb') as f:
            image_bytes = f.read()
            
        if image_type in ['preview', 'thumbnail']:
            media_type = "image/webp"
        else:
            media_type = "image/png"
        
        return Response(image_bytes, media_type=media_type)
    
    except Exception:
        return Response(None, status_code=404)

@app.get("/metadata")
async def get_json():
    global json_path
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            return Response(f.read(), media_type="application/json")
    except Exception:
        return Response(None, status_code=404)

@app.post("/update/settings")
async def update_settings(settings: Settings):
    global images_folder_path
    global json_path
    
    images_folder_path = settings.images_folder_path
    json_path = settings.json_path
    
    return Response('{"message": "Successfully update settings."}', media_type="application/json")