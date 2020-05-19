# Scrappix - an open source GUI-based web scraper
This repo constains the source-code for the final submission of Applied Technology Group Project for the 3rd year of Information Technology.

This Python application will help the user to scrape data from a website (for now only the hardcoded ecommerces) and export the extracted data to a database table hosted at [SQLite](https://sqliteonline.com/).

## 
 
 # Running from GitHub repo
 > To run this app from here using CLI:
 1. Download or clone the repo using
 `git clone https://github.com/laisbsc/Scrappix.git` on your local machine
 2. At the root folder **activate your virtual environment** (conda, venv, whatever you use to run python apps) and run `pip install -r requirements.txt` to locally install all the dependencies required for the project to run.
 3. Go to the second level scrapix folder (the one on the same level as the scrapy.cfg file) and run `scrapy crawl scrappix_amazon` on your terminal to execute one crawler. > how do I execute them all?? 
