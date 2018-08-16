from django.urls import path,re_path
# from rest_framework.urlpatterns import format_suffix_patterns

# from django.conf.urls import url

# from rest_framework.routers import DefaultRouter
# from eaty_product.views import ProductViewSet, ProductTypeViewSet
from . import views

urlpatterns = [
    path('producttypes/', views.ProductTypeList.as_view()),
    path('producttypes/<int:pk>/', views.ProductTypeDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

"""
urlpatterns = [
    path('', views.index, name='index'),
]
"""
# urlpatterns = [
# ]


# router = DefaultRouter()
# router.register(prefix='product', viewset=ProductViewSet)
# router.register(prefix='producttype', viewset=ProductTypeViewSet)

# urlpatterns = router.urls