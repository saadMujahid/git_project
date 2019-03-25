from django.conf.urls import url
from temp import views
# Template taging
app_name='temp'


urlpatterns=[

url(r'^relative/$',views.relative,name='relative'),

url(r'^other/$',views.other,name='other'),
]
