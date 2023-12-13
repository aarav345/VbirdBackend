from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from routes.route import router

app = FastAPI()


app.include_router(router)


# Enable CORS (Cross-Origin Resource Sharing) to allow requests from your React Native app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this with the appropriate origin(s)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




