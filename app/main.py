from fastapi import FastAPI
from app.routes.employees import router as employees_router
from app.database import client, database
import asyncio

app = FastAPI(
    title="Employee Management API",
    description="A REST API for managing employees with MongoDB",
    version="1.0.0"
)

# Include routers
app.include_router(employees_router)

@app.on_event("startup")
async def startup_event():
    try:
        # Test connection first
        await client.admin.command('ping')
        print("✅ MongoDB connection successful!")
        
        # Create indexes
        collection = database.employees
        await collection.create_index("employee_id", unique=True)
        await collection.create_index("department")
        await collection.create_index("skills")
        print("✅ MongoDB indexes created successfully")
        
    except Exception as e:
        print(f"❌ MongoDB connection failed: {e}")
        print("Please make sure MongoDB is running on localhost:27017")

@app.on_event("shutdown")
async def shutdown_event():
    client.close()
    print("✅ MongoDB connection closed")

@app.get("/")
async def root():
    return {"message": "Employee Management API"}

@app.get("/health")
async def health_check():
    try:
        # Test database connection
        await client.admin.command('ping')
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": "disconnected", "error": str(e)}
