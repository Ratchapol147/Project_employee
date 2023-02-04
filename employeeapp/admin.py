from django.contrib import admin
from employeeapp.models import employee
# Register your models here

class StatementAdmin(admin.ModelAdmin):
    list_display=['fname','lname']  #สร้างตาราง

admin.site.register(employee,StatementAdmin)
