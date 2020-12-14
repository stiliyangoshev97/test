import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'users_project.settings')

import django
django.setup()

#Create faker
import random
from users_app.models import Users


#Fake generator variable
from faker import Faker
fakegen = Faker()

def populate(N = 5):
	for entry in range (N):
		fake_name = fakegen.name().split()
		fake_firstName = fake_name[0]
		fake_lastName = fake_name[1]
		fake_email = fakegen.email()

		#Crate new entry
		user = Users.objects.get_or_create(firstName = fake_firstName, lastName = fake_lastName, email = fake_email)[0]


if __name__ == '__main__':
	print('Running population script..')
	populate(20)
	print('Population has ended')

