from django.db import models
from employees.models import Employee

class LeaveType(models.Model):
    name = models.CharField(max_length=100)
    default_days = models.IntegerField()

    def __str__(self):
        return self.name

class LeaveRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    applied_on = models.DateTimeField(auto_now_add=True)
    reviewed_on = models.DateTimeField(null=True, blank=True)
    reviewer = models.ForeignKey(Employee, related_name='reviewed_leaves', 
                                 on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.employee} - {self.leave_type} ({self.status})"
