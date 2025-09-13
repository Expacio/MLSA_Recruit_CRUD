from flask import Flask, jsonify, request
import pymongo
from enum import Enum
from dotenv import load_dotenv, dotenv_values
import os

class TextColor(Enum):
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    RESET = "\033[0m"


def colortxt(text, color):
    return f"{color.value}{text}{TextColor.RESET.value}"

load_dotenv()
print(colortxt("Connecting to MongoDB...", TextColor.BRIGHT_YELLOW))
mongoclient = pymongo.MongoClient(os.getenv("MONGO_URI"))
print(colortxt("Connected to MongoDB", TextColor.BRIGHT_GREEN))
app = Flask(__name__)

class Student:
    def __init__(self, name, branch, reg_no, hostel, dob):
        self.name = name
        self.reg_no = reg_no
        self.branch = branch
        self.hostel = hostel
        self.dob = dob

@app.route('/')
def index():
    return "works!"

@app.route("/api/students/all", methods=["GET"])
def get_students():
    students = list(mongoclient["memnotes"]["students"].find())
    if not students:
        return jsonify({"message": "No students in this db!"}), 404
    for s in students:
        s["_id"] = str(s["_id"])
    return jsonify(students)


@app.route("/api/students/findbyid/<string:regno>", methods=["GET"])
def findbyid(regno):
    db = mongoclient['memnotes']
    students = db['students']
    particular_student = students.find_one({"reg_no": regno})
    if not particular_student:
        return jsonify({"message": 'No such student found'}), 404
    student = Student(name=particular_student['name'], branch=particular_student['branch'], reg_no=particular_student['reg_no'], hostel=particular_student['hostel'], dob=particular_student['dob'])
    return jsonify(student.__dict__)

@app.route("/api/students/admit", methods=["POST"])
def admit():
    data = request.get_json()
    #we will do some data validation here
    if not all (k in data for k in ('name', 'branch', 'reg_no', 'hostel', 'dob')):
        return jsonify({"error": "Invalid data"}), 400
    mongoclient['memnotes']['students'].insert_one(data)
    data['_id'] = str(data['_id'])
    return jsonify({"message": "Student admitted successfully", "admission": data})

@app.route("/api/students/deletebyid/<string:regno>", methods=["DELETE"])
def delete_by_id(regno):
    result = mongoclient['memnotes']['students'].delete_one({"reg_no": regno})
    if result.deleted_count == 0:
        return jsonify({"message": "No student is there with given registration number"}), 404
    return jsonify({"message": "Student deleted successfully!"})

@app.route("/api/students/update/<string:regno>", methods=["PUT"])
def update_student(regno):
    data = request.get_json()
    if not data:
        return jsonify({"err": "No data provided"}), 400
    db = mongoclient['memnotes']
    students = db['students']
    result = students.update_one({"reg_no": regno}, {"$set": data})
    if result.modified_count == 0:
        return jsonify({"message": "No student found with this registration no"})
    return jsonify({"message": "student updated successfully!"})

if __name__ == "__main__":
    app.run('0.0.0.0')