import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'ProTwo.settings')


import django
django.setup()

#FAKE POP SCRIPT
import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()


def populate(n=5):
    
    for entry in range(n):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_user_email = fakegen.ascii_free_email()

        fake_user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, user_email=fake_user_email)[0]


if __name__ == "__main__":
    print("Script is processing...")
    populate(10)
    print("Population Created!")