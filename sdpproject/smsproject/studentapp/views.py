from django.db.models import Q
from django.shortcuts import render

from  adminapp.models import Student,Course
from facultyapp.models import CourseContent


# Create your views here.

def studenthome(request):
    sid = request.session["sid"]
    student = Student.objects.get(studentid=sid)
    print(student)


    return render(request,"studenthome.html", {"sid": sid,"student":student})

def checkstudentlogin(request):
    sid = request.POST["sid"]  # request.GET["uname"]
    pwd = request.POST["pwd"]  # request.GET["pwd"]
    flag = Student.objects.filter(Q(studentid=sid) & Q(password=pwd))
    print(flag)
    if flag:
        print("login success")
        request.session["sid"] = sid  # creating sesson variable
        # return HttpResponse("Login Success")
        student = Student.objects.get(studentid=sid)
        print(student)
        return render(request, "studenthome.html", {"sid": sid})
    else:
        msg = "Login Failed"
        return render(request, "studentlogin.html", {"messege": msg})

def studentchangepwd(request):
    sid = request.session["sid"]
    return render(request,"studentchangepwd.html",{"sid":sid})

def studentupdatepwd(request):
    sid = request.session["sid"]
    opwd=request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(sid,opwd,npwd)
    flag=Student.objects.filter(Q(studentid=sid)&Q(password=opwd))
    if flag:
        print("old pwd is correct")
        Student.objects.filter(studentid=sid).update(password=npwd)
        print("updated ...")
        msg="Password Updated Successfully"
    else:
        print("old pwd is wrong!!")
        msg="Old Password is Incorrect"
    #return HttpResponse("iam in admin change pass page")
    return render(request,"studentchangepwd.html",{"sid":sid,"messege":msg})

def studentcourses(request):
    sid=request.session["sid"]
    return render(request,"studentcourses.html",{"sid":sid})

def studentcoursecontent(request):
    sid=request.session["sid"]
    content=CourseContent.objects.all();
    return render(request,"studentcoursecontent.html",{"sid":sid,"coursecontent":content})


def displaystudentcourses(request):
    academic_year = request.POST["academic_year"]
    semester = request.POST["semester"]
    sid=request.session["sid"]
    courses=Course.objects.filter(Q(academicyear=academic_year)&Q(semester=semester))
    return render(request,"displaystudentcourses.html",{"courses":courses,"sid":sid})
