from lib2to3.fixes.fix_input import context
from sys import exception
from .forms import NewAccount,LoginForm
from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from .models import*
from django.shortcuts import get_object_or_404
from .models import Account


# Create your views here

def create_account(request):
    context = {}

    if request.method == 'POST':
        form = NewAccount(request.POST, request.FILES)
        # if form.is_valid():
        # print(request.POST)
        # print(request.FILES['profile_image'])

        # form = NewAccount(request.POST)
        # context['form'] = form
        if form.is_valid():
            id = form.cleaned_data['id']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            image = form.cleaned_data['image']


            Account.create_account(id,name,email,password,image)
            return redirect('login')
            # print('success')
    else:
        form = NewAccount()
        context['form'] = form
    return render(request, 'account/create_account.html', context)


def update_account(request, id):

    account = get_object_or_404(Account, pk=id)

    if request.method == 'POST':

        account.name = request.POST.get('name')
        account.email = request.POST.get('email')
        account.password = request.POST.get('password')
        account.save()
        return redirect('account/update_account.html')


    context = {'id': id, 'account': account}
    return render (request, 'account/update_account.html', context)



def delete_account(request, id):
    context = {}
    try:
        Account.objects.filter(pk=id).delete()
        context = {"id": id, 'msg': 'account is deleted'}


    except:
        import sys
        context['error'] = sys.exc_info()[1]
    return render(request, 'account/delete_account.html', context)



def login(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                account = Account.objects.get(email=email, password=password)
                return redirect('account_detail', id=account.id)
            except Account.DoesNotExist:
                context['error'] = "Invalid email or password"
    else:
        form = LoginForm()
    context['form'] = form
    return render(request , 'account/account_login.html', context)

def list_account(request):
    context = {}
    accountsobj = Account.objects.all()
    context["accounts"] = accountsobj
    return render(request, "account/list_account.html", context)


def account_detail(request, id):
    account = get_object_or_404(Account, pk=id)
    return render(request, 'account/account_detail.html', {'account': account})
