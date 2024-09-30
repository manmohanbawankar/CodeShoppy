"""skill URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from skillapp import views as v


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index, name="index"),
    path('about/', v.about, name="about"),
    path('contact/', v.contact, name="contact"),

#Customer Urls
    path('customer/', v.customer, name="customer"),
    path('customer_loginpage/', v.customer_loginpage, name="customer_loginpage"),
    path('regpage/', v.regpage, name="regpage"),
    path('customer_reg/', v.customer_reg, name="customer_reg"),
    path('customer_login/', v.customer_login, name="customer_login"),
    path('customer_change/', v.customer_change, name="customer_change"),
    path('display/', v.display, name="display"),
    path('edit/<str:email>', v.edit, name="edit"),
    path('update/', v.update, name="update"),
    path('delete/<str:email>', v.delete, name="delete"),
    path('logout/', v.logout, name="logout"),
    path('unknown/', v.unknown, name="unknown"),
    path('adminbro/', v.adminbro, name="adminbro"),
    path('admin_view_projects/', v.admin_view_projects, name="admin_view_projects"),

    #Admin Urls
    path('administration/', v.administration, name="administration"),
    path('admin_login/', v.admin_login, name="admin_login"),
    path('admini_change/', v.admini_change, name="admini_change"),
    path('admini_display/', v.admini_display, name="admini_display"),
    path('admini_mypurchase/', v.admini_mypurchase, name="admini_mypurchase"),
    path('addfeedback/', v.addfeedback, name="addfeedback"),
    path('viewfeedback/', v.viewfeedback, name="viewfeedback"),
    path('viewfeedback_delete/<int:id>', v.viewfeedback_delete, name="viewfeedback_delete"),
    path('admini_logout/', v.admini_logout, name="admini_logout"),
    path('sell/', v.sell, name="sell"),
    path('sellview_my/', v.sellview_my, name="sellview_my"),
    path('sell_edit/<int:id>', v.sell_edit, name="sell_edit"),
    path('sell_update/', v.sell_update, name="sell_update"),
    path('sell_delete/<int:id>', v.sell_delete, name="sell_delete"),
    path('customer_del/<int:id>', v.customer_del, name="customer_del"),
    path('sellview_all/', v.sellview_all, name="sellview_all"),
    path('sell_buy/<int:id>', v.sell_buy, name="sell_buy"),
    path('project_del/<int:id>', v.project_del, name="project_del"),
    path('sell_likes/<int:id>', v.sell_likes, name="sell_likes"),
    path('sell_dislikes/<int:id>', v.sell_dislikes, name="sell_dislikes"),
    path('my_purchase/', v.my_purchase, name="my_purchase"),
    path('comment/<int:id>', v.comment, name="comment"),
    path('view_reviews/<int:id>', v.view_reviews, name="view_reviews"),
    path('comment_del/<int:id>', v.comment_del, name="comment_del"),
    path('customer_comment_del/<int:id>', v.customer_comment_del, name="customer_comment_del"),
    path('comment_update/', v.comment_update, name="comment_update"),
    path('viewcomment/', v.viewcomment, name="viewcomment"),

]
