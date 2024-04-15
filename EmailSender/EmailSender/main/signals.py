from django.db.models.signals import save, post_delete
from django.dispatch import reciever

from django.contrib.auth.models import User
from .models import Profile

