from fastapi import FastAPI
import uvicorn
from routes.user import userRoute
from routes.auth import authRoute
from routes.post import postRoute

app = FastAPI()
app.include_router(authRoute)
app.include_router(userRoute)
app.include_router(postRoute)


@app.get("/")
async def indexPage():
    return {"message_0": 'Hello! This is the backend/API services for fluffr.cf!',
            "message_1": "If you got here by accident, don't worry, you didnt break anything. Just head back to "
                         "fluffr.cf and everything will be fine!",
            "message_2": "As for those here on purpose, you found our API service! Well done! Please leave lol."
    }


if __name__ == "__main__":
    uvicorn.run("index:app",
                host="0.0.0.0", port=3000,
                reload=True)
