from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('login/', views.user_login, name='login'),

    # 该视图返回了一个next参数，用于登录成功之后的跳转
    path('login/', auth_views.LoginView.as_view(), name='login'),  # 尾部是什么再按一次可以跳出
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),

    path('password_change/',
         auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done',
         auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
]
