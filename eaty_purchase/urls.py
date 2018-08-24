from django.urls import path
from . import views
from .views import list_users, create_user, update_user, delete_user, list_groups, create_group, update_group, delete_group, list_purchases, create_purchase, update_purchase, delete_purchase

urlpatterns = [
    # CRUD - User API
    path('user', list_users, name='list_users'),
    path('newuser', create_user, name='create_user'),
    path('updateuser/<int:id>/', update_user, name='update_user'),
    path('deleteuser/<int:id>/', delete_user, name='delete_user'),
     # CRUD - Group API
    path('group', list_groups, name='list_groups'),
    path('newgroup', create_group, name='create_group'),
    path('updategroup/<int:id>/', update_group, name='update_group'),
    path('deletegroup/<int:id>/', delete_group, name='delete_group'),

    # CRUD - Purchase API
    path('purchase', list_purchases, name='list_purchases'),
    path('newpurchase', create_purchase, name='create_purchase'),
    path('updatepurchase/<int:id>/', update_purchase, name='update_purchase'),
    path('deletepurchase/<int:id>/', delete_purchase, name='delete_purchase'),


    # REST API User
    path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    # REST API Group
    path('groups/', views.GroupList.as_view()),
    # path('groups/<int:pk>/', views.GroupDetail.as_view()),
    path('groups/<int:pk>/', views.GroupDetail.as_view()),
    
    # REST API Purchase
    path('purchases/', views.PurchaseList.as_view()),
    # path('purchases/<int:pk>/', views.PurchaseDetail.as_view()),
    path('purchases/<int:pk>/', views.PurchaseDetail.as_view()),

]


# router = DefaultRouter()
# router.register(prefix='group', viewset=GroupViewSet)
# router.register(prefix='user', viewset=UserViewSet)

# urlpatterns = router.urls
