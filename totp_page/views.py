import pyotp
from django.shortcuts import render

from .models import TOTPCode

def get_code(totp_code):
    no_space = totp_code.replace(" ","")
    totp = pyotp.TOTP(no_space)
    return totp.now()

# Create your views here.
def totp_homepage(request):
    list_totps = TOTPCode.objects.all()


    contex = {
        "list_totps": list_totps,
    }
    
    return render(request, 'totp_page/homepage.html',contex)