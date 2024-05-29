from django import forms

from app.models import * 

class Student_data(forms.Form):
    Student_Name=forms.CharField(max_length=50)
    Student_age=forms.IntegerField()
    Student_email=forms.EmailField()
    Student_url=forms.URLField()
    
    Student_password=forms.CharField(widget=forms.PasswordInput)
    g=[("MALE",'male'),('FEMALE','female')]
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    gender1=forms.ChoiceField(choices=g)
    
    c=[('PYTHON','python'),("HTML",'html'),("CSS",'css')]
    Scourse=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    Scourse1=forms.MultipleChoiceField(choices=c,widget=forms.SelectMultiple)
    
    Sdetails=forms.CharField(widget=forms.Textarea(attrs={"cols":10,'rows':10}))


class TopicForm(forms.Form):
    topic_name=forms.CharField()
    
class WebpageForm(forms.Form):
    topic_name=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField()
    url=forms.URLField()
     