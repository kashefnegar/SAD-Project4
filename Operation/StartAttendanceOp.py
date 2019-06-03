import urllib
import urllib.request
import json

from Object.Course import Course
from Object.Exam import Exam
from Object.Professor import Professor
from Object.Room import Room
from Object.Student import Student
from Object.Time import Time


class StartAttendanceOp:
    def __init__(self):
        self.initData()
        link = "http://142.93.134.194:8088/api/attendance"
        with urllib.request.urlopen(link) as url:
            info = url.read().decode('utf8')
            self.setJsonData(info)

    def initData(self):
        self.exams = []
        self.date = ''
        self.status = ''

    def setJsonData(self, info):
        data = json.loads(info)
        self.status = data["status"]
        self.date = data["date"]
        self.setExams(data["classes"])

    def setExams(self, data):
        for exam in data:
            tempExam = self.createExam(exam)
            self.exams.append(tempExam)


    def createExam(self, examInfo):
        exam = Exam(examInfo["exam_id"])

        room = Room(examInfo["room_number"])
        exam.addRoom(room)

        start = examInfo["start_at"]
        end = examInfo["end_at"]
        exam.setTime(Time(self.date, start, end))

        course = Course(examInfo["course_name"])
        professor = self.createProf(examInfo["professor"])
        course.addProfessor(professor)
        exam.setCourse(course)

        for studentInfo in examInfo["students"]:
            student = self.createStudent(studentInfo)
            exam.addStudent(student, studentInfo["chair_number"])

        return exam

    def createProf(self, profInfo):
        firstName = profInfo["first_name"]
        lastName = profInfo["last_name"]
        profId = profInfo["id"]
        return Professor(firstName, lastName, profId)

    def createStudent(self, stdInfo):
        firstName = stdInfo["first_name"]
        lastName = stdInfo["last_name"]
        stdId = stdInfo["id"]
        return Student(firstName, lastName, stdId)