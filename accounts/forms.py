from django.contrib.auth import get_user_model  #return the user models
from django.contrib.auth.forms import UserCreationForm  #already have user form from the import



class UserCreateForm(UserCreationForm):
    
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
        self.fields['password1'].label = 'Enter Password'
        self.fields['password2'].label = 'Confirm Password'

