from django.urls import path
from . import views

urlpatterns = [
    path('', views.index1, name='Home1'),
    path('ecom/index2/', views.index2, name='Home2'),
    path('ecom/about/', views.about, name='AboutUs'),
    path('ecom/about1/', views.about1, name='AboutUs1'),
    path('ecom/contact1/', views.contact1, name='ContactUs1'),
    path('ecom/contact/', views.contact, name='ContactUs'),
    path('ecom/tracker/', views.tracker, name='TrackingStatus'),
    path('ecom/productview/<int:myid>/<slug:mycategory>', views.productview, name='ProductView'),
    path('ecom/productview1/<int:myid>/<slug:mycategory>', views.productview1, name='ProductView'),
    path('ecom/search1/', views.search1, name='Search1'),
    path('ecom/search2/', views.search2, name='Search2'),
    path('ecom/checkout/', views.checkout, name='Checkout'),
    path('ecom/cart/', views.cart, name='Cart'),
    path('ecom/emptycart/', views.emptycart, name='EmptyCart'),
    path('ecom/addtocart/', views.addtocart, name='AddToCart'),
    path('ecom/signup/', views.signup, name='signup'),
    path('ecom/login/', views.login, name='login'),
    path('ecom/logout/', views.logout, name='logout'),
]