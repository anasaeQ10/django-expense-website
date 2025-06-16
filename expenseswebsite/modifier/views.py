# views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/authentication/login')
def profile(request):
    user = request.user  # Récupère l'utilisateur actuellement connecté
    context = {
        'user': user
    }
    return render(request, 'profile/user_info.html', context)