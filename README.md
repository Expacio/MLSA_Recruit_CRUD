# My MLSA Recruitment Project (Backend CRUD API)


## Project overview
This project consists of a backend API developed on Python (Flask) consisting of a Student-Data API.


---

## Features
- Basic CRUD API for Students-Based APIs
- Features: admitting students alongwith their **name**, **branch**, **registration number**, **hostel name**, **date of birth**
- This requires understanding of Python, Flask, MongoDB and how HTTP endpoints work 

---

###  Tech Stack
[![Python](https://img.shields.io/badge/Python-3776AB?logo=pytclickhon&logoColor=fff)](#)
[![Flask](https://img.shields.io/badge/Flask-000?logo=flask&logoColor=fff)](#)
[![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?logo=mongodb&logoColor=white)](#)

### Installation
```bash
python3 -m requirements.txt
```
This installs our major requirements such as Flask, PyMongo (official MongoDB driver for Python) and dotenv

### Endpoints
| Endpoint | Method | Description |
|---|---:|---|
| /api/students/all | GET | Lists all students currently admitted (in a JSON format) |
| /api/students/findbyid/ADD_regno_HERE | GET | Lists details of a student in a JSON format (using request JSON body) |
| /api/students/admit | POST  | Admits a student into the MongoDB database (data from request JSON body) |
| /api/students/delete | DELETE | Removes a student from the database |
| /api/students/update/ADD_regno_HERE | DELETE | Updates a student's info based on what request body JSON you supply |

### Live Deployment (pls work 🙏🙏🙏)
[Click to visit render.com deployment](https://mlsa-recruit-crud.onrender.com/)

---
