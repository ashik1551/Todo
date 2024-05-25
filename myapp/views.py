from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import User_reg,Login_form,Task_reg,User_edit
from .models import User,Taskmodel
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator


def signin_required(fn):
    def wrapper(request,**kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            return fn(request,**kwargs)
    return wrapper

def login_id_check(fn):
    def wrapper(request,**kwargs):
        id=kwargs.get('key')
        data=Taskmodel.objects.get(id=id)
        if data.user!=request.user:
            return redirect('index')
        else:
            return fn(request,**kwargs)
    return wrapper


class Register(View):
    def get(self,request,**kwargs):
        form=User_reg()
        context={'form':form}
        return render(request,"register.html",context)
    
    def post(self,request,**kwargs):
        data=User_reg(request.POST)
        if data.is_valid():
            User.objects.create_user(**data.cleaned_data)
            return redirect('login')
        else:
            messages.error(request,"Username already exists")
            return redirect('register')

        
        
class Signin(View):
    def get(self,request,**kwargs):
        form=Login_form()
        return render(request,'login.html',{'form':form})
    
    def post(self,request,**kwargs):
        form=Login_form(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(username=u_name,password=pwd)
            if user:
                login(request,user)
                return redirect('index')
            else:
                messages.error(request,"incorrect username or password")
                return redirect('login')

@method_decorator(signin_required,name='dispatch')
class Add_task(View):
    def get(self,request,**kwargs):
        form=Task_reg()
        userdata=User.objects.get(username=request.user)
        data=Taskmodel.objects.filter(user=request.user).order_by('status')
        context={'form':form,'data':data,'userdata':userdata}
        return render(request,"index.html",context)
    
    def post(self,request,**kwargs):
        data=Task_reg(request.POST)       
        if data.is_valid():
            data.instance.user=request.user
            data.save()
            messages.success(request,"Task Added Sucessfully")
        return redirect('index')

@method_decorator(signin_required,name='dispatch')
@method_decorator(login_id_check,name='dispatch')
class Delete(View):
    def get(self,request,**kwargs):
        id=kwargs.get('key')
        Taskmodel.objects.get(id=id).delete()
        return redirect('index')
    
@method_decorator(signin_required,name='dispatch')
@method_decorator(login_id_check,name='dispatch')
class Update(View):
    def get(self,request,**kwargs):
        id=kwargs.get('key')
        data=Taskmodel.objects.get(id=id)
        if data.status:
            data.status=False
        else:
            data.status=True
        data.save()
        return redirect('index')

class Signout(View):
    def get(self,request,**kwargs):
        logout(request)
        return redirect('login')
    
class Delete_acc(View):
    def get(self,request,**kwargs):
        User.objects.get(username=request.user).delete()
        messages.success(request,"Account Deleted Successfully")
        return redirect('login')
    
class Profile(View):
    def get(self,request):
        data=User.objects.get(username=request.user)
        form=User_edit(instance=data)
        context={'data':data,'form':form}
        return render(request,"profile.html",context)
    
    def post(self,request):
        data=User.objects.get(username=request.user)
        form=User_edit(request.POST,instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile updated successfully")
        return redirect('index')
    