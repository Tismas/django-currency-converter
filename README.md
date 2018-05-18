# django-currency-converter
Scraping data from ecb and exposing it in REST api

## How to
Create virtualenv and activate it. Then run:  


> _pip install -r requirements.txt_  


To populate/update database go to scrapers/rss and run:  


> _scrapy crawl central_bank_  


To run application go to app catalog and run:  


> _python manage.py runserver_  
