from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(EmployDetails)
admin.site.register(CostCenter)
admin.site.register(JobType)
admin.site.register(VisaType)
admin.site.register(Project)
admin.site.register(Division)
admin.site.register(SalaryGrade)
admin.site.register(Status)