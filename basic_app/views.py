from django.shortcuts import render
from . models import Services, ai_showcase, Get_In_Touch



def home(request):
    admin_services = Services.objects.all()
    return render(request,'home.html', {'admin_services': admin_services})




def solution1(request):
    ai_showcasee = ai_showcase.objects.all()    
    return render(request,'solution1.html', {'ai_showcasee': ai_showcasee})

def contact(request):
    get_in_touch_items = Get_In_Touch.objects.all()
    return render(request, 'contact.html', {'get_in_touch_items': get_in_touch_items})


def about(request):
    return render(request,'about.html')

# def solution(request):
#     return render(request,'solution.html')


