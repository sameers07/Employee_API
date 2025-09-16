# 📋 Employee Management API

A modern RESTful API for managing employee data built with **FastAPI** and **MongoDB**.  
This project shows **CRUD operations**, advanced searching, and real-world API practices.

---

## 🌟 Features

- ✅ Full CRUD Operations – Create, Read, Update, Delete employees  
- ✅ Advanced Filtering – Search by department, skills, and more  
- ✅ Data Analytics – Average salary calculations by department  
- ✅ Real-time Documentation – Interactive Swagger UI  
- ✅ Database Indexing – Optimized MongoDB performance  
- ✅ Error Handling – Proper error management  
- ✅ Async Operations – Non-blocking database calls  

---

## 🛠️ Tech Stack

- **Framework:** FastAPI (Python)  
- **Database:** MongoDB  
- **Async Driver:** Motor  
- **Validation:** Pydantic  
- **API Documentation:** Swagger UI  

---

## 📦 Installation

### Prerequisites
- Python **3.8+**  
- MongoDB installed and running  
- pip (Python package manager)  

### Setup Steps

1. Clone and navigate to the project:
   ```bash
   cd Employee_API
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start MongoDB:
   ```bash
   sudo systemctl start mongod                 # Linux
   brew services start mongodb-community       # Mac
   ```

5. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

6. Access the API:
   - API: [http://localhost:8000](http://localhost:8000)  
   - Docs: [http://localhost:8000/docs](http://localhost:8000/docs)  
   - Health: [http://localhost:8000/health](http://localhost:8000/health)  

---

## 🚀 API Endpoints

| Method | Endpoint                    | Description                     |
|--------|-----------------------------|---------------------------------|
| GET    | `/`                         | Welcome message                 |
| GET    | `/health`                   | API health status               |
| POST   | `/employees/`               | Create new employee             |
| GET    | `/employees/`               | List all employees              |
| GET    | `/employees/{employee_id}`  | Get specific employee           |
| PUT    | `/employees/{employee_id}`  | Update employee                 |
| DELETE | `/employees/{employee_id}`  | Delete employee                 |
| GET    | `/employees/avg-salary`     | Average salary by department    |
| GET    | `/employees/search`         | Search employees by skill       |

---

## 📝 Usage Examples

### Create an Employee
```bash
curl -X POST "http://localhost:8000/employees/"   -H "Content-Type: application/json"   -d '{
    "employee_id": "E001",
    "name": "John Doe",
    "department": "Engineering",
    "salary": 75000,
    "joining_date": "2023-01-15",
    "skills": ["Python", "MongoDB"]
  }'
```

### Get All Employees
```bash
curl http://localhost:8000/employees/
```

### Get Average Salary by Department
```bash
curl http://localhost:8000/employees/avg-salary
```

### Search Employees by Skill
```bash
curl "http://localhost:8000/employees/search?skill=Python"
```

---

## 🗃️ Database Schema

```json
{
  "employee_id": "string (unique)",
  "name": "string",
  "department": "string",
  "salary": "number",
  "joining_date": "ISODate",
  "skills": ["array", "of", "strings"]
}
```

---

## 📊 Project Structure

```text
Employee_API/
├── app/
│   ├── main.py          # FastAPI application setup
│   ├── database.py      # MongoDB connection
│   ├── models.py        # Pydantic models
│   ├── schemas.py       # Request/response schemas
│   └── routes/
│       └── employees.py # API endpoints
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

---

## 🧪 Testing

1. Visit [http://localhost:8000/docs](http://localhost:8000/docs)  
2. Click on any endpoint  
3. Click **Try it out**  
4. Enter required parameters  
5. Click **Execute**  

---

## 🔧 Configuration

Optional environment variable (`.env` file):

```bash
MONGODB_URL=mongodb://localhost:27018
```

---

## 🐛 Troubleshooting

- **MongoDB not running**  
  ```bash
  sudo systemctl start mongod
  ```

- **Port already in use**  
  ```bash
  lsof -ti:8000 | xargs kill
  ```

- **Dependencies issues**  
  ```bash
  pip install -r requirements.txt --upgrade
  ```

- **Database connection failed**  
  - Check if MongoDB is installed and running  
  - Verify connection string in `database.py`  

---

## 📈 Performance Features

- Async Database Operations – Non-blocking MongoDB queries  
- Indexed Fields – Faster searches on employee_id, department, skills  
- Connection Pooling – Efficient database connections  
- Input Validation – Prevents invalid data from reaching database  

---

## 🤝 Contributing

1. Fork the repository  
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit changes:
   ```bash
   git commit -m 'Add feature'
   ```
4. Push to branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request  


---

## 🎯 Learning Outcomes

This project demonstrates:  
- RESTful API design  
- MongoDB database integration  
- Async/await programming in Python  
- Pydantic data validation  
- API documentation with Swagger  
- Error handling and status codes  
- Database indexing and optimization  

---

🚀 **Happy Coding!**
