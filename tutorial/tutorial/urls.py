from django.conf.urls import patterns, include, url
from django.contrib import admin
import views
from twitter import views as model_views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',views.home),
    url(r'^hello/',views.hello),
    url(r'^user/',model_views.makeuser),
    url(r'^admin/', include(admin.site.urls)),
)
