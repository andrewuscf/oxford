from job.models import JobApplication, Worker, Place
from django import forms
from django.contrib.auth.forms import UserCreationForm


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=False)

    class Meta:
        model = Worker
        fields = ("username", "first_name", "last_name", "email", "password1", "password2", "phone")

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            Worker.objects.get(username=username)
        except Worker.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )


class JobApplicationForm(forms.ModelForm):
    """
    A form for JobApplication model
    """
    class Meta:
        model = JobApplication


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        exclude = ('latitude', 'longitude')