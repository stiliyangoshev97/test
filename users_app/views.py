from django.shortcuts import render
from users_app.models import Users

# Create your views here.

def index(request):
	return render(request, 'users_app/index.html')


def users(request):
	users_list = Users.objects.order_by('firstName')
	users_dict = {'users': users_list}
	return render(request, 'users_app/users.html', context = users_dict)