from django.urls import path
from polls import views

urlpatterns = [
    path('login/', views.loginPage, name='loginpage'), ### login page
    path('logout/', views.logoutPage, name='logoutpage'), #### logout page
    path('register/', views.registerpage, name='registerpage'), ### register page
    path('profile/', views.profile, name='profilepage'), ### profile page
    path('changeprof/', views.changeprof, name='prochangepage'), ### profilechangepage
    path('changepass/',views.changepass, name='changepasspage'), ## changpass page
    
    path('', views.home, name='indexpage'), #### home page
    path('table/', views.table, name='tablepage'), ### tablepage
    path('all_table/', views.all_show, name='allshowpage'), ### all show
    path('per_views/', views.per_views, name='perviwspage'), ### table per views
    path('create/', views.create, name='createpage'), ## table createpage
    path('basic/', views.basic, name = 'basicpage'),
    
    path('armyphoto/', views.army_pho, name = 'armyphotopage'), #### aramy photo page
    path('createyear/', views.crtyear, name='crtyearpage'), #### createyearpage
    path('edityear/<str:pk>/', views.edityear, name="edityearpage"), ### edityear page
    path("delyear/<str:pk>/", views.delyear, name='deleteyearpage'), ### delete year
    
    path('createphoto', views.crephoto, name="crephotopage"), ### photo create page
    path('editphoto', views.edit_photo, name="editphotopage"), ### photo create page
    path('view photo/<str:pk>/', views.photo_view, name='viewpage'), ### arakan photo views page
    
]