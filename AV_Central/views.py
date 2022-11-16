from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required


def home_page(request):
     context= {}
     return render(request, 'index.html', context )

