from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from .routes import auth

app = FastAPI()

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Your Vue.js frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Test MongoDB connection
@app.get("/test-db")
async def test_db():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client.volleyball_stats
        # Insert a test document
        test_result = db.test.insert_one({"test": "Hello MongoDB!"})
        return {"message": "Successfully connected to MongoDB!", "id": str(test_result.inserted_id)}
    except Exception as e:
        return {"error": str(e)}

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])

@app.get("/")
async def root():
    return {"message": "Volleyball Stats API"}