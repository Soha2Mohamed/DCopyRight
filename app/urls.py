from django.contrib import admin
from django.urls import include, path 
from app.Views import user,post

urlpatterns = [
    #User views
    path('user/create/', user.CreateUser.as_view()), 
    path('user/login/', user.LoginUserView.as_view()),  
    path('user/<int:pk>/', user.RetrieveUser.as_view()),
    path('user/update/', user.UpdateUser.as_view()),
    path('user/delete/<int:pk>', user.DestroyUser.as_view()),

    #Post views
    path('post/create/', post.CreatePost.as_view()),
    path('posts/', post.RetrievePost.as_view()),
]
