# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from .models import CustomUser

# to override the default fields by setting the model to our CustomUser and using the default fields 
# via Meta.fields which includes all default fields. 
# To add our custom age field, we simply tack it on at the end, and it will display automatically on our future 
# signup page. 
class CustomUserCreationForm(UserCreationForm): 
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("age",)

class CustomUserChangeForm(UserChangeForm): 
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields