from django.urls import path, include, re_path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('container/run/<str:requestedImage>/', views.run_services),
    path('container/list/<str:list_what>/', views.docker_list),
    path('container/remove/<str:containerName>/', views.remove_services),
    path('', views.home, name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('upload_folder/', views.upload_folder, name='upload_folder'),
    path('', include('django.contrib.auth.urls')),
    path('files/', include('db_file_storage.urls')),
    re_path(r'^delete/(.*)/$', views.delete, name='delete'),
    path('deadlocksf/', views.deadlocksetfalse, name='deadlocksf'),
    path('deadlockst/', views.deadlocksettrue, name='deadlockst')
]
