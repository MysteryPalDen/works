from django.db import models
from datetime import datetime

# Create your models here.

class Emergencies(models.Model):
    em_name = models.CharField(max_length = 45)
    def __str__(self):
        return self.id
    def get_em_name(self):
        return self.em_name

class Users(models.Model):
    login = models.CharField(max_length = 45)
    usrpswd = models.CharField(max_length = 45)
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    login_str = models.CharField(max_length = 45)
    phone = models.CharField(max_length = 11)
    tg_id = models.CharField(max_length = 45, null = True, blank = True)
    def __str__(self):
        return self.id
    def get_login(self):
        return self.login

class Controllers(models.Model):
    controller_name = models.CharField(max_length = 45)
    special_key = models.CharField(max_length = 45)
    def __str__(self):
        return self.id
    def get_controller_name(self):
        return self.controller_name
    def get_special_key(self):
        return self.special_key

class Controllers_Users(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    controller = models.ForeignKey(Controllers, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

class Recieve(models.Model):
    controller = models.ForeignKey(Controllers, on_delete=models.CASCADE)
    emergency = models.ForeignKey(Emergencies, on_delete=models.CASCADE)
    time_right_now = models.DateTimeField()

    def __str__(self):
        return self.id
    def get_time(self):
        return self.time_right_now
    def get_verbose_time(self):
        return str(self.time_right_now)

