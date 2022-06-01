from django.urls import path, include

from apps.vulnerabilities.api import views

app_name = "vulnerabilities"

urlpatterns = [
    path("", views.hello, name="vulns"),

]
