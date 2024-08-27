from django.urls import path
from django.conf.urls.static import static
from . import views
from .views import login
# from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login, name='login'),

    path('list_account/', views.list_account, name='list_account'),

    path('create_account/', views.create_account, name='create_account'),

    path('delete_account/<int:id>/', views.delete_account, name='delete_account'),

    path('update_account/<int:id>/', views.update_account, name='update_account'),

    path('account_detail/<int:id>/', views.account_detail, name='account_detail'),

    # path('register/',views.create_account, name='create_account'),

]
