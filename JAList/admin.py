from django.contrib import admin
from .models import Applicant, Student_Information, School_Record, Scholarship, Status

admin.site.register(Applicant)
admin.site.register(Student_Information)
admin.site.register(School_Record)
admin.site.register(Scholarship)
admin.site.register(Status)

# Register your models here.
