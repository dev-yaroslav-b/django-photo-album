from django import forms
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

from .models import MediaPost


class MediaPostForm(forms.ModelForm):
    class Meta:
        model = MediaPost
        fields = ('title', 'description', 'media',)


class ShareYoutubeVideoForm(forms.Form):
    link = forms.CharField(max_length=1000)


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/accounts/login/"
    template_name = "registration/signup.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)
