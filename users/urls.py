from django.urls import path

from users.views import ImagesTemplateView

urlpatterns = [
    path('', ImagesTemplateView.as_view(), name='images')
]
