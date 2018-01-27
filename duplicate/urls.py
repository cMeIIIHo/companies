from django.conf.urls import url
from duplicate import views

app_name = 'duplicate'


urlpatterns = [
    url(r'^$', views.show_duplicates, name='show_duplicates'),
]
