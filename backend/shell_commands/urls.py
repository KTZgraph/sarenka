
from django.urls import path
from shell_commands.views import commands

urlpatterns = [
    path('get_smbiosversiob',  commands.get_smbiosversiob),
]