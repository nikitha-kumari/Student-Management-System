from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddFacultyForm,AddStudentForm,StudentForm
from .models import Admin, Student, Faculty, Course,FacultyCourseMapping


# Create your views here.
def adminhome(request):
    adminuname = request.session["auname"]
    return render(request,"adminhome.html", {"adminuname": adminuname})



def logout(request):
    return render(request,"login.html")

def checkadminlogin(request):
    adminuname = request.POST["uname"] #request.GET["uname"]
    adminpwd = request.POST["pwd"]#request.GET["pwd"]

    flag=Admin.objects.filter(Q(username=adminuname)&Q(password=adminpwd))
    print(flag)
    if flag:
        print("login success")
        request.session["auname"] = adminuname#creating sesson variable
        #return HttpResponse("Login Success")
        return render(request,"adminhome.html", {"adminuname": adminuname})
    else:
        msg="Login Failed"
        return render(request,"login.html",{"messege":msg})

def viewstudents(request):
    students=Student.objects.all()
    count = Student.objects.count()
    auname = request.session["auname"]
    return render(request,"viewstudents.html",{"studentdata":students,"count":count,"adminuname":auname})
def viewfaculty(request):
    faculty = Faculty.objects.all()
    count = Faculty.objects.count()
    auname = request.session["auname"]
    return render(request,"viewfaculty.html",{"facultydata":faculty,"count":count,"adminuname":auname})

def viewcourses(request):
    courses = Course.objects.all()
    count = Course.objects.count()
    auname = request.session["auname"]
    return render(request,"viewcourses.html",{"coursesdata":courses,"count":count,"adminuname":auname})
def adminstudent(request):
    auname=request.session["auname"]
    return render(request,"adminstudent.html",{"adminuname":auname})

def adminfaculty(request):
    auname = request.session["auname"]
    return render(request,"adminfaculty.html",{"adminuname":auname})

def admincourse(request):
    auname = request.session["auname"]
    return render(request,"admincourse.html",{"adminuname":auname})

def addcourse(request):
    auname = request.session["auname"]
    return render(request,"addcourse.html",{"adminuname":auname})


def updatecourse(request):
    auname = request.session["auname"]
    courses = Course.objects.all()
    count = Course.objects.count()
    return render(request,"updatecourse.html",{"adminuname":auname,"courses":courses,"count": count})

def courseupdation(request,cid):
    auname = request.session["auname"]
    return render(request,"courseupdation.html",{"cid":cid,"adminuname":auname})

def  studentupdation(request,sid):
    print(sid)
    auname = request.session["auname"]
    student=get_object_or_404(Student,pk=sid)
    if request.method=="POST":
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return HttpResponse("Student Updated Successfully!!")
        else:
            return HttpResponse("Updation Failed")
    else:
        form=StudentForm(instance=student)

    return render(request,"studentupdated.html",{"form":form,"adminuname":auname})

def courseupdated(request):
    auname = request.session["auname"]

    cid = request.POST["cid"]
    courseid=int(cid)
    coursetitle = request.POST["coursetitle"]
    LTPSK = request.POST["LTPSK"]
    coursecredits = request.POST["coursecredits"]

    Course.objects.filter(id=courseid).update(coursetitle=coursetitle, LTPSK=LTPSK, coursecredits=coursecredits)
    msg = "Course Updated Successfully"
    return render(request, "courseupdation.html", {"msg": msg, "adminuname": auname,"cid":cid})

def insertcourse(request):
    auname = request.session["auname"]
    if request.method=="POST":
        dept=request.POST["dept"]
        program=request.POST["program"]
        academic_year=request.POST["academic_year"]
        semester=request.POST["semester"]
        year=request.POST["year"]
        coursecode=request.POST["coursecode"]
        coursetitle=request.POST["coursetitle"]
        LTPSK = request.POST["LTPSK"]
        coursecredits=request.POST["coursecredits"]
        #object creation
        course=Course(department=dept,program=program,academicyear=academic_year,semester=semester,year=year,coursecode=coursecode,
                      coursetitle=coursetitle,LTPSK=LTPSK,coursecredits=coursecredits)
        Course.save(course)
        message="Course Added Successfully!!!!"
        return render(request,"addcourse.html",{"msg":message,"adminuname":auname})


def deletecourse(request):
    auname = request.session["auname"]#auname is session variable
    courses = Course.objects.all()
    count = Course.objects.count()
    return render(request, "deletecourse.html", {"coursesdata": courses, "count": count,"adminuname":auname})

def coursedeletion(request,cid):
   # auname = request.session["auname"]
    Course.objects.filter(id=cid).delete()
    return redirect("deletecourse")
    #return HttpResponse("course deleted success")

def addfaculty(request):
    auname = request.session["auname"]
    form = AddFacultyForm()
    if request.method == "POST":
        form1=AddFacultyForm(request.POST)
        if form1.is_valid():
            form1.save()
            messege = "Faculty Added Successfully!!!"
            return render(request,"addfaculty.html", {"msg":messege,"form":form,"adminuname":auname})
        else:
            messege = "Failed to Add Faculty"
            return render(request, "addfaculty.html", {"msg": messege, "form": form,"adminuname":auname})

    return render(request,"addfaculty.html",{"form":form,"adminuname":auname})

def deletefaculty(request):
    auname = request.session["auname"]
    faculty = Faculty.objects.all()
    count = Faculty.objects.count()
    return render(request, "deletefaculty.html", {"facultydata": faculty,"count": count,"adminuname":auname})

def facultydeletion(request,fid):
    #auname = request.session["auname"]
    Faculty.objects.filter(id=fid).delete()
    return redirect("deletefaculty")
    #return HttpResponse("course deleted success")

def addstudent(request):
    auname = request.session["auname"]
    form = AddStudentForm()
    if request.method == "POST":
        form1 = AddStudentForm(request.POST)
        if form1.is_valid():
            form1.save()
            messege = "Student Added Successfully!!!"
            return render(request,"addstudent.html", {"msg":messege,"form":form,"adminuname":auname})
        else:
            messege = "Failed to Add Student"
            return render(request, "addstudent.html", {"msg": messege, "form": form, "adminuname": auname})

    return render(request,"addstudent.html",{"form":form,"adminuname":auname})

def updatestudent(request):
    auname = request.session["auname"]
    students = Student.objects.all()
    count = Student.objects.count()
    return render(request, "updatestudent.html", {"studentdata": students,"count": count
        ,"adminuname":auname})


def deletestudent(request):
    auname = request.session["auname"]
    students = Student.objects.all()
    count = Student.objects.count()
    return render(request, "deletestudent.html", {"studentdata": students,"count": count
        ,"adminuname":auname})


def studentdeletion(request,sid):
    auname = request.session["auname"]
    Student.objects.filter(id=sid).delete()
    return redirect("deletestudent")

def facultycoursemapping(request):
    auname = request.session["auname"]
    fmcourses=FacultyCourseMapping.objects.all()

    return render(request,"facultycoursemapping.html",{"adminuname":auname,"fmcourses":fmcourses})

def adminchangepwd(request):
    auname = request.session["auname"]
    return render(request,"adminchangepwd.html",{"adminuname":auname})

def adminupdatepwd(request):
    auname = request.session["auname"]
    opwd=request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(auname,opwd,npwd)
    flag=Admin.objects.filter(Q(username=auname)&Q(password=opwd))
    if flag:
        print("old pwd is correct")
        Admin.objects.filter(username=auname).update(password=npwd)
        print("updated ...")
        msg="Password Updated Successfully"
    else:
        print("old pwd is wrong!!")
        msg="Old Password is Incorrect"
    #return HttpResponse("iam in admin change pass page")
    return render(request,"adminchangepwd.html",{"adminuname":auname,"messege":msg})
