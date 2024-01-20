from django.contrib import admin

from users.models import UserImage


@admin.register(UserImage)
class UserImageAdmin(admin.ModelAdmin):
    pass
