from django.contrib import admin
from web.models import RegistrationClass, AboutClass, IssuesClass, WhyfemmeClass,TextClass


# Register your models here.
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'dob', 'education', 'message')


admin.site.register(RegistrationClass, RegistrationAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image')


admin.site.register(AboutClass, AboutAdmin)


class IssuesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image')


admin.site.register(IssuesClass, IssuesAdmin)


class WhyfemmeAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image')


admin.site.register(WhyfemmeClass, WhyfemmeAdmin)


class TextAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(TextClass, TextAdmin)