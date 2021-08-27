from django.shortcuts import render
from loginApp.new_user_form import NewUsers
from loginApp.login import UserLogin


# Create your views here.
def home(request):
    return render(request, 'loginApp/home.html')


def new_user(request):
    form = NewUsers()

    if request.method == 'POST':
        form = NewUsers(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return home(request)
    return render(request, 'loginApp/new_user.html', {'register': form})


def user_login(request):
    form = UserLogin()
    if request.method == 'GET':
        form = UserLogin(request.GET)

    return render(request, 'loginApp/login.html', {'login': form})
