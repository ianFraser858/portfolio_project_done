from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Job

# Register your models here.


class JobAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(Job, JobAdmin)
# admin.site.register(Job)
