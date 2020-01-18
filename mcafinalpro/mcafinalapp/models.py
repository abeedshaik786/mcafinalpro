from django.db import models

# Create your models here.
class Company(models.Model):
    CompanyName = models.CharField(max_length=100,blank=False)
    Description = models.CharField(max_length=1000,blank=False)
    JobDescription = models.CharField(max_length=1000,blank=True)
    InterviewDate = models.DateTimeField()
    Skills = models.CharField(max_length=500,blank=True)
    InterviewLocation = models.CharField(max_length=1000,blank=True)
    HrNumber = models.IntegerField(max_length=12,blank=True)

    def __str__(self):
        return self.CompanyName
class StudentData(models.Model):
    StudentName = models.CharField(max_length=100)
    Qualification = models.CharField(max_length=100)
    studentSkills = models.CharField(max_length=500)
    Nationality = models.CharField(max_length=100)
    Religion = models.CharField(max_length=50)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True) 



