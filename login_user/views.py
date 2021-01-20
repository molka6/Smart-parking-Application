from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.template.loader import select_template


def home(request):
    """Home page."""
    return render(request, "home.html")
def index(request):
    return render(request, "index.html")
def user_login(request):
    """Authenticate a user."""
    # Etape 1 :
    username = request.POST["username"]
    password = request.POST["password"]

    # Etape 2 :
    user = authenticate(username=username, password=password)

    # Etape 3 :
    if user is not None:
        login(request,user)
        messages.add_message(request, messages.SUCCESS, "Vous êtes connecté !")
        return redirect("/app0/")
    else:
        messages.add_message(request, messages.ERROR, "Les champs renseignés sont invalides.")
        return redirect("homepage")
   


def user_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Vous êtes déconnecté !")
    return redirect("home")
