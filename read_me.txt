""""
Intro Django:

Ferramenta essencial para backend
terminal cmd:
pip install django  # instala django
django-admin startproject projeto_django .   # cria projeto


Apps Django:
parts of the website, every section is an app
every new section: register into settings/Installed_Apps
urls: set url that refers to the apps(section)

for this project: local server (light)
terminal cmd: python manage.py runserver

will initiate server 127.0.0.1: 8000
If need to change to port ****: python manage.py runserver ****

to see our site: click url on terminal

para executar qlqr coisa: python manage.py

Process of creating new app 'name':
python manage.py startapp name
Creates a new file in the roots of the project
cria um file urls.py in this new file
in this file:
'''
from django.urls import path
from . import views

urlpatterns = [
    path('LAST_URL', views.index)
]
'''

CREATE APP = Register it in settings.py and urls.py of main project, igual other

go to views.py in the new app file:
def index(request):
    return render(request, 'PATH_TO_YOUR_HTML.html')

terminal >> python manage.py runserver
go to 'LAST_URL' to see your new section

"""
