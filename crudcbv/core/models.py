from django.db import models

from django.core.exceptions import ValidationError


def validate_telefone(value):
    if not value.isdigit():
        raise ValidationError('O telefone deve conter apenas números. o código de área seguido dos 9 números do telefone de contato!')


class Produto(models.Model):
    nomeProd = models.CharField(max_length=100, verbose_name='Nome')
    preco = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Preço')

    def __str__(self):
        return self.nomeProd

class Fornecedor(models.Model):
    nomeForn = models.CharField(max_length=100, verbose_name='Nome')
    telefoneForn = models.CharField(max_length=11, verbose_name='Telefone', validators=[validate_telefone])

    def __str__(self):
        return self.nomeForn

    class Meta:
        verbose_name_plural = 'Fornecedores'


class Cliente(models.Model):
    nomeClie = models.CharField(max_length=100, verbose_name='Nome')
    telefoneClie = models.CharField(max_length=11,verbose_name='Telefone', validators=[validate_telefone])

    def __str__(self):
        return self.nomeClie