"""
urls daughters in blog app
as refered in urls.py in projeto_django directory
"""

from django.urls import path
from . import views  # . = reference to blog directory

# /blog/  = where site ends if new reference: new end
urlpatterns = [
    path('', views.index)  # views.index happens when calling url '' = in this case previous url (blog)
]
