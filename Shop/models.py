from django.db import models
from django.contrib.auth.models import User

class Material(models.Model):
    price = models.IntegerField(blank = False)
    material = models.CharField(blank = False, max_length=20)
    massa = models.FloatField(blank = False)

    def __str__(self):
        return self.material

class Size(models.Model):
    price = models.FloatField(blank = False)
    title = models.CharField(blank = False, max_length=3)
    massa = models.FloatField(blank = False)

    def __str__(self):
        return self.title

class Color(models.Model):
    price = models.IntegerField(blank=False)
    title = models.CharField(blank=False, max_length=20)

    def __str__(self):
        return self.title

class Kuntic(models.Model):
    title = models.CharField(blank=False, max_length=20)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    custom = models.BooleanField(default=False)
    extra = models.TextField(blank=True)
    extra_price = models.IntegerField(default=0)

    def price(self):
        return self.material.price * self.size.price + self.extra_price

    def get_mass(self):
        return self.material.massa * self.size.massa

    def __str__(self):
        return 'номер: ' + str(self.id) + ', ' + str(self.price()) + ' пыли.'

class Order(models.Model):
    kuntic = models.ForeignKey(Kuntic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=20, blank=False)

    def __str__(self):
        if self.kuntic.get_mass() > 150:
            return self.state + 'отправка тележкой' + self.kuntic
        else:
            return self.state + 'отправка воздушным шаром' + self.kuntic