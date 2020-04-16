  
def scrape():

    from splinter import Browser
    from bs4 import BeautifulSoup
    import pandas as pd
    from pprint import pprint

    import time
    from bs4 import BeautifulSoup as bs
    import pandas as pd
    import numpy as np
    from selenium import webdriver
    import requests as req
    import re




    def init_browser():
        executable_path = {'executable_path' : '/usr/local/bin/chromedriver'}
        return Browser('chrome', **executable_path, headless=False)


# Function to Scrape NASA title

    def mars_title():

        url = "https://mars.nasa.gov/news/" 
        response = req.get(url)

        soup = bs(response.text, 'html5lib')

        news_title = soup.find("div", class_="content_title").text
        return news_title


    def mars_text():

        nasa_browser = init_browser()

        url = "https://mars.nasa.gov/news/"
        nasa_browser.visit(url)
        time.sleep(30)

        nasa_html = nasa_browser.html
        soup = BeautifulSoup(nasa_html, "html.parser")


        content_text = soup.find("div", class_="article_teaser_body").get_text()
        return content_text


    news_title = mars_title()
    news_p = mars_text()



#Function to Scrape JPL data
    def scrape_jpl():

        # Initialize browser
        jpl_browser = init_browser()

        # Visit the nasa jpl site
        url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        jpl_browser.visit(url)

        # Scrape page into soup
        jpl_html = jpl_browser.html
        soup = BeautifulSoup(jpl_html, "html.parser")

        # Find featured image
        mars_image = "https://www.jpl.nasa.gov/" + soup.find(
            "section", class_="centered_text clearfix main_feature primary_media_feature single"
        ).find(
        "article", class_="carousel_item"
        )["style"].split()[1][5:57]
        return mars_image


    featured_img_url = scrape_jpl()

  # Function to scrape weather data
    def scrape_weather_tweet():

        twitter_response = req.get('https://twitter.com/marswxreport?lang=en')
        soup = bs(twitter_response.text, 'html.parser')
        tweet_containers = soup.find_all('div', class_='js-tweet-text-container')
        mars_weather = tweet_containers[0].text
        return mars_weather

    mars_tweet = scrape_weather_tweet()     


    def scrape_facts():

        # Visit the specefacts site
        facts_url = "https://space-facts.com/mars/"

        mars_table = pd.read_html(facts_url)

        # Return results
        mars_df = mars_table[0]
        mars_df = mars_df.rename( columns = {0 : "fact", 1 : "value"})
        
       

        mars_html = mars_df.to_html()

        print(mars_html)
        return(mars_html)


    facts_table_df = scrape_facts()

    # Function to scrape hemisphere data
    def scrape_hemispheres():

        # Initialize browser
        hemis_browser = init_browser()

        # Visit the Astrogeology site
        hemis_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

        url_1 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
        url_2 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
        url_3 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
        url_4 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"

        #URL 1
        hemis_browser.visit(url_1)

        # Scrape page into soup
        html_1 = hemis_browser.html
        soup_1 = BeautifulSoup(html_1, "html.parser")

        # Find info
        photo_1 = "https://www.jpl.nasa.gov/" + soup_1.find(
            "img", class_="wide-image"
        )["src"]

        title_1 = soup_1.find(
            "h2", class_="title"
        ).text


        #URL 2
        hemis_browser.visit(url_2)

        # Scrape page into soup
        html_2 = hemis_browser.html
        soup_2 = BeautifulSoup(html_2, "html.parser")

        # Find info
        photo_2 = "https://www.jpl.nasa.gov/" + soup_2.find(
            "img", class_="wide-image"
        )["src"]

        title_2 = soup_2.find(
            "h2", class_="title"
        ).text


        #URL 3
        hemis_browser.visit(url_3)

        # Scrape page into soup
        html_3 = hemis_browser.html
        soup_3 = BeautifulSoup(html_3, "html.parser")

        # Find info
        photo_3 = "https://www.jpl.nasa.gov/" + soup_3.find(
            "img", class_="wide-image"
        )["src"]

        title_3 = soup_3.find(
            "h2", class_="title"
        ).text


        #URL 4
        hemis_browser.visit(url_4)

        # Scrape page into soup
        html_4 = hemis_browser.html
        soup_4 = BeautifulSoup(html_4, "html.parser")

        # Find info
        photo_4 = "https://www.jpl.nasa.gov/" + soup_4.find(
            "img", class_="wide-image"
        )["src"]

        title_4 = soup_4.find(
            "h2", class_="title"
        ).text



        # Store in dictionary
        hemisphere_image_urls = [
        {"title": title_1, "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": title_2, "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": title_3, "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
        {"title": title_4, "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
        ]


        # Return results
        return hemisphere_image_urls

    mars_hemispheres = scrape_hemispheres()

    mars_dict = {
    "news_title" : news_title,
    "news_p" : news_p,
    "mars_image" : _img_url,
    "mars_tweet" : mars_weather,
    "facts_table_df" : mars_facts,
    "mars_hemispheres" : mars_hemispheres
    }

    return(mars_dict)