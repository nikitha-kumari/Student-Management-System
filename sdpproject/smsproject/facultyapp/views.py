# Create your views here.
from django.db.models import Q
from django.shortcuts import render

from adminapp.models import Faculty,FacultyCourseMapping,Course

def facultyhome(request):
    fid = request.session["fid"]
    return render(request,"facultyhome.html", {"fid": fid})

def facultycourses(request):
    fid = request.session["fid"]
    mappingcourses = FacultyCourseMapping.objects.all()
    fmcourses = []

    for course in mappingcourses:
        if (course.faculty.facultyid == int(fid)):
            fmcourses.append(course)

    print(fmcourses)
    dir(fmcourses)
    count = len(fmcourses)
    return render(request,"facultycourses.html", {"fid": fid,"fmcourses":fmcourses,"count":count
})

def checkfacultylogin(request):
    fid = request.POST["fid"]  # request.GET["uname"]
    pwd = request.POST["pwd"]  # request.GET["pwd"]
    flag = Faculty.objects.filter(Q(facultyid=fid) & Q(password=pwd))
    print(flag)
    if flag:
        print("login success")
        request.session["fid"] = fid  # creating sesson variable
        # return HttpResponse("Login Success")
        return render(request, "facultyhome.html", {"fid": fid})
    else:
        msg = "Login Failed"
        return render(request, "facultylogin.html", {"messege": msg})

def facultychangepwd(request):
    fid = request.session["fid"]
    return render(request,"facultychangepwd.html",{"fid":fid})

def facultyupdatepwd(request):
    fid = request.session["fid"]
    opwd=request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(fid,opwd,npwd)
    flag=Faculty.objects.filter(Q(facultyid=fid)&Q(password=opwd))
    if flag:
        print("old pwd is correct")
        Faculty.objects.filter(facultyid=fid).update(password=npwd)
        print("updated ...")
        msg="Password Updated Successfully"
    else:
        print("old pwd is wrong!!")
        msg="Old Password is Incorrect"
    #return HttpResponse("iam in admin change pass page")
    return render(request,"facultychangepwd.html",{"fid":fid,"messege":msg})

