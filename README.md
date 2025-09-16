Employee Management API 🚀
A simple and modern API to manage your company's employees. Built with FastAPI and MongoDB.

What This Does ✨
This API lets you:

Add new employees to your system

View, update, and delete employee info

Search employees by department or skills

See average salaries across departments

Get automatic documentation with examples

Quick Start 🏁
Make sure MongoDB is running:

bash
sudo systemctl start mongod
Install requirements:

bash
pip install -r requirements.txt
Run the API:

bash
uvicorn app.main:app --reload
Open your browser to:

http://localhost:8000 - Basic info

http://localhost:8000/docs - Interactive documentation (try here first!)

How to Use It 🎯
Add an Employee
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
Get Average Salaries
bash
curl http://localhost:8000/employees/avg-salary
Search by Skill
bash
curl "http://localhost:8000/employees/search?skill=Python"
Easy Testing ✅
The easiest way to test is through the built-in docs at http://localhost:8000/docs:

Click on any endpoint

Click "Try it out"

Fill in the example data

Click "Execute"

What's Inside 📁
text
Employee_Management_API/
├── app/
│   ├── main.py          # Main application
│   ├── database.py      # MongoDB connection
│   ├── models.py        # Data structures
│   └── routes/
│       └── employees.py # All the API endpoints
Need Help? 🤔
If something doesn't work:

Check if MongoDB is running: sudo systemctl status mongod

Make sure all dependencies are installed: pip install -r requirements.txt

Check the error messages in your terminal

You Built a Real API! 🎉
This isn't just a tutorial - this is the kind of API that companies actually use for employee management. Great job!

Happy coding! 😊
