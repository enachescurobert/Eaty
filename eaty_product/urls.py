from django.urls import path
from rest_framework.routers import DefaultRouter
from eaty_product.views import ProductViewSet, ProductTypeViewSet
from . import views
"""
urlpatterns = [
    path('', views.index, name='index'),
]
"""
# urlpatterns = [
# ]


router = DefaultRouter()
router.register(prefix='product', viewset=ProductViewSet)
router.register(prefix='producttype', viewset=ProductTypeViewSet)

urlpatterns = router.urls