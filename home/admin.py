from django.contrib import admin
from .models import MyImage,Footer
# Register your models here.
@admin.register(MyImage)
class myImageModel(admin.ModelAdmin):
    list_display = ("title" , "image")

@admin.register(Footer)
class FooterModel(admin.ModelAdmin):
    list_display = ("title" , "content")