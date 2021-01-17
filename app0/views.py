
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import User
from django.template import loader
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import UserForm



def index1(request):
    users = User.objects.all()
    template = loader.get_template('app0/index1.html')
    context = {
        'users': users
    }
    return HttpResponse(template.render(context, request=request))

def detail_element(request,user_id):
    user = User.objects.get(pk=user_id)
    context = {
        'user_id':user.id ,
         'user_name':user.name,
         'user_number': user.carNumber,
         'created':user.created_at
    }
    return render(request, 'app0/det.html', context)
def ajouter(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            carNumber = request.POST.get('carNumber')
            user = User.objects.filter(carNumber=carNumber)
            if not user.exists():
                user =User.objects.create(
                     name=name,
                     carNumber= carNumber
                                     )
            messages.success(request,'successfully!')
            return HttpResponseRedirect('/app0/')
        else:
            context = {
               'form': form
             }
            return HttpResponseRedirect('/app0/')
    else:
        form = UserForm()
        context['form'] = form  
    return render(request, 'app0/add.html',context)

def search(request):
    query=request.GET.get('query')
    if not query:
        users=User.objects.all()
    name = "Résultats pour la requête %s"%query
    context = {
        'users':  users,
        'name' : name ,   
    }
    return render(request, 'app0/search.html', context)
def delete(request):
    users = User.objects.filter('selectioner').delete()
    context = {
        'users':  users    
    }
    return render(request, 'app0/list.html', context)



def ind(request):
    return render(request, 'app0/search.html')
def users(request):
    return render(request, 'users.html')
def list(request):
    return render(request, 'app0/list.html')

  