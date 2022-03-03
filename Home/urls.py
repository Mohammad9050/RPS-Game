from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
app_name = 'Home'

urlpatterns = [
    # path('', views.home, name='home'),
    # path('sign_up', views.sign_up, name='sign_up'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    # path('signup', views.SignUpView.as_view(), name='signup'),
    path('signup', views.sign_up, name='signup'),
    path('password_change/', auth_view.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done', auth_view.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path('edit_user/<int:pk>', views.EditView.as_view(), name='edit_user'),
    path('edit_user/', views.edit_user, name='edit_user'),
    # path('detail_user/<int:pk>', views.DetailUser.as_view(), name='detail_user')
    ]
