from django.contrib.auth.forms import UserCreationForm

from online_shop_app.froms import StyledFormMixin
from users.models import User


class UserRegisterForm(StyledFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
