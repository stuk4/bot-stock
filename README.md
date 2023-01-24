# Bot Stock

This is a bot created to check stock of a product.

## Built With
- [Django](https://www.djangoproject.com/) - A high-level Python web framework
- [Celery](https://docs.celeryproject.org/) - An asynchronous task queue/job queue based on distributed message passing
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) - A library for parsing and navigating HTML and XML documents
- [sqlparse](https://pypi.org/project/sqlparse/) - A non-validating SQL parser for Python
- [prompt-toolkit](https://pypi.org/project/prompt-toolkit/) - A library for building powerful interactive command line and terminal applications
- [kombu](https://pypi.org/project/kombu/) - A messaging library for Python
- [django-cron](https://pypi.org/project/django-cron/) - A simple Django app to run cron jobs
- [billiard](https://pypi.org/project/billiard/) - A fork of the Python multiprocessing package
- [amqp](https://pypi.org/project/amqp/) - Low-level AMQP client for Python

## Requirements
This project requires the following Python packages:
- amqp==5.0.6
- asgiref==3.3.4
- beautifulsoup4==4.9.3
- billiard==3.6.4.0
- cached-property==1.5.2
- celery==5.1.0
- click==7.1.2
- click-didyoumean==0.0.3
- click-plugins==1.1.1
- click-repl==0.2.0
- Django==3.2.4
- django-common-helpers==0.9.2
- django-cron==0.5.1
- importlib-metadata==4.5.0
- kombu==5.1.0
- prompt-toolkit==3.0.18
- pytz==2021.1
- six==1.16.0
- soupsieve==2.2.1
- sqlparse==0.4.1
- typing-extensions==3.10.0.0
- vine==5.0.0
- wcwidth==0.2.5
- zipp==3.4.1

## Getting Started

To run this project locally, clone the repository and install the requirements:

```bash
git clone https://github.com/stuk4/bot-stock.git
cd bot_stock
pip install -r requirements.txt
```
Then, you can run the server:
```bash
python manage.py runserver
```
