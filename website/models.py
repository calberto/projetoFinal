from django.db import models

<<<<<<< HEAD
class Contato(models.Model):
    nome = models.CharField(max_length=100, null=True)
    sobrenome = models.CharField(max_length=100, null=True)
    endereco = models.TextField(blank=True, null=True)
    email = models.EmailField(null=True)
    mensagem = models.TextField(blank=True, null=True)
    receber_noticias = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
=======
# Create your models here.
>>>>>>> 8aaa8fa7274a57f1c5dd7c0e8ddcdfdc4e12fc57
