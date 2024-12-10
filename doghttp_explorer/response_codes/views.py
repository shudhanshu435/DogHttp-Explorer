from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
import re

# Create your views here.
def home(request):
    return render(request, 'response_codes/home.html') # a basic home page

# Create your views here.
def home(request):
    return render(request, 'response_codes/home.html') # a basic home page

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user) # log the user in after signup
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'response_codes/signup.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('search')
    else:
        form = AuthenticationForm()
    return render(request, 'response_codes/login.html', {'form':form})

def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def search(request):
    filtered_codes = []
    images = []
    search_query = request.GET.get('query', '').strip()

    if search_query:
        # handling patterns like 2xx, 3xx, 4xx etc
        regex_pattern = search_query.replace('x', r'\d')
        print(f"Regex pattern: {regex_pattern}")
        for code in range(100,600): # http codes are in between 100 and 599
            if re.match(f"^{regex_pattern}$", str(code)):
                filtered_codes.append(code)
                images.append(f"https://http.dog/{code}.jpg")

    if request.method == 'POST':
        # save the filtered list
        name = request.POST.get('name')
        if not name:
            messages.error(request, "List name is required.")
        elif not filtered_codes:
            messages.error(request, "No response codes to save.")
        else:
            ResponseCodeList.objects.create(
                user=request.user,
                name=name,
                response_codes=",".join(map(str, filtered_codes)),
                image_links=",".join(images)
            )
            messages.success(request, f"List '{name}' saved successfully!")
            return redirect('lists')

    # pass the zipped lists directly to the template
    zipped = zip(filtered_codes, images)

    return render(request, 'response_codes/search.html',{
        'zipped': zipped,
        'query': search_query,
    })


@login_required
def lists(request):
    user_lists = ResponseCodeList.objects.filter(user=request.user)

    return render(request, 'response_codes/lists.html',{
        'lists': user_lists
    })


@login_required
def view_list(request, pk):
    try:
        response_list = ResponseCodeList.objects.get(pk=pk, user=request.user)
    except ResponseCodeList.DoesNotExist:
        messages.error(request, "List not found.")
        return redirect('lists')

    # response codes and images
    codes = response_list.response_codes.split(',')
    images = response_list.image_links.split(',')

    zipped = zip(codes, images)
    return render(request, 'response_codes/view_list.html', {
        'response_list': response_list,
        'zipped': zipped
    })


@login_required
def edit_list(request, pk):
    # get the list belonging to the logged-in user or return a 404 error if not found
    response_list = get_object_or_404(ResponseCodeList, pk=pk, user=request.user)

    if request.method == 'POST':
        # Fetch data from form
        name = request.POST.get('name')
        response_codes = request.POST.get('response_codes')

        # Validate
        if not name:
            messages.error(request, "List name is required.")
        elif not response_codes:
            messages.error(request, "At least one response code is required.")
        else:
            # Update the ResponseCodeList object
            response_list.name = name
            response_list.response_codes = response_codes.strip()  # Remove extra spaces
            response_list.image_urls = ",".join(
                [f"https://http.dog/{code.strip()}.jpg" for code in response_codes.split(',')]
            )
            response_list.save()
            messages.success(request, "List updated successfully!")
            return redirect('lists')  # Redirect to the lists page

    return render(request, 'response_codes/edit_list.html', {'response_list': response_list})

@login_required
def delete_list(request, pk):
    response_list = get_object_or_404(ResponseCodeList, pk=pk, user=request.user)
    ListName = response_list.name
    response_list.delete()
    messages.success(request, f"List '{ListName}' has been deleted.")
    return redirect('lists')  # after deleting redirect back to the list page

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user) # log the user in after signup
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'response_codes/signup.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('search')
    else:
        form = AuthenticationForm()
    return render(request, 'response_codes/login.html', {'form':form})

def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def search(request):
    filtered_codes = []
    images = []
    search_query = request.GET.get('query', '').strip()

    if search_query:
        # handle patterns like 2xx, 3xx, 4xx etc
        regex_pattern = search_query.replace('x', r'\d')
        print(f"Regex pattern: {regex_pattern}")
        for code in range(100,600): # http codes are in between 100 and 599
            if re.match(f"^{regex_pattern}$", str(code)):
                filtered_codes.append(code)
                images.append(f"https://http.dog/{code}.jpg")

    if request.method == 'POST':
        # save the filtered list
        name = request.POST.get('name')
        if not name:
            messages.error(request, "List name is required.")
        elif not filtered_codes:
            messages.error(request, "No response codes to save.")
        else:
            ResponseCodeList.objects.create(
                user=request.user,
                name=name,
                response_codes=",".join(map(str, filtered_codes)),
                image_links=",".join(images)
            )
            messages.success(request, f"List '{name}' saved successfully!")
            return redirect('lists')

    # pass the zipped lists directly to the template
    zipped = zip(filtered_codes, images)

    return render(request, 'response_codes/search.html',{
        'zipped': zipped,
        'query': search_query,
    })


@login_required
def lists(request):
    user_lists = ResponseCodeList.objects.filter(user=request.user)

    return render(request, 'response_codes/lists.html',{
        'lists': user_lists
    })


@login_required
def view_list(request, pk):
    try:
        response_list = ResponseCodeList.objects.get(pk=pk, user=request.user)
    except ResponseCodeList.DoesNotExist:
        messages.error(request, "List not found.")
        return redirect('lists')

    # Parse response codes and images
    codes = response_list.response_codes.split(',')
    images = response_list.image_links.split(',')

    zipped = zip(codes, images)
    return render(request, 'response_codes/view_list.html', {
        'response_list': response_list,
        'zipped': zipped
    })


@login_required
def edit_list(request, pk):
    # Retrieve the list belonging to the logged-in user or return a 404 error if not found
    response_list = get_object_or_404(ResponseCodeList, pk=pk, user=request.user)

    if request.method == 'POST':
        # Fetch data from form
        name = request.POST.get('name')
        response_codes = request.POST.get('response_codes')

        # Validate
        if not name:
            messages.error(request, "List name is required.")
        elif not response_codes:
            messages.error(request, "At least one response code is required.")
        else:
            # Update the ResponseCodeList object
            response_list.name = name
            response_list.response_codes = response_codes.strip()  # Remove extra spaces
            response_list.image_urls = ",".join(
                [f"https://http.dog/{code.strip()}.jpg" for code in response_codes.split(',')]
            )
            response_list.save()
            messages.success(request, "List updated successfully!")
            return redirect('lists')  # Redirect to the lists page

    return render(request, 'response_codes/edit_list.html', {'response_list': response_list})

@login_required
def delete_list(request, pk):
    response_list = get_object_or_404(ResponseCodeList, pk=pk, user=request.user)
    ListName = response_list.name
    response_list.delete()
    messages.success(request, f"List '{ListName}' has been deleted.")
    return redirect('lists')  # after deleting redirect back to the list page
