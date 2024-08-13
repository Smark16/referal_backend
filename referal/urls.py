from . import views
from django.urls import path

urlpatterns = [
     path('', views.ObtainPairView.as_view()),
     path("all_users", views.AllUsers.as_view()),

    # background
     path('post_basics', views.post_basic.as_view()),

      # bussiness
    path("post_bussiness", views.post_bussiness.as_view()),

    #services
    path("post_services", views.post_services.as_view()),
    path("services", views.services.as_view()),

    #modules
    path("modules", views.Modules.as_view()),
]