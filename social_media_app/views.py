from django.shortcuts import render,redirect
from social_media_app.forms import Social_media_user_register_form,User_register_form

# Create your views here.


def home(request):
    return render(request, "home.html")

def dash(request):
    return render(request, 'dash.html')

def user_register(request):
    user_register_form_object = User_register_form()
    social_media_user_register_form_object = Social_media_user_register_form()
    if request.method == 'POST':
        user_register_form_object = User_register_form(request.POST)
        social_media_user_register_form_object = Social_media_user_register_form(request.POST)
        if user_register_form_object.is_valid() and social_media_user_register_form_object.is_valid():
            user_object = user_register_form_object.save()
            social_media_user_object = social_media_user_register_form_object.save(commit = False)
            social_media_user_object.user = user_object
            social_media_user_register_form_object.save()
            return redirect('/')
            
    return render(request, 'user_register.html', {'social_media_user_register_form_object':social_media_user_register_form_object, 'user_register_form_object':user_register_form_object})