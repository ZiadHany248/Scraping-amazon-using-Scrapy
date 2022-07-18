#importing scrapy library and items file
import scrapy
from ..items import Amazon2Item

#creating a class
class amazon(scrapy.Spider):

    #naming the spider
    name = 'amazon_p'
    #giving it the urls it should start from
    start_urls = ['https://www.amazon.com/s?k=laptop&s=date-desc-rank&page=1']
    
    next_page = 2   
    #parse function
    def parse(self, response):
        
        #creating an instance of the items class
        items = Amazon2Item()
        
        #For this spider we want to grab all the info one the page
        #that is NOT sponsered content, so I'll be grabbing each container
        #and checking if it has "sponsered" in it; if it doesn't we'll extract
        #info from it
        
        #grabbing a list of containers
        containers = response.css('.s-card-border').extract()
        
        #iterating through them
        for i in range(len(containers)):

            #grabbing the text that should be "Sponsered" if the content
            #really is sponsored
            selection = scrapy.Selector(text = containers[i]).css('.s-label-popover-hover .a-color-base::text').get()
            
            #If it isn't sponsored we'll extract the name, price and image link
            #of each product
            if selection == None:
                prod_name = scrapy.Selector(text = containers[i]).css('.a-size-medium::text').extract()
                price = scrapy.Selector(text = containers[i]).css('.a-price-whole::text').extract()
                image = scrapy.Selector(text = containers[i]).css('.s-image::attr(src)').extract()       
                items['prod_name'] = prod_name
                items['price'] = price
                items['image'] = image

                yield items
        #Going through multiple pages using a loop to determine how many pages we
        #want
        if amazon.next_page < 10:
            amazon.next_page +=1
            followed = 'https://www.amazon.com/s?k=laptop&s=date-desc-rank&page='+ str(amazon.next_page)
            
            yield response.follow(followed ,callback = self.parse)