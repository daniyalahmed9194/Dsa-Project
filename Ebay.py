from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time
import re

# Set up the Chrome WebDriver
service = Service(executable_path=r'C:\Users\lenovo\Desktop\gmd\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Lists to store data
prices = []   
ratings = []   
solds = []  
pics = []  
titles = [] 
discounts = []
d_prices = []

# Navigate to eBay search page
driver.get('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=earpods&_sacat=0&_odkw=pods&_osacat=0')
def click_page_number(page_number):
    try:
        # Construct the XPath for the pagination button based on the page number
        pagination_button_xpath = f"//a[@class='pagination__item' and text()='{page_number}']"
        
        # Wait until the pagination button is clickable and click it
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pagination_button_xpath))).click()
        print(f"Clicked on page {page_number}")
        
        time.sleep(5)  # Optional: Wait for page to load before further actions
    except Exception as e:
        print(f"Error occurred while clicking on page {page_number}: {e}")
# Give the page time to load
driver.implicitly_wait(9)

for page in range(1, 86):
    click_page_number(page)
# Extract page source and parse with BeautifulSoup
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')

    # Loop through each product entry and extract details
    for product in soup.findAll('div', attrs={'class': 's-item__wrapper'}):  # Targeting correct product container
        # Extract product title
        title = product.find('div', attrs={'class': 's-item__title'})
        if title:
            titles.append(title.text)
        else:
            titles.append("No title")

        # Extract product price
        price = product.find('span', attrs={'class': 's-item__price'})
        if price:
            cleaned_price = price.text.replace('$', '').strip()
            prices.append("Rs. " + cleaned_price)
        else:
            prices.append("No price")
        d_price = product.find('span', attrs={'class': 's-item__additional-price'})
        if d_price:
            cleaned_dprice = d_price.text.replace('$','').replace('List price: ', '').replace('Was:', '').strip()
            d_prices.append(cleaned_dprice)
        else:
            d_prices.append("No d_price")
        #discout = product.find('span', attrs={'class': 's-item__discount'})
        #cleaned_dis = discout.text.replace('%', '').replace(' off', '').strip()
        #if discout:
        #    discounts.append(cleaned_dis)
        #else:
        #    discounts.append("No discount")
        discout = product.find('span', attrs={'class': 's-item__discount'})

        if discout:
            cleaned_dis = discout.text.replace('$', '').replace('%', '').replace(' off', '').strip()
            discounts.append(cleaned_dis+ "% Off")
        else:
            discounts.append("No discount")

        # Extract product rating (if available)
        rating = product.find('span', attrs={'class': 's-item__reviews-count'})
        #if rating:
        #    ratings.append(rating.text.strip())
        #else:
        #    ratings.append("No rating")
        #rating = product.find('span', attrs={'class': 's-item__reviews-count'})

        if rating:
            # Extract the text content
            rating_text = rating.text.strip()

            # Use regular expression to extract only the numeric part (e.g., number of reviews)
            rating_cleaned = re.findall(r'\d+', rating_text)

            if rating_cleaned:
                ratings.append(rating_cleaned[0])  # Append the first number found (review count)
            else:
                ratings.append("No rating")
        else:
            ratings.append("No rating")
        # Extract number of items sold (if available)
        sold = product.find('span', attrs={'class': 's-item__dynamic s-item__quantitySold'})
        #if sold:
        #    cleaned_sold = sold.text.replace('+', '').replace('sold', '').strip()
        #    solds.append(sold.text.strip())
        #else:
        #    solds.append(0)
        if sold:
            cleaned_sold = sold.text.replace('+', '').replace('sold', '').strip()
            # Further clean to remove extra spaces in between numbers (if any)
            cleaned_sold = ' '.join(cleaned_sold.split())  # Removes multiple spaces
            solds.append(cleaned_sold + " sold")
        else:
            solds.append("Not sold")

        # Extract product image URL (if available)
        #pic = product.find('div', attrs={'src': 's-item__image-wrapper image-treatment'})
        #if pic and 'src' in pic.attrs:
        #    pics.append(pic['src'])
        #else:
        #    pics.append("No image")

        pic = product.find('div', class_='s-item__image-wrapper image-treatment')

        # Find the <img> tag within that div and extract the 'src' attribute
        if pic:
            img_tag = pic.find('img')  # Find the img tag within the div
            if img_tag and 'src' in img_tag.attrs:
                pics.append(img_tag['src'])  # Append the image URL to the list
            else:
                pics.append("No image")
        else:
            pics.append("No image")

# Create a DataFrame with the extracted data
df = pd.DataFrame({
    'Title': titles,
    'Price': prices,
    'Discounted Price': d_prices,
    'Off' : discounts,
    'Rating': ratings,
    'Sold': solds,
    'Image URL': pics
})

# Save the data to a CSV file
df.to_csv('ebay_products_pods_new.csv', index=False, encoding='utf-8')

# Close the driver
driver.quit()

print("Scraping completed and data saved to ebay_products.csv")
