# -*- coding: utf-8 -*-

from django.urls import include, re_path, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

import spirit.urls

# Override admin login for security purposes
from django.contrib.auth.decorators import login_required
admin.site.login = login_required(admin.site.login)

urlpatterns = [
    re_path(r'^forum/', include(spirit.urls)),

    # This is the default django admin
    # it's not needed to use Spirit
    re_path(r'^admin/', admin.site.urls),

    re_path(r'^', include("Website.urls")),
]

if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
