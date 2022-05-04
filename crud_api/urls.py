from itertools import product
from django.urls import path
from . import views


urlpatterns = [
	path('', views.api_overview, name="api-overview"),
    #client
    path('client/<int:pk>/', views.ClientDetail.as_view(), name='clientdetailcreate'),
    path('client/', views.ClientList.as_view(), name='clientlistcreate'),

    #product
    path('product/<int:pk>/', views.ProductDetail.as_view(), name='productdetailcreate'),
    path('product/', views.ProductList.as_view(), name='productlistcreate'),

    #bill
    path('bill/<int:pk>/', views.BillDetail.as_view(), name='billdetailcreate'),
    path('bill/', views.BillList.as_view(), name='billlistcreate'),

    #bill
    path('bill-products/<int:pk>/', views.Bills_ProductDetail.as_view(), name='bill_productdetailcreate'),
    path('bill-products/', views.Bills_ProductList.as_view(), name='bill_productlistcreate'),
    ]

    # #task
    # path('task/', views.task_overview, name="task-overview"),
	# path('task-list/', views.taskList, name="task-list"),
	# path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	# path('task-create/', views.taskCreate, name="task-create"),
	# path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	# path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
    # #client
    # path('client/', views.client_overview, name="client-overview"),
    # path('client/list/', views.client_list, name="client-list"),
	# path('client/detail/<str:pk>/', views.client_detail, name="client-detail"),
	# path('client/create/', views.client_create, name="client-create"),
	# path('client/update/<str:pk>/', views.client_update, name="client-update"),
	# path('client/delete/<str:pk>/', views.client_delete, name="client-delete"),


    #endpoints requeridos
    #registrar usuario con correo y contraseña

    #iniciar sesion json web token

    #Un endpoint que permita realizar la descarga de un archivo CSV con la lista de registros de
    #Cliente: mostrando documento, nombre completo y la cantidad facturas relacionadas.

    #Un endpoint que permita realizar el cargue de un archivo CSV con resgitros para la
    #creacion de Clientes
