from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from rest_framework import generics
from eaty_purchase.serializers import UserSerializer, GroupSerializer, SessionSerializer
from eaty_purchase.forms import UserForm, GroupForm, SessionForm
from .models import Session

# Rest API
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class SessionList(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class SessionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


# User API
def list_users(request):
    users = User.objects.all()
    return render(request,"app/pages/Django-User-API/user-template.html", {'users':users})

def create_user(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_users')

    return render(request,'app/pages/Django-User-API/users-form.template.html', {'form':form})

def update_user(request, id):
    user = User.objects.get(id=id)
    form = UserForm(request.POST or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect('list_users')

    return render(request, 'app/pages/Django-User-API/users-form.template.html', {'form':form, 'user':user})

def delete_user(request, id):
    user = User.objects.get(id=id)

    if request.method == 'POST':
        user.delete()
        return redirect('list_users')

    return render(request, 'app/pages/Django-User-API/user-delete-confirm.template.html')


# Group API
def list_groups(request):
    groups = Group.objects.all()
    return render(request,"app/pages/Django-Group-API/group-template.html", {'groups':groups})

def create_group(request):
    form = GroupForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_groups')

    return render(request,'app/pages/Django-Group-API/groups-form.template.html', {'form':form})

def update_group(request, id):
    group = Group.objects.get(id=id)
    form = GroupForm(request.POST or None, instance=group)

    if form.is_valid():
        form.save()
        return redirect('list_groups')

    return render(request, 'app/pages/Django-Group-API/groups-form.template.html', {'form':form, 'group':group})

def delete_group(request, id):
    group = Group.objects.get(id=id)

    if request.method == 'POST':
        group.delete()
        return redirect('list_groups')

    return render(request, 'app/pages/Django-Group-API/group-delete-confirm.template.html')


# Session API
def list_sessions(request):
    sessions = Session.objects.all()
    return render(request,"app/pages/Django-Session-API/session-template.html", {'sessions':sessions})

def create_session(request):
    form = SessionForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_sessions')

    return render(request,'app/pages/Django-Session-API/sessions-form.template.html', {'form':form})

def update_session(request, id):
    session = Session.objects.get(id=id)
    form = SessionForm(request.POST or None, instance=session)

    if form.is_valid():
        form.save()
        return redirect('list_sessions')

    return render(request, 'app/pages/Django-Session-API/sessions-form.template.html', {'form':form, 'session':session})

def delete_session(request, id):
    session = Session.objects.get(id=id)

    if request.method == 'POST':
        session.delete()
        return redirect('list_sessions')

    return render(request, 'app/pages/Django-Session-API/session-delete-confirm.template.html')

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'bunny': 'bad bunny baby baby',
        'user': UserSerializer(user, context={'request': request}).data

    }