from django.urls import path
from . import views
from .views import list_producttypes, create_producttype, update_producttype, delete_producttype, list_products, create_product, update_product, delete_product

urlpatterns = [
    # CRUD - ProductType API
    path('type', list_producttypes, name='list_producttypes'),
    path('new', create_producttype, name='create_producttype'),
    path('update/<int:id>/', update_producttype, name='update_producttype'),
    path('delete/<int:id>/', delete_producttype, name='delete_producttype'),
     # CRUD - Product API
    path('product', list_products, name='list_products'),
    path('newproduct', create_product, name='create_product'),
    path('updateproduct/<int:id>/', update_product, name='update_product'),
    path('deleteproduct/<int:id>/', delete_product, name='delete_product'),


    # REST API ProductType
    path('types/', views.ProductTypeList.as_view()),
    # path('producttypes/<int:pk>/', views.ProductTypeDetail.as_view()),
    path('types/<int:pk>/', views.ProductTypeDetail.as_view()),

    # REST API Product
    path('products/', views.ProductList.as_view()),
    # path('products/<int:pk>/', views.ProductDetail.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),

]


# router = DefaultRouter()
# router.register(prefix='product', viewset=ProductViewSet)
# router.register(prefix='producttype', viewset=ProductTypeViewSet)

# urlpatterns = router.urls
