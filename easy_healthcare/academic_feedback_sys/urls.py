from django.urls import path
from . import views


app_name = "academic_feedback_sys"

urlpatterns = [
    # TEACHER PATHS
    path("teacherhome/", views.TeacherHome, name="staff"),
    path("teacherprofile/", views.TeacherProfile, name="profile"),
    path("teacherstudents/", views.TeacherStudents, name="students"),
    path("teacherrecentgraded/", views.TeacherRecentGraded, name="recent_grades"),
    path("teachereditstudent/<str:first_name>/<str:middle_name>/<str:last_name>/", views.TeacherEditStudentGrade, name="edit_student_grade"),
]