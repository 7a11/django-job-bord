from django.contrib import admin

# Register your models here.
from job.models import Job , Category , applyy

admin.site.register(Job)
admin.site.register(Category)
admin.site.register(applyy)
