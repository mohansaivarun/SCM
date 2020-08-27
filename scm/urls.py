from django.contrib import admin
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.sample),
    url(r'^admin', admin.site.urls),
    url(r'^addressbk', include("addressbk.urls")),
    url(r'^cscore', include("cscore.urls")),
    url(r'^docmgmt', include("docmgmt.urls")),
    url(r'^imprt', include("imprt.urls")),
    url(r'^frms', include("frms.urls")),
    url(r'^meetings', include("meetings.urls")),
    url(r'^user', include("user.urls")),
]
