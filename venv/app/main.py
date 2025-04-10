from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.auth import router as auth_router
from routes.weather import router as weather_router
from routes.schemes import router as schemes_router
from routes.gemini import router as gemini_router  # New import

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your Next.js frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(weather_router, prefix="/api", tags=["weather"])
app.include_router(schemes_router, prefix="/api", tags=["schemes"])
app.include_router(gemini_router, prefix="/api", tags=["gemini"])  # New router

@app.get("/")
async def root():
    return {"message": "Welcome to the Authentication API"}