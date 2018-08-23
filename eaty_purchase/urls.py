from django.urls import path
from . import views
from .views import list_users, create_user, update_user, delete_user, list_groups, create_group, update_group, delete_group, list_profiles, create_profile, update_profile, delete_profile

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
    # CRUD - Profile API
    path('profile', list_profiles, name='list_profiles'),
    path('newprofile', create_profile, name='create_profile'),
    path('updateprofile/<int:id>/', update_profile, name='update_profile'),
    path('deleteprofile/<int:id>/', delete_profile, name='delete_profile'),


    # REST API User
    path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    # REST API Group
    path('groups/', views.GroupList.as_view()),
    # path('groups/<int:pk>/', views.GroupDetail.as_view()),
    path('groups/<int:pk>/', views.GroupDetail.as_view()),
    
    # REST API Profile
    path('profiles/', views.ProfileList.as_view()),
    # path('profiles/<int:pk>/', views.ProfileDetail.as_view()),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view()),

]


# router = DefaultRouter()
# router.register(prefix='group', viewset=GroupViewSet)
# router.register(prefix='user', viewset=UserViewSet)

# urlpatterns = router.urls
