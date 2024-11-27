import time

def scroll_end(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        
        
def get_page_data(driver):
    all_ = driver.find_elements(By.CSS_SELECTOR, value = 'div[class^="browse-search__pod c"]')
    ic(len(all_))
    data = {}
    i = 0
    for element in all_:
        name = description = left_paner =  sponsored = right_paner = price =  links = rating_count = model = pickup = delivery =  ''
        rating = 0
        i+=1
        # print(f'element {i}')

        try:
            name = element.find_element(By.CSS_SELECTOR, value = 'p[data-testid="attribute-brandname-above"]').text
        except:
            name = 'no name'
        description = element.find_element(By.CSS_SELECTOR, value = 'span[class="sui-text-primary sui-font-regular sui-mb-1 sui-line-clamp-5 sui-text-ellipsis sui-inline"]').text
        try:
            left_paner = element.find_element(By.CSS_SELECTOR, value = 'span[class="sui-cursor-default sui-inline-block sui-bg-[#3e7697] sui-py-1 sui-px-2 sui-font-bold sui-text-sm sui-text-inverse"]').text
        except:
            left_paner = ''
        try:
            element.find_element(By.CSS_SELECTOR, value = 'div[class="sui-inline-block sui-px-2 sui-py-1 sui-bg-subtle"]').text
            sponsored = True
        except:
            sponsored = False
        
        right_paner = element.find_element(By.CSS_SELECTOR, value = 'div[class="sui-absolute sui-z-10 sui-right-0"]').text
        price = element.find_element(By.CSS_SELECTOR, value = 'div[class="price"]').text.replace('\n.\n', '.').replace('$', '')
        un_wanted_links = [ 'https://www.homedepot.com/b/Kitchen-Kitchen-Cabinets/cabinets-cabinet-hardware/hampton-base-cabinets-in-white'
                        ,'https://www.homedepot.com/b/Kitchen-Kitchen-Cabinets/kitchen-cabinets-cabinet-hardware/unfinished-wall-cabinets-in-beech'
                        ,'https://www.homedepot.com/b/Kitchen-Kitchen-Cabinets/cabinets-cabinet-hardware/shaker-base-cabinets-in-white'
                        ,'https://www.homedepot.com/b/Kitchen-Kitchen-Cabinets/kitchen-cabinets-cabinet-hardware/shaker-wall-cabinets-in-white']
        #get links 
        #there is multi links i am not sure of the logic of it's the same i will drop the code 
        links = list(set([i.get_attribute('href').replace("#ratings-and-reviews" , '') for i in element.find_elements(By.CSS_SELECTOR, value = 'a[href]') 
                        if i.get_attribute('href').replace("#ratings-and-reviews" , '')  not in un_wanted_links]))
        try:
            rating = element.find_element(By.CSS_SELECTOR, value = 'span[class="sui-inline-flex sui-gap-2px sui-relative sui-text-primary sui-cursor-pointer sui-pointer-events-none sui-text-left sui-tap-highlight-transparent sui-text-base"]').get_attribute('aria-label').replace(' Stars', '')
        except:
            rating = 0
        rating = float(rating)
        try:
            rating_count = element.find_element(By.CSS_SELECTOR, value = 'span[class="sui-font-regular sui-text-xs sui-leading-tight sui-tracking-normal sui-normal-case sui-line-clamp-unset sui-text-primary"]').text.replace('(', "").replace(')', "")
        except:
            rating_count = 0
        rating_count = int(rating_count)
        try:
            model = element.find_element(By.CSS_SELECTOR, value = 'div[class="sui-flex sui-text-xs sui-mb-1 sui-mr-1"]').text.replace('Model# ', "")
        except:
            model = name
        try:
            pickup = element.find_element(By.CSS_SELECTOR, value = 'span[data-component="FulfillmentPodStore"]').text
        except:
            pickup = ''
        try:
            delivery = element.find_element(By.CSS_SELECTOR, value = 'span[data-component="FulfillmentPodShipping"]').text
        except:
            delivery = ''
        
        
        # print(element.text)
        data[i] = [name,description,left_paner,sponsored,rating,rating_count,right_paner,price,links,model,pickup,delivery]
        # print(name,description )
        # print(left_paner,sponsored,right_paner,price,rating,rating_count,model,pickup,delivery)
        # print(links)
        # print("__________________________________")
    return data
        
        #active
        
# <button type="button" class="sui-inline-flex sui-items-center sui-justify-center sui-border-none sui-border-0 focus-visible:sui-bg-button-focus focus-visible:sui-outline-none focus-visible:sui-fill-primary focus-visible:sui-rounded-base hover:sui-rounded-base hover:sui-bg-button-hover-subtle sui-h-11 sui-w-11 sui-fill-primary" role="option" aria-label="Skip to Next Page"><svg class="sui-inline-block sui-align-baseline sui-fill-inherit sui-w-6 sui-h-6" viewBox="0 0 24 24" focusable="false" aria-hidden="true" data-testid="ArrowForwardIcon"><path d="M5.271 1.604 15.555 12 5.271 22.396l1.6 1.582L18.72 12 6.87.02l-1.6 1.583Z"></path></svg></button>

# #in active
# <button type="button" class="sui-inline-flex sui-items-center sui-justify-center sui-border-none sui-border-0 focus-visible:sui-bg-button-focus focus-visible:sui-outline-none focus-visible:sui-fill-primary focus-visible:sui-rounded-base hover:sui-rounded-base sui-h-11 sui-w-11 sui-fill-subtle" role="option" aria-label="Skip to Next Page" disabled=""><svg class="sui-inline-block sui-align-baseline sui-fill-inherit sui-w-6 sui-h-6" viewBox="0 0 24 24" focusable="false" aria-hidden="true" data-testid="ArrowForwardIcon"><path d="M5.271 1.604 15.555 12 5.271 22.396l1.6 1.582L18.72 12 6.87.02l-1.6 1.583Z"></path></svg></button>

# <button type="button" class="sui-inline-flex sui-items-center sui-justify-center sui-border-none sui-border-0 focus-visible:sui-bg-button-focus focus-visible:sui-outline-none focus-visible:sui-fill-primary focus-visible:sui-rounded-base hover:sui-rounded-base hover:sui-bg-button-hover-subtle sui-h-11 sui-w-11 sui-fill-primary" role="option" aria-label="Skip to Next Page"><svg class="sui-inline-block sui-align-baseline sui-fill-inherit sui-w-6 sui-h-6" viewBox="0 0 24 24" focusable="false" aria-hidden="true" data-testid="ArrowForwardIcon"><path d="M5.271 1.604 15.555 12 5.271 22.396l1.6 1.582L18.72 12 6.87.02l-1.6 1.583Z"></path></svg></button>




# <svg class="sui-inline-block sui-align-baseline sui-fill-inherit sui-w-6 sui-h-6" viewBox="0 0 24 24" focusable="false" aria-hidden="true" data-testid="ArrowForwardIcon"><path d="M5.271 1.604 15.555 12 5.271 22.396l1.6 1.582L18.72 12 6.87.02l-1.6 1.583Z"></path></svg>