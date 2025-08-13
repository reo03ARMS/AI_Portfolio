from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.helpers import complete_social_login
from django.views.decorators.csrf import csrf_exempt

# index はログイン必須


@login_required
def index(request):
    return render(request, 'web/index.html')

# ログインページ


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')  # 既にログインしていれば index にリダイレクト
    return render(request, 'web/login.html')

# ログアウト処理


def logout_view(request):
    logout(request)
    return redirect('login')
