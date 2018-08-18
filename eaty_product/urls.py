from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns

# from django.conf.urls import url

# from rest_framework.routers import DefaultRouter
# from eaty_product.views import ProductViewSet, ProductTypeViewSet
from . import views
from .views import list_products, create_product, update_product, delete_product

urlpatterns = [
    # CRUD - ProductType API
    path('', list_products, name='list_products'),
    path('new', create_product, name='create_product'),
    path('update/<int:id>/', update_product, name='update_product'),
    path('delete/<int:id>/', delete_product, name='delete_product'),

    # REST API ProductType
    path('producttypes/', views.ProductTypeList.as_view()),
    # path('producttypes/<int:pk>/', views.ProductTypeDetail.as_view()),
    path('producttypes/<int:pk>/', views.ProductTypeDetail.as_view()),

]

# urlpatterns = format_suffix_patterns(urlpatterns)

"""
urlpatterns = [
    path('', views.list_product, name='list_product'),
]
"""
# urlpatterns = [
# ]


# router = DefaultRouter()
# router.register(prefix='product', viewset=ProductViewSet)
# router.register(prefix='producttype', viewset=ProductTypeViewSet)

# urlpatterns = router.urls
