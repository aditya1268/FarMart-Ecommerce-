"""
URL configuration for farmart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from front_farm.views import *
from django.conf import settings

from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',front_page,name ="page_front"),    
    path('home/',front_page1,name ="page_front1"),    
    path('second_page/',register_page,name ="second_front"),    
    path('register_user/',register_user,name ="register1_user"),    
    path('login_user/',login_user,name ="login_user1"),    
    path('show_veges/<store_username>/',show_veges,name ="show_veges_user"),    
    path('user_dashboard/<username>/',user_dashboard,name ="user_dashboard"),    
    path('show_user/',user_show1,name ="show_all_user"),    
    path('show_fruit/',fruit_show,name ="fruit_show1"),    
    path('show_vegestables/',vegetables_show,name ="fruit_show1"),    
    path('show_homeproduct/',homeproduct_show,name ="homeproduct1"),    
    path('login/',login_store,name ="login_store_"),    
    path('cart/',addtocart,name ="add_cart"),    
    path('show_user_veges/',user_veges_show,name ="user_show_veges"),    
        
    path('update_vege/<id>/',update_vege,name="update_vege"),
    path('delete_vege/<id>/',delete_vege,name="delete_vege"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
