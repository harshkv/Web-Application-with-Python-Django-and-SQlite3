from django.db import models

# Create your models here.
class Employee(models.Model):
    # emp_id = models.CharField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    emp_email = models.EmailField(max_length=100, unique = True)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=50)



    class Meta:
        db_table = 'Employee'    # to rename the table only

    def __str__(self):
        return self.emp_name


class Education(models.Model):
    #models.cascade
    #models.protect
    employee = models.ForeignKey(Employee,on_delete=models.PROTECT)
    edu_name = models.CharField(max_length=50)
    edu_type = models.CharField(max_length =50)
    edu_uni = models.CharField(max_length=10)

    class Meta:
        db_table ='emp_education'

    def __str__(self):
        return self.edu_name