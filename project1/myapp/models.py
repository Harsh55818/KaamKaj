from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=50)
    contact_number = models.IntegerField()
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=8)

class Intern(models.Model):
    name = models.CharField(max_length=50)
    contact_number = models.IntegerField()
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=8)

class Poster(models.Model):
    company_name = models.CharField(max_length=200)
    company_description = models.TextField()
    internship_description = models.TextField()
    responsibilities = models.TextField()
    qualification = models.TextField()
    benefits = models.TextField()
    cost = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()
    contact_info = models.TextField()
    contact_info2 = models.TextField(null=True)
    feedback = models.TextField()
