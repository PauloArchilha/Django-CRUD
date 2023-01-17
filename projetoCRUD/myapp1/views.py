from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

# Create your views here.


def index(request):
    users = User.objects.all()
    context = {
        'users': users
    }

    return render(request, 'index.html', context)


def create(request):

    if request.method == 'GET':
        form = UserForm()

        context = {
            'form': form,
        }
        return render(request, 'criar.html', context=context)
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)


def modify(request, user_id):
    context = {
        'id': user_id,

    }
    return render(request, 'user/index.html', context=context)
