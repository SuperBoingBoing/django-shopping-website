from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home),
    path("signup", views.signup, name='signup'),
    path("signin", views.signin, name='signin'),
    path("logout", views.logout, name='logout'),
    path("snack", views.snack),
    path("addtocart", views.addtocart),
    path("phone", views.phone),
    path('movie', views.movie),
    path('cart', views.addtocart),
    path('calculator', views.calculator),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

