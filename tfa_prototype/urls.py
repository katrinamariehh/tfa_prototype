from django.conf.urls import patterns, include, url
from django.contrib import admin
from books.views import BookList, AuthorList

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tfa_prototype.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('two_factor.urls', 'two_factor')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^books/', BookList.as_view()),
    url(r'^authors/', AuthorList.as_view()),
)
