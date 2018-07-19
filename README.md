# Portfolio Project

This is a portfolio project written in Python using Django2 as part of [this](https://www.udemy.com/the-ultimate-beginners-guide-to-django-django-2-python-web-dev-website/learn/v4/overview) web development course. 

I have added functionality to it to let me display details of an individul project. I have also removed the URL pattern giving access to the Blog functionality as I don't usually take the time to type out my thoughts on a keyboard (and I'm not sure anyone wants to be subject to them). Someday I might add it back.

Cloning this repository and then running this webstite from your local host is as simple as:
(assuming you have a postgresSQL db with the correct name installed)
* Install virtualenv using pip
* Navigate to the cloned project's folder
* run `venv name_of_virtual_enviroment` from your command line
* run `source name_of_virtual_enviroment\Scripts\activate`
* run `pip install -r requirments.txt`
* run `python manage.py makemigrations`
* run `python manage.py migrate`
* run `python manage.py collectstatic`
* run `python manage.py runserver`

