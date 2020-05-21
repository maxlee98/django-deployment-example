from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.forms import NewUserForm

# Create your views here.

def index(request):
    return render(request, 'AppTwo/index.html')



def help_site(request):
    help_page = {'help_page':"This is a help page"}
    return render(request, 'AppTwo/help.html', context=help_page)

def user_page(request):
    
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid:
            form.save(commit=True) #This line saves the form
            return index(request) #This brings you back to the homepage
        else:
            print("ERROR FORM INVALID")

    return render(request, 'AppTwo/registration.html', {'form':form} )


    # DJANGO LEVEL2
    # user_list = User.objects.order_by("first_name")
    # user_dict = {'user_records': user_list}
    # return render(request, 'AppTwo/user.html', context=user_dict)





#ORIGINAL SOLUTION FOR DJANGO LEVEL3
# def registration(request):
#     form = forms.UserForm()

#     if request.method == "POST":
#         form = forms.UserForm(request.POST)

#         if form.is_valid():
#             print("FORM IS VALIDATED.")

#             new_user = User.objects.get_or_create(first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], user_email=form.cleaned_data['user_email'])[0]

#             print("User is created.")
#             print("User FirstName: " + form.cleaned_data['first_name'])
#             print("User LastName: " + form.cleaned_data['last_name'])
#             print("User Email: " + form.cleaned_data['user_email'])



#     return render(request, 'AppTwo/registration.html', {'form':form})
