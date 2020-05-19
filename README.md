The use of UserAgents to bypass scraping restrictions <br>
Every website puts restrictions on scraping practices, due to the overhead that it can bring the website's internal servers (refer back to the principles of web scraping - Law 1 is 'Do not harm the website'). <br>

There are plenty of ways in which a user is able to scrape the data bypassing the restrictions in a friendly manner. Considering that Amazon does not forbid crawlers from scraping its data, it instead requires the UserAgent (identity of the brawser looking for data) and tried to match one of the specified on its robots.txt file (https://www.amazon.co.uk/robots.txt). If a brawser tries to scrape data in a very short interval, the website refuses and can block the browser, and the way it knows it is the same actor is by the UserAgent identification. <br>
The work-around I chose to use was the implementation of a library called scrapy-user-agents that loops through a list of standard UserAgents commonly used on the web (all in a file with around 2200 user-agent's names collected from https://developers.whatismybrowser.com/ using https://github.com/hyan15/crawler-demo/tree/master/crawling-basic/common_user_agents. The library also allows for the possibility of inserting your own User-Agent by setting parameters at `RANDOM_UA_FILE` testing each one until the website allows for the data scraping. The list of 
 
 
 # Running
 > To run this app using CLI go to the top level directore (the one on the same level as the .cfg file) and run: 
 `scrapy crawl scrappix_amazon`


That will start the User-Agent matching process and scrawl the Amazon web page afterwards.
 