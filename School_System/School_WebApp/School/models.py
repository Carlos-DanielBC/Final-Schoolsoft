from django.db import models


class Students(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birthdate = models.DateField()
    mail = models.CharField(max_length=200)
    phone_number = models.BigIntegerField()
    status = models.SmallIntegerField()

class Subject(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    description = models.CharField(max_length=200)
    level = models.CharField(max_length=200)

class Teachers(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    code = models.IntegerField()
    id_number = models.CharField('cedula',max_length=11)
    # subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
class Relationship(models.Model):
    Subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Teachers_id =  models.ForeignKey(Teachers, on_delete=models.CASCADE)

class Parents(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    id_number = models.CharField('cedula',max_length=11)
    mail = models.CharField(max_length=200)
    phone_number = models.BigIntegerField()
    status = models.SmallIntegerField()

class Course(models.Model):
    level = models.CharField(max_length=200)

class Inscription(models.Model):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    course_id =  models.ForeignKey(Course, on_delete=models.CASCADE)
    date_inscription = models.DateTimeField()
    pay_status = models.SmallIntegerField()
    ref_pay = models.CharField(max_length=200)
    inscription_status = models.SmallIntegerField()
    


