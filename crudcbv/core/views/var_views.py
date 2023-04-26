from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from ..models import Produto, Cliente, Fornecedor

@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = 'core/index.html'


class IndexProdutoView(ListView):
    models = Produto
    template_name = 'core/produto_lst.html'
    queryset = Produto.objects.all()
    context_object_name = 'produtos'
    paginate_by = 3
    ordering = 'id'

    def get_queryset(self):

        pesquisa = self.request.GET.get('search')

        if pesquisa:
            produtos = Produto.objects.filter(nomeProd__icontains=pesquisa)
        else:
            produtos = Produto.objects.all()
        
        return produtos


class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'core/produto_form.html'
    fields = ['nomeProd', 'preco']
    success_url = reverse_lazy('lst_produto')


class UpdateProdutoView(UpdateView):

    model = Produto
    template_name = 'core/produto_form.html'
    fields = ['nomeProd', 'preco']
    success_url = reverse_lazy('lst_produto')


class DeleteProdutoView(DeleteView):
    model = Produto
    template_name = 'core/produto_del.html'
    success_url = reverse_lazy('lst_produto')


class RelatorioProdutoView(ListView):
    models = Produto
    template_name = 'core/produto_rel.html'
    queryset = Produto.objects.all()
    context_object_name = 'produtos'
    

class IndexClienteView(ListView):
    models = Cliente
    template_name = 'core/cliente_lst.html'
    queryset = Cliente.objects.all()
    context_object_name = 'clientes'
    paginate_by = 3
    ordering = 'id'

    def get_queryset(self):

        pesquisa = self.request.GET.get('search')

        if pesquisa:
            clientes = Cliente.objects.filter(nomeClie__icontains=pesquisa)
        else:
            clientes = Cliente.objects.all()
        
        return clientes


class CreateClienteView(CreateView):
    model = Cliente
    template_name = 'core/cliente_form.html'
    fields = ['nomeClie', 'telefoneClie']
    success_url = reverse_lazy('lst_cliente')


class UpdateClienteView(UpdateView):
    model = Cliente
    template_name = 'core/cliente_form.html'
    fields = ['nomeClie', 'telefoneClie']
    success_url = reverse_lazy('lst_cliente')


class DeleteClienteView(DeleteView):
    model = Cliente
    template_name = 'cliente_del.html'
    success_url = reverse_lazy('lst_cliente')


class RelatorioClienteView(ListView):
    models = Cliente
    template_name = 'core/cliente_rel.html'
    queryset = Cliente.objects.all()
    context_object_name = 'clientes'


class IndexFornecedorView(ListView):
    models = Fornecedor
    template_name = 'core/fornecedor_lst.html'
    queryset = Fornecedor.objects.all()
    context_object_name = 'fornecedores'
    paginate_by = 3
    ordering = 'id'

    def get_queryset(self):

        pesquisa = self.request.GET.get('search')

        if pesquisa:
            fornecedores = Fornecedor.objects.filter(nomeForn__icontains=pesquisa)
        else:
            fornecedores = Fornecedor.objects.all()
        
        return fornecedores


class CreateFornecedorView(CreateView):
    model = Fornecedor
    template_name = 'core/fornecedor_form.html'
    fields = ['nomeForn', 'telefoneForn']
    success_url = reverse_lazy('lst_fornecedor')


class UpdateFornecedorView(UpdateView):
    model = Fornecedor
    template_name = 'core/fornecedor_form.html'
    fields = ['nomeForn', 'telefoneForn']
    success_url = reverse_lazy('lst_fornecedor')


class DeleteFornecedorView(DeleteView):
    model = Fornecedor
    template_name = 'core/fornecedor_del.html'
    success_url = reverse_lazy('lst_fornecedor')


class RelatorioFornecedorView(ListView):
    models = Fornecedor
    template_name = 'core/fornecedor_rel.html'
    queryset = Fornecedor.objects.all()
    context_object_name = 'fornecedores'
    