from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from datetime import date, datetime
from app.database import get_employee_collection
from app.schemas import Employee, EmployeeCreate, EmployeeUpdate, DepartmentAvgSalary
from bson import ObjectId

router = APIRouter(prefix="/employees", tags=["employees"])

# Helper function to convert MongoDB document to Employee model
def employee_helper(employee) -> dict:
    # Convert datetime back to date if needed
    joining_date = employee["joining_date"]
    if isinstance(joining_date, datetime):
        joining_date = joining_date.date()
    
    return {
        "id": str(employee["_id"]),
        "employee_id": employee["employee_id"],
        "name": employee["name"],
        "department": employee["department"],
        "salary": employee["salary"],
        "joining_date": joining_date,
        "skills": employee.get("skills", [])
    }

# 1. Create Employee
@router.post("/", response_model=Employee, status_code=201)
async def create_employee(employee: EmployeeCreate):
    collection = get_employee_collection()
    
    # Check if employee_id already exists
    existing_employee = await collection.find_one({"employee_id": employee.employee_id})
    if existing_employee:
        raise HTTPException(status_code=400, detail="Employee ID already exists")
    
    # Convert date to datetime for MongoDB
    employee_dict = employee.model_dump()
    if isinstance(employee_dict.get('joining_date'), date):
        employee_dict['joining_date'] = datetime.combine(employee_dict['joining_date'], datetime.min.time())
    
    result = await collection.insert_one(employee_dict)
    new_employee = await collection.find_one({"_id": result.inserted_id})
    
    return employee_helper(new_employee)

# ... rest of your code remains the same ...

# 2. List Employees by Department (PUT THIS BEFORE PARAMETERIZED ROUTES)
@router.get("/", response_model=List[Employee])
async def list_employees(department: Optional[str] = Query(None)):
    collection = get_employee_collection()
    
    query = {}
    if department:
        query["department"] = department
    
    employees = await collection.find(query).sort("joining_date", -1).to_list(length=100)
    
    return [employee_helper(emp) for emp in employees]

# 3. Average Salary by Department (PUT SPECIFIC ROUTES BEFORE PARAMETERIZED ROUTES)
@router.get("/avg-salary", response_model=List[DepartmentAvgSalary])
async def avg_salary_by_department():
    collection = get_employee_collection()
    
    pipeline = [
        {
            "$group": {
                "_id": "$department",
                "avg_salary": {"$avg": "$salary"}
            }
        },
        {
            "$project": {
                "department": "$_id",
                "avg_salary": 1,
                "_id": 0
            }
        }
    ]
    
    result = await collection.aggregate(pipeline).to_list(length=100)
    return result

# 4. Search Employees by Skill (PUT SPECIFIC ROUTES BEFORE PARAMETERIZED ROUTES)
@router.get("/search", response_model=List[Employee])
async def search_employees_by_skill(skill: str = Query(...)):
    collection = get_employee_collection()
    
    employees = await collection.find({"skills": skill}).to_list(length=100)
    
    return [employee_helper(emp) for emp in employees]

# 5. Get Employee by ID (PARAMETERIZED ROUTES SHOULD COME LAST)
@router.get("/{employee_id}", response_model=Employee)
async def get_employee(employee_id: str):
    collection = get_employee_collection()
    employee = await collection.find_one({"employee_id": employee_id})
    
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    return employee_helper(employee)

# 6. Update Employee
@router.put("/{employee_id}", response_model=Employee)
async def update_employee(employee_id: str, employee_update: EmployeeUpdate):
    collection = get_employee_collection()
    
    # Check if employee exists
    existing_employee = await collection.find_one({"employee_id": employee_id})
    if not existing_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    # Prepare update data (exclude unset fields)
    update_data = {k: v for k, v in employee_update.model_dump(exclude_unset=True).items() if v is not None}
    
    if update_data:
        await collection.update_one(
            {"employee_id": employee_id}, 
            {"$set": update_data}
        )
    
    # Return updated employee
    updated_employee = await collection.find_one({"employee_id": employee_id})
    return employee_helper(updated_employee)

# 7. Delete Employee
@router.delete("/{employee_id}")
async def delete_employee(employee_id: str):
    collection = get_employee_collection()
    
    result = await collection.delete_one({"employee_id": employee_id})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    return {"message": "Employee deleted successfully"}
