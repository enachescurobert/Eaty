from django.urls import path,re_path
# from rest_framework.urlpatterns import format_suffix_patterns

# from django.conf.urls import url

# from rest_framework.routers import DefaultRouter
# from eaty_product.views import ProductViewSet, ProductTypeViewSet
from . import views

urlpatterns = [
    re_path(r'^producttypes/$', views.ProductTypeList.as_view()),
    re_path(r'^producttypes/(?P<pk>[0-9]+)/$', views.ProductTypeDetail.as_view()),
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