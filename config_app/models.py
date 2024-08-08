from django.db import models

class Mexmonxona(models.Model):
    name = models.CharField(max_length=100)
    yulduzlar_soni = models.IntegerField()
    narxi = models.IntegerField()


    def __str__(self):
        return self.name
    

class Transport(models.Model):
    name = models.CharField(max_length=100)
    narxi = models.IntegerField()

    def __str__(self):
        return self.name
    

class Travel(models.Model):
    country_name = models.CharField(max_length=100)
    haqida = models.TextField()
    muddati = models.IntegerField()
    narxi = models.IntegerField()
    mexmonxona = models.ForeignKey(Mexmonxona, on_delete=models.CASCADE, related_name='mexmonxona')
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE, related_name='transport')

    def __str__(self):
        return self.country_name
