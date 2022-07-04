from django.db import models

class Reja(models.Model):
    nom=models.CharField(max_length=80)
    malumot=models.TextField()
    vaqt=models.DateTimeField()
    status=models.BooleanField()
    def __str__(self):
        return self.nom
