from django.db import models

# Create your models here.

class Materias(models.Model):
    nome = models.CharField(max_length=50)
    credito = models.IntegerField()
    codigo = models.CharField(max_length=15)

    class Meta:
        db_table = 'Materias'

    def __str__(self):
        return self.nome
