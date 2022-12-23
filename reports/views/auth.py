from django.contrib.auth.views import LoginView as BaseLoginView


class LoginView(BaseLoginView):
    template_name = "auth.html"
    redirect_authenticated_user = True


login = LoginView.as_view()
