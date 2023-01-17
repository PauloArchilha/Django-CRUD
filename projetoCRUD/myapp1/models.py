from django.db import models

# Create your models here.


class User(models.Model):
    nome = models.CharField('nome', max_length=50)
    telefone = models.BigIntegerField('telefone')
    email = models.EmailField()

    def __str__(self):
        return f'Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}'
