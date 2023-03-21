from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

GENDER = ((0, "Female"), (1, "Male"), (2, "Other"))


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, unique=False)
    last_name = models.CharField(max_length=50, unique=False)
    gender = models.IntegerField(choices=GENDER, default=0)
    date_of_birth = models.DateField()
    profile_image = CloudinaryField('image', default='placeholder')
    email = models.EmailField()

    def __str__(self):
        return f'{self.user.username} Profile'
