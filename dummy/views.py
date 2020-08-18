from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.contrib.auth import get_user_model
from django.contrib import messages 
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from django.contrib.auth import logout

User = get_user_model()

class Profile(TemplateView):
    template_name = 'profile.html'

    def get(self,request,*args,**kwargs):
        user = User.objects.all()
        return render(request,'profile.html',context = {'user':user})

# Create your views here.
class Login(TemplateView):
    template_name = 'login.html'

    def post(self,request,*args,**kwargs):
        try:
            email = request.POST.get('uname')
            password = request.POST.get('psw')
            user = User.objects.get(email=email)
            if(user != None):
                if password == user.password:
                    login(request,user)
                    return redirect('base:profile')
                else:
                    messages.error(request, 'Email or password is incorrect')
                    return render(request,'sign_up.html')
        except:
            messages.error(request, 'Email or password is incorrect')
            return render(request,'login.html')

class Signup(TemplateView):
    template_name = 'sign_up.html'

    def post(self,request,*args,**kwargs):
        try:
            import pdb;pdb.set_trace()
            email = request.POST.get('uname')
            username = request.POST.get('uname2')
            password = request.POST.get('psw')
            password2 = request.POST.get('psw2')
            if(password != password2 ):
                messages.error(request, 'Password does not match')
                return render(request,'sign_up.html')
            user = User.objects.filter(email=email)
            if user:
                messages.error(request, 'Email already exist')
            else:
                user = User.objects.filter(username=username)
                if user:
                    messages.error(request, 'Username already exists,Please change you username')
                else:
                    user = User.objects.create(email=email,password=password,username=username)
                    user.save()
                    messages.info(request,"Your accout has been created")
            return render(request,'sign_up.html')
        except:
            messages.error(request, 'Email or password is incorrect')
            return render(request,'sign_up.html')


class DeleteUser(TemplateView):
    def post(self,request,*args,**kwargs):
        user_id = request.POST.get('id')
        user = User.objects.get(id=user_id)
        user.delete()
        return JsonResponse({}, status = 200)


class Logout(TemplateView):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('/auth')


