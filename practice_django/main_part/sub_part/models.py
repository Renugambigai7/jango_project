from django.db import models

# Create your models here.
class register_table(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email_id=models.EmailField()
    password=models.CharField(max_length=50)
    
 
class course_table(models.Model):
    course_name=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email_id=models.EmailField()
    registered_for=models.CharField(max_length=50)
    primary_account_email_id=models.CharField(max_length=50)
    