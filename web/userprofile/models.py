from django.db import models
from django.contrib.auth import get_user_model
# from django_countries.fields import CountryField

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='profile_set')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)
    image = models.ImageField(blank=True, default='profile/default.jpg', upload_to='profile/')

    def __str__(self):
        return "Пользователь: {} {}".format(self.user.first_name, self.user.last_name)


class Address(models.Model):
    # country = CountryField()
    region = models.CharField(max_length=255, )
    city = models.CharField(max_length=255, )
    street = models.CharField(max_length=255, )
    index = models.CharField(max_length=15, )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='address_set')
    objects = models.Manager()

    def __str__(self):
        return "{city}".format(city=self.city)
