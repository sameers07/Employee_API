from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date

class EmployeeBase(BaseModel):
    employee_id: str
    name: str
    department: str
    salary: float
    joining_date: date
    skills: List[str] = []

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    department: Optional[str] = None
    salary: Optional[float] = None
    joining_date: Optional[date] = None
    skills: Optional[List[str]] = None

class Employee(EmployeeBase):
    id: str

    class Config:
        from_attributes = True

class DepartmentAvgSalary(BaseModel):
    department: str
    avg_salary: float
