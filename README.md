# Scraping-amazon-using-scrapy

**Description:** This project is a webscraper that utilizes Scrapy to scrap pages from amazon. The keyword I used to search the pages of amazon was "Playstation". 
The scraper went through the first 150 pages of amazon and returned The Image link, price and name of each. 
The code for the scraper itself can be found [here](Scrapy_generated_folder/Scrapy_folder/spiders/scraper.py). It's best to keep it in the spider in the spiders folder when using scrapy. Other files uploaded are settings I used for scrapy and Items. I uploaded them as they're, as opposed to other kinds of settings, unintuitive.
The resulting csv file was also uploaded in case one only wanted to merely ook at how the result _looks_ .

**Functionality:** This project can be divided into three parts. They're the three parts that constitute any Scrapy project

1. Every Scrapy project has to begin with defining the class where everything in the project will be embedded. It has to contain the `name` as it's the name you'll be using when running the project in the terminal. `start_urls`: a list that contains all the urls to which you want to apply the code
2. the `parse` function inside which _what_ you want to do with the urls you open is placed.It also contains the items class (found in the items file, it has to be imported in the beginning of the code, as is seen in the beginning of the scraper file provided. It's best practice to always import the items class and yeild items instead of yielding a regular dictionary expression. Usually `response.css()` is the method used to pull any element using it's HTML. I, however, face a problem which is that some of the elements on the page were ads put there by Amazon irrelevent of the search.
The solution I came up with was to:
    1. Pull all elements on the page as list
    2. Use a `for` loop to go through each of those elements and check if the element is sponsored or not. This was done using the css selector `.s-label-popover-hover       .a-color-base::text`.
    3. What we want is to do things to the non-sponsored elements. So we, using the selector check if it returns `None` or not. If it does then it isn't sponsored and we     extract the name, image link and price from that product and store each of them in a csv using `yield items`.
3. The last part is the part that repeats the process for each page within a certain provided range. The range provided here is 10 so it scrapes the first 10 pages and returns them. When the code is run it's run in the terminal using `scrapy crawl [name provided]` in this case since it's `amazon_p` that's the name we'll use. TO store the command has to have `-o [filename].csv` appended to the command. It stores it after it's completed and can be run. The result I got when I first ran it was the one provided with the name "result.csv"
