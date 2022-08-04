import os
from celery import Celery
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wine_shop.settings') #set the DJANGO_SETTINGS_MODULE variable for the Celery command-line program.
app = Celery('wine_shop') #create an instance of the application with app = Celery('myshop').
app.config_from_object('django.conf:settings', namespace='CELERY') #     You load any custom configuration from your project settings using the config_from_object() method. The namespace attribute specifies the prefix that Celery-related settings will have in your settings.py file. By setting the CELERY namespace, all Celery settings need to include the CELERY_ prefix in their name (for example, CELERY_BROKER_URL).
app.autodiscover_tasks() # tells celery to auto-discover asynchronous tasks for your applications. Celery will look for a tasks.py file in each application directory of applications added to INSTALLED_APPS in order to load asynchronous tasks defined in it.
