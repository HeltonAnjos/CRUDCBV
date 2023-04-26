from core.views import var_views
from django.urls import path
from core.views.login import LoginView
from core.views.logout import logout_view


urlpatterns = [
    path('', var_views.HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('lst/produto', var_views.IndexProdutoView.as_view(), name='lst_produto'),
    path('add/produto', var_views.CreateProdutoView.as_view(), name='add_produto'),
    path('<int:pk>/updatep/', var_views.UpdateProdutoView.as_view(), name='upd_produto'),
    path('<int:pk>/deletep/', var_views.DeleteProdutoView.as_view(), name='del_produto'),
    path('rel/produto/', var_views.RelatorioProdutoView.as_view(), name='rel_produto'),
    path('lst/cliente', var_views.IndexClienteView.as_view(), name='lst_cliente'),
    path('add/cliente', var_views.CreateClienteView.as_view(), name='add_cliente'),
    path('<int:pk>/updatec/', var_views.UpdateClienteView.as_view(), name='upd_cliente'),
    path('<int:pk>/deletec/', var_views.DeleteClienteView.as_view(), name='del_cliente'),
    path('rel/cliente/', var_views.RelatorioClienteView.as_view(), name='rel_cliente'),
    path('lst/fornecedor', var_views.IndexFornecedorView.as_view(), name='lst_fornecedor'),
    path('add/fornecedor', var_views.CreateFornecedorView.as_view(), name='add_fornecedor'),
    path('<int:pk>/updatef/', var_views.UpdateFornecedorView.as_view(), name='upd_fornecedor'),
    path('<int:pk>/deletef/', var_views.DeleteFornecedorView.as_view(), name='del_fornecedor'),
    path('rel/fornecedor/', var_views.RelatorioFornecedorView.as_view(), name='rel_fornecedor'),
]
