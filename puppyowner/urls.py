from django.urls import path
from . import views

urlpatterns = [
   path('update/<str:pk>/', views.puppy_update, name='update'),
   path('puppy_post/', views.puppy_post, name="puppy_post"),
   path('all-pups/', views.all_pups, name='all_pups'),
   path('puppy_delete/<str:pk>/', views.puppy_delete, name='puppy_delete'),
   path('all-pups/<str:pk>/', views.puppy_detial, name='puppy_detial'),
   path('emdee_contact_post/', views.emdeecontact, name="emdee_contact_post"),
   path('emdee_blog_post/', views.emdee_blog, name="emdee_blog_post"),
   path('emdee_friend_mail_post/', views.puppy_post, name="emdee_friend_mail_post"),
]
