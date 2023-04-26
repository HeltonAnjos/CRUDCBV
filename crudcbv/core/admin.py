from django.contrib import admin

from .models import Produto, Fornecedor, Cliente


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nomeProd', 'preco')


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nomeForn', 'telefoneForn')


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nomeClie', 'telefoneClie')