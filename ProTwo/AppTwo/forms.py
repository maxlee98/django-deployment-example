from django import forms
from django.core import validators
from AppTwo.models import User


#--MODEL SOLUTION--

class NewUserForm(forms.ModelForm):
    #ADD ANY VALIDATOR HERE
    # first_name = form.CharField(validator=)
    class Meta():
        model = User
        fields = '__all__'











#--ORIGINAL SOLUTION--
# class UserForm(forms.Form):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     user_email = forms.EmailField()
#     user_vemail = forms.EmailField(label='Enter Your Email Again: ')



#     def clean(self):
#         all_clean_data = super().clean()
#         user_email = all_clean_data['user_email']
#         user_vemail = all_clean_data['user_vemail']

#         if user_email != user_vemail:
#             raise forms.ValidationError("Please make sure your emails match.")