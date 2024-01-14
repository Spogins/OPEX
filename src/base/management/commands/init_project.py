# -*- coding: utf-8 -*-
import os
import random
from datetime import datetime, timedelta

import environ
from django.contrib.auth.models import User
from django.core.files import File
from django.core.management import BaseCommand
from django.utils import timezone

from config import settings


env = environ.Env()


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
        self.create_admin()

    @staticmethod
    def create_admin():
        if env.str("ADMIN_USERNAME", default=None) and env.str("ADMIN_PASSWORD", default=None):
            user = User.objects.create_superuser(
                first_name="admin",
                last_name="admin",
                username=env.str("ADMIN_USERNAME"),
                is_superuser=True,
                is_active=True,
            )
            user.set_password(env.str("ADMIN_PASSWORD"))
            user.save()
            print("ADMIN CREATED")

