from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from fox.models import Fox
from django.contrib.auth import authenticate

class RegistrationForm(ModelForm):
"""
Form that takes multiple inputs for a Fox
object and a User object.
"""
    username = forms.CharField(label=(u'User Name'))
    email = forms.EmailField(label=(u'Email Address'))
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    password1 = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))

    class Meta:
    """
    Class that allows the form to use
    the Fox object model as a guideline.
    """
        model = Fox
        exclude = ('user',)

    def clean_ip(self):
    """
    Method that cleans the ip, also checks to make
    sure the IP is not already taken.
    """
        ip = self.cleaned_data['ip']
        try:
            Fox.objects.get(ip=ip)
        except Fox.DoesNotExist:
            return ip
        raise forms.ValidationError("That ip is already taken, please select another.")
    
    def clean_username(self):
    """
    Method that cleans the username, also checks
    to make sure the username is not already taken.
    """
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("That username is already taken, please select another.")

    def clean_password1(self):
    """
    Method that cleans the passwords, also checks
    to make sure both passwords match.
    """
        password = self.cleaned_data['password']
        password1 = self.cleaned_data['password1']
        if password != password1:
            raise forms.ValidationError("The passwords did not match. Please try again.")
        return password

class LoginForm(forms.Form):
"""
Form that takes a username and password to login using
built in Django auth.
"""
    username = forms.CharField(label=(u'User Name'))
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))

    def clean_username(self):
    """
    Method that cleans the username, also checks
    to make sure the username exists in the database.
    """
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("That username does not exist in the database.")
        return username

    def clean_password(self):
    """
    Method that cleans the password, also checks
    to make sure the password is correct if the
    username is in the database.
    """
        password = self.cleaned_data['password']
        try:
            username = self.cleaned_data['username']
        except KeyError:
            pass
        else:
            fox = authenticate(username=username, password=password)
            if fox is None:
                raise forms.ValidationError("Password incorrect.")
        return password

class ChangeIPForm(ModelForm):
"""
Form that takes an IP and changes the current user's
IP to the new IP given.
"""
    class Meta:
    """
    Class that allows the form to use the
    Fox object model as a guideline.
    """
        model = Fox
        exclude = ('user',)

    def clean_ip(self):
    """
    Method that cleans the IP, and checks
    to make sure the IP is not already in the
    database.
    """
        ip = self.cleaned_data['ip']
        try:
            Fox.objects.get(ip=ip)
        except Fox.DoesNotExist:
            return ip
        raise forms.ValidationError("That ip is already taken, please select another.")

class ChangePasswordForm(forms.Form):
"""
Form that takes the current password, and the new password twice,
to change the current user's password to the new password.
"""
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    newPassword = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    verifyNewPassword = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))

    def clean_password(self):
        password = self.cleaned_data['password']
        try:
            username = self.cleaned_data['username']
        except KeyError:
            pass
        else:
            fox = authenticate(username=username, password=password)
            if fox is None:
                raise forms.ValidationError("Password incorrect.")
        return password
