# Django (MVC)
* Model -> Database, table (ORM)
* View -> web pages view
* control -> URl
## Project Vs Application
* project parent
    * application childrens (more than one applications can include in one projects)
## Create virtual envornment
* `python -m venv <abc>`
    * Windows `.\<abc>\Scripts\activate`
    * Linux `source <abc>/bin/activate`
* Install required packages in Virtual Envornment
    * `pip install numpy pandas django`
    * install packages with **requirements.txt**
        * `pip install -r requirements.txt`
    * `pip freeze` Show all packages list in console
    * `pip freeze > requirements.txt` Save all pakcages names in **requirements.txt**
## Start working on Django Project
* `python -m django --version`
* Create new project 
    * `django-admin startproject <mysite>`
* now run your server
    * `python manage.py runserver`
        * optional if you want to see **\admin**
            * `python manage.py migrate`

* Create **polls** app
    * `python manage.py startapp <polls>`
        * **polls/urls.py** create
        ```
        from django.urls import path
        from . import views

        urlpatterns = [
            path("",views.index, name='poll_index'),
        ]
        ```
        * **polls/views.py**
        ```
        from django.shortcuts import render, HttpResponse

        def index(request):
            return HttpResponse("<h1>Polls Application Page</h1>")
        ```        
    * add **polls/urls.py** in main project **mysite/urls.py**     
        * **mysite/urls.py**
        ```
        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
            path("polls", include('polls.urls'))
            path('admin/', admin.site.urls),
        ]
        ```    