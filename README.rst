Rimbaud
=======

Un écrivain veut se mettre au numérique et vous demande de lui réaliser une application web pour publier ses articles sur les internets !

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style

:License: MIT

Basic Commands
--------------

1. Clone the repo
::
    git clone https://github.com/dbousfira/rimbaud.git


2. Modify a .env file at the root

3. Install requirements/local.txt with your favorite environment handler.

4. To launch app: 
:: 
    python manage.py runserver


Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.
