from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from myapp.forms import UserForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'myapp/index.html')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            verification_code = form.cleaned_data.get('verification_code')
            if verification_code == "0000":
                # 사용자 인증
                user = form.save()  # 사용자 생성
                login(request, user)  # 로그인
                return redirect('login')
            else:
                form.add_error('verification_code', '올바른 인증 코드를 입력하세요.')
    else:
        form = UserForm()
    return render(request, 'myapp/signup.html', {'form': form})



@login_required
def map(request):
    return render(request, 'myapp/map.html')