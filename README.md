📋 Employee Management API
A modern, RESTful API for managing employee data built with FastAPI and MongoDB. This project demonstrates full CRUD operations, advanced querying, and real-world API development practices.

🌟 Features
✅ Full CRUD Operations - Create, Read, Update, Delete employees

✅ Advanced Filtering - Search by department, skills, and more

✅ Data Analytics - Average salary calculations by department

✅ Real-time Documentation - Interactive Swagger UI

✅ Database Indexing - Optimized MongoDB performance

✅ Error Handling - Comprehensive error management

✅ Async Operations - Non-blocking database calls

🛠️ Tech Stack
Framework: FastAPI (Python)

Database: MongoDB

Async Driver: Motor

Validation: Pydantic

API Documentation: Swagger UI

📦 Installation
Prerequisites
Python 3.8+

MongoDB installed and running

pip (Python package manager)

Setup Steps
Clone and navigate to the project:

bash
cd mongo-employee-api
Create a virtual environment:

bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate    # Windows
Install dependencies:

bash
pip install -r requirements.txt
Start MongoDB:

bash
sudo systemctl start mongod  # Linux
# or
brew services start mongodb/brew/mongodb-community  # Mac
Run the application:

bash
uvicorn app.main:app --reload
Access the API:

API: http://localhost:8000

Documentation: http://localhost:8000/docs

Health Check: http://localhost:8000/health

🚀 API Endpoints
Method	Endpoint	Description
GET	/	Welcome message
GET	/health	API health status
POST	/employees/	Create new employee
GET	/employees/	List all employees
GET	/employees/{employee_id}	Get specific employee
PUT	/employees/{employee_id}	Update employee
DELETE	/employees/{employee_id}	Delete employee
GET	/employees/avg-salary	Average salary by department
GET	/employees/search	Search employees by skill
📝 Usage Examples
Create an Employee
bash
curl -X POST "http://localhost:8000/employees/" \
  -H "Content-Type: application/json" \
  -d '{
    "employee_id": "E001",
    "name": "John Doe",
    "department": "Engineering",
    "salary": 75000,
    "joining_date": "2023-01-15",
    "skills": ["Python", "MongoDB"]
  }'
Get All Employees
bash
curl http://localhost:8000/employees/
Get Average Salary by Department
bash
curl http://localhost:8000/employees/avg-salary
Search Employees by Skill
bash
curl "http://localhost:8000/employees/search?skill=Python"
🗃️ Database Schema
javascript
{
  "employee_id": "string (unique)",
  "name": "string",
  "department": "string",
  "salary": "number",
  "joining_date": "ISODate",
  "skills": ["array", "of", "strings"]
}
📊 Project Structure
text
mongo-employee-api/
├── app/
│   ├
│   ├── main.py              # FastAPI application setup
│   ├── database.py          # MongoDB connection
│   ├── models.py            # Pydantic models
│   ├── schemas.py           # Request/response schemas
│   └── routes/
│       ├
│       └── employees.py     # API endpoints
├── requirements.txt         # Dependencies
└── README.md               # This file
🧪 Testing
The API includes built-in testing through the interactive Swagger UI:

Visit http://localhost:8000/docs

Click on any endpoint

Click "Try it out"

Enter required parameters

Click "Execute"

🔧 Configuration
Environment variables (optional):

bash
# In a .env file or environment variables
MONGODB_URL=mongodb://localhost:27018
🐛 Troubleshooting
Common Issues:
MongoDB not running:

bash
sudo systemctl start mongod
Port already in use:

bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill
Dependencies issues:

bash
pip install -r requirements.txt --upgrade
Database connection failed:

Check if MongoDB is installed and running

Verify connection string in database.py

📈 Performance Features
Async Database Operations: Non-blocking MongoDB queries

Indexed Fields: Faster searches on employee_id, department, skills

Connection Pooling: Efficient database connections

Input Validation: Prevents invalid data from reaching database

🤝 Contributing
Fork the repository

Create a feature branch: git checkout -b feature-name

Commit changes: git commit -m 'Add feature'

Push to branch: git push origin feature-name

Submit a pull request

📄 License
This project is open source and available under the MIT License.

🎯 Learning Outcomes
This project demonstrates:

RESTful API design principles

MongoDB database integration

Async/await programming in Python

Pydantic data validation

API documentation with OpenAPI/Swagger

Error handling and status codes

Database indexing and optimization

Happy Coding! 🚀


