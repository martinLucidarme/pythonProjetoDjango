Insert static files in a django made site
(CSS, JS, img...)

create the 'static' paste (Django will automatically look there)
go to base.html
on top : {% load static %}

then look for links to the css files you wanna get

insert href = "{% static 'path_of_css_file' %}"

in example: href="vendor/bootstrap...."
=>"{% static 'paginas/vendor/bootstrap...' %}"

CREATE LINK:
look for <li></li> in html file
change 'href=' to right urls

example:
base.html -> li => home and Sobre
<li class="nav-item active">
            <a class="nav-link" href="/">Home
              <span class="sr-only">(current)</span>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/sobre/">Sobre</a>
          </li>

You can also move static file to templates' file
then it is not only 'paginas' templates
we can reorganize file to delete pagina file
(be careful to change adresses then)
Need to tell Django in settings where to look for static files then
settings.py > STATIC_URL
Write:
STATICFILES_DIRS = [
    BASE_DIR / 'templates/static',  # path of where your statics are
]

Now Static file are working and accessible out of app folder

Now with image:
Do a {%load static%} comand in html where u want the image
in image source: < img src="{% static 'path_of_image' %}">
