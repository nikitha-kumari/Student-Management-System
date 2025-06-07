from django.db import models

# Create your models here.
class Admin(models.Model):
    id=models.AutoField(primary_key = True)
    username=models.CharField(max_length=100,blank=False,unique=True)
    password=models.CharField(max_length=100,blank=False)

    class Meta:
        db_table = "admin_table"
    def __str__(self):
        return self.username

class Course(models.Model):
    id = models.AutoField(primary_key=True)

    department_choices = (("CSE(Regular)" ,"CSE(R)"),("CSE(Honors)" ,"CSE(H)"),("CS&IT" ,"CSIT"))
    department = models.CharField(max_length=100, blank=False,choices=department_choices)

    program_choices = (("B.Tech", "B.Tech"), ("M.Tech", "M.Tech"))
    program = models.CharField(max_length=50, blank=False, choices=program_choices)

    academic_choices = (("2023-24", "2023-24"), ("2024-25", "2024-25"))
    academicyear = models.CharField(max_length=20, blank=False,choices=academic_choices)

    semester_choices = (("ODD", "ODD"), ("EVEN", "EVEN"))
    semester = models.CharField(max_length=10, blank=False,choices=semester_choices)
    year = models.IntegerField(blank=False)
    coursecode = models.CharField(max_length=20, blank=False)
    coursetitle = models.CharField(max_length=100, blank=False)
    LTPSK=models.CharField(max_length=10,blank=False)
    coursecredits=models.FloatField(blank=False)

    class Meta:
        db_table = "course_table"
    def __str__(self):
        return self.coursecode





class Student(models.Model):
    id=models.AutoField(primary_key=True)
    studentid=models.BigIntegerField(blank=False,unique=True)
    fullname = models.CharField(max_length=100, blank=False)

    gender_choices = (("MALE", "MALE"), ("FEMALE", "FEMALE"), ("OTHERS", "OTHERS"))
    gender = models.CharField(max_length=50, blank=False,choices=gender_choices)

    department_choices = (("CSE(Regular)", "CSE(R)"), ("CSE(Honors)", "CSE(H)"), ("CS&IT", "CSIT"))
    department = models.CharField(max_length=50, blank=False,choices=department_choices)

    program_choices = (("B.Tech", "B.Tech"), ("M.Tech", "M.Tech"))
    program = models.CharField(max_length=50, blank=False,choices=program_choices)

    sem_choices= (("ODD", "ODD"), ("EVEN", "EVEN"))
    semester = models.CharField(max_length=10, blank=False,choices=sem_choices)
    year = models.IntegerField(blank=False)
    password = models.CharField(max_length=100, blank=False,default="klu123")
    email = models.CharField(max_length=100, blank=False,unique=True)
    contact = models.CharField(max_length=100, blank=False,unique=True)

    class Meta:
        db_table = "student_table"
    def __str__(self):
        return str(self.studentid)




class Faculty(models.Model):
    id=models.AutoField(primary_key=True)
    facultyid=models.BigIntegerField(blank=False,unique=True)
    fullname = models.CharField(max_length=100, blank=False)
    gender_choices = (("MALE", "MALE"), ("FEMALE", "FEMALE"), ("OTHERS", "OTHERS"))
    gender = models.CharField(max_length=50, blank=False,choices=gender_choices)

    department_choices = (("CSE(Regular)", "CSE(R)"), ("CSE(Honors)", "CSE(H)"), ("CS&IT", "CSIT"))
    department = models.CharField(max_length=50, blank=False,choices=department_choices)

    qualification_choices = (("M.Tech", "M.Tech"), ("Ph.D", "Ph.D"))
    qualification = models.CharField(max_length=50, blank=False,choices=qualification_choices)

    designation_choices = (
    ("Prof", "Professor"), ("Assoc.Prof", "Associate Professor"), ("Assit.Prof", "Assistent Professor"))
    designation = models.CharField(max_length=50, blank=False,choices=designation_choices)

    password = models.CharField(max_length=100, blank=False,default="klu123")
    email = models.CharField(max_length=100, blank=False,unique=True)
    contact = models.CharField(max_length=100, blank=False,unique=True)

    class Meta:
        db_table = "faculty_table"
    def __str__(self):
        return str(self.fullname)

class FacultyCourseMapping(models.Model):
    mappingid=models.AutoField(primary_key=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    component_choices=(("L","Lecture"),("T","Tutorial"),("P","Practical"),("S","Skill"))
    components = models.CharField(max_length=10,blank=False,choices=component_choices)

    facultytype = models.BooleanField(blank=False,verbose_name="Faculty Type") # true = Main faculty,False = Assistance faculty
    sectionalloted = models.IntegerField(blank=False)


    class Meta:
        db_table = "facultycoursemapping_table"

    def __str__(self):
        return f"{self.course.coursetitle}--{self.faculty.fullname}"


