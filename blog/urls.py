
from blog import views
from django.urls import path
urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('profile/', views.profile, name="profile"),
    path('signup/', views.user_signup, name="signup"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('post-add/', views.post_add, name="post_add"),
    path('post-update/<int:id>/', views.post_update, name="post_update"),
    path('post-delete/<int:id>/', views.post_delete, name="post_delete"),
]
