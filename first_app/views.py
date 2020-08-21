from django.shortcuts import render
from first_app.models import Webpage, Topic, AccessRecord, User
# from django.contrib.auth.models import User
from first_app.forms import UserProfileForm, UserForm

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list, 'text':'hello world', 'number':100}
    return render(request, 'first_app/index.html', context=date_dict)
def UserIndex(request):
    users_list = User.objects.order_by('first_name')
    users_dict = {'users':users_list}
    return render(request, 'first_app/users.html', context=users_dict)
# def user_form_view(request):
    form = forms.UserForm()
    return render(request, 'first_app/user_form.html', {'form': form})
    # form = NewUser()
    # if request.method == 'POST':
    #     form = NewUser(request.POST)
    #
    #     if form.is_valid():
    #         form.save(commit=True)
    #         return index(request)
    #     else:
    #         print('ERROR')
    # return render(request, 'first_app/user_form.html', {'form':form})

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'first_app/registeration.html', {
        'user_form':user_form, 'profile_form':profile_form, 'registered':registered
    })