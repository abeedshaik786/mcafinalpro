from django import forms
from django.forms import ModelForm,Textarea
from .models import Company,StudentData

class CompanyFormmodel(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(CompanyFormmodel,self).__init__(*args, **kwargs)
        #self.fields.widget.attrs["class"] = " form-control "
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = " form-control "
          

    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
                'Description': Textarea(attrs={'cols':80 ,'rows':5}),
                'JobDescription': Textarea(attrs={'cols':80 ,'rows':5})

                }
class StudentDataFormmodel(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(StudentDataFormmodel,self).__init__(*args, **kwargs)
        #self.fields.widget.attrs["class"] = " form-control "
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = " form-control "
    
    class Meta:
        model = StudentData
        fields = '__all__'
