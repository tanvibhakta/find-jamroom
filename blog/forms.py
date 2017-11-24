"""
You probably only need this file if you are havung a form which will write to the database.

"""



from django import forms
# from .models import Owner, Jamroom, OperatingHours, Customer, Booking
#
# class HomeSearchForm(forms.ModelForm):
#
#     class Meta:
#         model = Post
#         fields = ('title', 'text',)


class HomeSearchForm(forms.Form):
   search_term = forms.CharField(max_length = 100)
