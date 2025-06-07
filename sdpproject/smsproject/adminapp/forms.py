from django import forms

from .models import Faculty, Student


class AddFacultyForm(forms.ModelForm):
    class Meta:
        model=Faculty
        fields = "__all__" #all fields in the model,autofield is hided
        exclude = {"password"}#this will exclude the fields
        labels={"facultyid":"Enter Faculty ID","gender":"Select Gender","fullname":"Enter Fullname"}

class AddStudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields = "__all__" #all fields in the model,autofield is hided
        exclude = {"password"}#this will exclude the fields
        labels={"studentid":"Enter Student ID","gender":"Select Gender","fullname":"Enter Fullname"}

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields = "__all__" #all fields in the model,autofield is hided
        exclude={"studentid"}
