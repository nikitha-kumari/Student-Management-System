from .models import CourseContent
from django import forms


class AddCourseContentForm(forms.ModelForm):
    class Meta:
        model=CourseContent
        fields = "__all__"