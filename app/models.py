from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
from datetime import date
from bson import ObjectId

class EmployeeModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    employee_id: str
    name: str
    department: str
    salary: float
    joining_date: date
    skills: List[str] = []

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        json_schema_extra={
            "example": {
                "employee_id": "E123",
                "name": "John Doe",
                "department": "Engineering",
                "salary": 75000,
                "joining_date": "2023-01-15",
                "skills": ["Python", "MongoDB", "APIs"]
            }
        }
    )
