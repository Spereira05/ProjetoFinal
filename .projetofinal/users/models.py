from django.contrib.auth.models import AbstractUser
from django.db import models
import bcrypt

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  

    def set_password(self, raw_password):
        self.password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())
        self._password = raw_password

    def check_password(self, raw_password):
        return bcrypt.checkpw(raw_password.encode('utf-8'), self.password.encode('utf-8'))
    
   
owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
