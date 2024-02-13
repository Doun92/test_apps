from django.shortcuts import render

# Create your views here.
def page_test(request):
    context = {
        "none": "none"
    }
    return render(request,'create_character/page_test.html',context)