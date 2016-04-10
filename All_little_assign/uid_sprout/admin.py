from django.contrib import admin

from models import User

admin.site.register(User)
# Register your models here.
class UserAdmin(admin.ModelAdmin):
	list_display = ('name','email','password')