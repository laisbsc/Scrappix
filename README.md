# Scrappix - an open source GUI-based web scraper
This repo constains the source-code for the final submission of Applied Technology Group Project for the 3rd year of Information Technology.

## What is Scrappix?
Scrappix is a python application designed to help users to scrape data from websites (for now only the hardcoded ecommerces) and export the extracted data to a database table hosted at [SQLite](https://sqliteonline.com/). The initial goal was to have an interactive GUI which would be deployed using Heroku and used for input of search term and the URL of the crawled website. The app would search for the keyterm on the input box (string) and fetch the following matching items on HTML:
 - item name;
 - price;
 - available stock;
 - product image.
 Those items would then be placed into a database.db file (matching the schema specified at the `db.py`). Where they could be queried and had graphs plotted from the data.

## Requirements:
 - Scrapy needs min. Python 3.5.1+ to run.
 I am using Python 3.8.2, Scrapy 2.1.0 deployed locally on a Windows 10 (version 18363) machine using PyCharm Community Ed. 2020.1.
 
 # Running Scrappix
 ## From GitHub repo:
 > To run this app from here using CLI:
 1. Download or clone the repo using
 `git clone https://github.com/laisbsc/Scrappix.git` on your local machine
 2. At the root folder **activate your virtual environment** (conda, venv, whatever you use to run python apps) and run `pip install -r requirements.txt` to locally install all the dependencies required for the project to run.
 3. Go to the second level scrapix folder (the one on the same level as the scrapy.cfg file) and run `scrapy crawl crawler_name` on your terminal to execute the desired crawler.
 4. The output from running the command should have been placed into a file with a `.db` extension to it.
 5. To analyse the output (and query it) go to [SQLite](https://sqliteonline.com/).
 6. On the top left-hand side click 'File' and load the file created upon last command's execution.
 You should be seeing all your scraped data on the screen now.
 
 ### To execute queries
 Type your query in the textbox at the top of the page and click 'run'.
