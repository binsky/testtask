from django.conf.urls import patterns, include, url
# from django.contrib import admin
from views import home_method

urlpatterns = patterns('',
    url(r'^$', home_method),
    # url(r'^$', 'Layout.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
