from django.conf.urls import url

from .views import GitHubWireRequestView

urlpatterns = [
    # url(r'^test-404/$', 'core.views.error404'),
    url(r'^github/wire-request/$', GitHubWireRequestView.as_view(), name='github-wire-request'),
]
