from django.conf.urls import url
from duplicate import views

app_name = 'duplicate'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'api/get_duplicates', views.get_duplicates, name='get_duplicates')
]
