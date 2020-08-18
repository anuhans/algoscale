from django.urls import path, include,re_path
from .views import Login,Signup,Profile,DeleteUser,Logout

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('profile', Profile.as_view(), name='profile'),
    path('signup', Signup.as_view(), name='signup'),
    path('deleteuser', DeleteUser.as_view(), name='deleteuser'),
    re_path(r'^logout/$', Logout.as_view(),name='logout'),
]
app_name = "base"