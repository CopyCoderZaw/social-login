from django.contrib import admin
from .models import CustomUser,City,Year,Photo ### customuser city model
# Register your models here.
class CustomAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
admin.site.register(CustomUser,CustomAdmin)
admin.site.register(City)
admin.site.register(Year)
admin.site.register(Photo)