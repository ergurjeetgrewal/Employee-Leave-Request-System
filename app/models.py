from django.db import models

# Create your models here.

class Employeeleave(models.Model):
    
    LEAVE_STATUS = (
        ('PENDING','PENDING'),
        ('APPROVED','APPROVED'),
        ('REJECTED','REJECTED'),
    )
    
    leave_applied_by = models.ForeignKey('accounts.CustomUser',on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=100)
    leave_description = models.CharField(max_length=100)
    leave_from = models.DateField()
    leave_to = models.DateField()
    leave_status = models.CharField(max_length=20,choices=LEAVE_STATUS,default='PENDING')
    leave_status_updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.leave_applied_by.first_name