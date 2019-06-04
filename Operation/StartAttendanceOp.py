import urllib
import urllib.request
import requests
import json

from Object.Course import Course
from Object.Exam import Exam
from Object.Professor import Professor
from Object.Room import Room
from Object.Student import Student
from Object.Time import Time
from Operation.setAttendance import setAttendance


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
        self.attendance = []

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

    def findAttendance(self, exam):
        for att in self.attendance:
            if att.exam.examId == exam.examId:
                return att
        temp = setAttendance().setExam(exam)
        self.attendance.append(temp)
        return self.attendance[-1]

    def sendToServer(self, exam):
        jsonObject = self.createJsonObject(exam)
        r = requests.post("http://142.93.134.194:8088/api/attendance", data=jsonObject)
        if r.status_code == 200:
            print("# The information was sent to server correctly")
        else:
            print(r.status_code, r.reason)
            print("# Unable to send information to server")
            f = open(r"D:\University\3971-2\SAD\Projects\4\Project4\examId" + str(exam.examId) + ".txt", "a")
            f.write(str(jsonObject))
            f.close()
            print("# Information is written in the file")

    def createJsonObject(self, exam):
        presentList = self.findAttendance(exam).getPresentList()
        presentListId = []
        for std in presentList:
            presentListId.append(std.getId())
        jsonObject = {}
        jsonObject.update({"examid": int(exam.examId)})
        if exam.isProfSigned:
            jsonObject.update({"is_teacher_signed": "true"})
        else:
            jsonObject.update({"is_teacher_signed": "false"})
        jsonObject.update({"present_students_list": presentListId})
        return jsonObject
