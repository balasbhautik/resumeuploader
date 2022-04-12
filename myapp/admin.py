from django.contrib import admin
from .models import Resume, Contact


# Register your models here.

@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'job_city',
                    'profile_image', 'my_file']



@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'dob', 'city', 'mobile', 'email']