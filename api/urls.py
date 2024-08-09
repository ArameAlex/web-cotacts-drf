from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.ContactsViewset)

urlpatterns = [
    path('page/<int:page>/', views.getpageData),
    path('mixin/', views.ContactsListMixins.as_view()),
    path('mixin/<pk>', views.ContactsDetailMixins.as_view()),
    path('generics/', views.ContactsListGenerics.as_view()),
    path('generics/<pk>', views.ContactsDetailGenerics.as_view()),
    path('viewsets/', include(router.urls)),
    path('users/', views.UserGenericAPIView.as_view()),
]
