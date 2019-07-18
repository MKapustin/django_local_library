from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User

class RegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = "/accounts/login/"
    template_name = "registration\\register.html"

    def form_valid(self, form):
        form.save()
        my_group = Group.objects.get(name='Library Members') 
        my_group.user_set.add(User.objects.filter(username__exact = form.cleaned_data.get('username')).first())

        return super(RegisterFormView, self).form_valid(form)