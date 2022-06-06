from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html',{'greeting':'Your_name'})
def reverse(request):
    user_text=request.GET['usertext']
    reverse_text=user_text[::-1]


    kol=len(user_text.split())
    context={'usertext': user_text, 'reversetext':reverse_text,'kolvo':kol}


    return render(request,'reverse.html',context)

