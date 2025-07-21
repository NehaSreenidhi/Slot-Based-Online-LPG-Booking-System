# forms.py
from django import forms
from .models import Booking
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    mobile_no = forms.CharField(max_length=10)
    consumer_no = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['username', 'mobile_no', 'consumer_no', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            profile = Profile(user=user, mobile_no=self.cleaned_data['mobile_no'], consumer_no=self.cleaned_data['consumer_no'])
            profile.save()
        return user

class LoginForm(forms.Form):
    mobile_no = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)
    
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'consumer_number', 'delivery_date', 'time_slot']
        
    DELIVERY_TIME_SLOTS = [
        ('1', '10:00 am - 12:00 pm'),
        ('2', '12:00 pm - 2:00 pm'),
        ('3', '2:00 pm - 4:00 pm'),
        ('4', '4:00 pm - 6:00 pm'),
    ]
    delivery_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time_slot = forms.ChoiceField(choices=DELIVERY_TIME_SLOTS)

