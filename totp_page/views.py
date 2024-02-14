from django.shortcuts import render

# Create your views here.
def totp_homepage(request):
    contex = {
        "none": "none"
    }
    return render(request, 'totp_page/homepage.html',contex)