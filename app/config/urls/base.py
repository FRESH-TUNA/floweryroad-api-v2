from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('app/admin/', admin.site.urls),
    path('app/', include('app.urls'))
]
