from django.urls import path
from . import views
from .views import list_users, create_user, update_user, delete_user, list_groups, create_group, update_group, delete_group, list_sessions, create_session, update_session, delete_session

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

    # CRUD - Session API
    path('session', list_sessions, name='list_sessions'),
    path('newsession', create_session, name='create_session'),
    path('updatesession/<int:id>/', update_session, name='update_session'),
    path('deletesession/<int:id>/', delete_session, name='delete_session'),


    # REST API User
    path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    # REST API Group
    path('groups/', views.GroupList.as_view()),
    # path('groups/<int:pk>/', views.GroupDetail.as_view()),
    path('groups/<int:pk>/', views.GroupDetail.as_view()),
    
    # REST API Session
    path('sessions/', views.SessionList.as_view()),
    # path('sessions/<int:pk>/', views.SessionDetail.as_view()),
    path('sessions/<int:pk>/', views.SessionDetail.as_view()),

]


# router = DefaultRouter()
# router.register(prefix='group', viewset=GroupViewSet)
# router.register(prefix='user', viewset=UserViewSet)

# urlpatterns = router.urls
