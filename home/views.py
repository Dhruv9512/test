from django.shortcuts import render
from .models import MyImage,Footer
# Create your views here.
def home(request):
    image_data = MyImage.objects.filter(title="Profile Photo").first()

    context = {
        "home_Image":{"profile_photo":image_data},
    }
    return render(request, 'home/home.html',context)