from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time


def click_page_number(page_number):
    try:
        # Construct the XPath for the pagination button based on the page number
        pagination_button_xpath = f"//a[@class='cn++Ap' and text()='{page_number}']"
        
        # Wait until the pagination button is clickable and click it
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pagination_button_xpath))).click()
        print(f"Clicked on page {page_number}")
        
        time.sleep(5)  # Optional: Wait for page to load before further actions
    except Exception as e:
        print(f"Error occurred while clicking on page {page_number}: {e}")

# Set up the Chrome WebDriver
service = Service(executable_path=r'C:\\Users\\lenovo\\Desktop\\gmd\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Lists to store data

prices = []   
ratings = []   
solds = []  
pics = []  
titles = [] 
discounts = []
d_prices = []

# Navigate to Flipkart search page
driver.get('https://www.flipkart.com/search?q=handfree&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')

# Give the page time to load
driver.implicitly_wait(15)

# Set page limit
page_limit = 3
current_page = 1

# Loop through pages until the page limit is reached
for page in range(1, 26):
    click_page_number(page)
    # Extract page source and parse with BeautifulSoup
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')

    # Loop through each product entry and extract details
    for product in soup.findAll('div', attrs={'class': 'slAVV4'}):  # Targeting correct product container
        # Extract product title
        title = product.find('a', attrs={'class': 'wjcEIp'})
        if title:
            titles.append(title.text)
        else:
            titles.append("No title")
        
        # Extract product price
        price = product.find('div', attrs={'class': 'Nx9bqj'})
        if price:
            cleaned_price = price.text.replace('$', '').strip()
            prices.append("Rs. "+price.text)
        else:
            prices.append("No price")

        discout = product.find('div', attrs={'class': 'UkUFwK'})
        if discout:
            discounts.append(discout.text)
        else:
            discounts.append("No discount")
        d_price = product.find('div', attrs={'class': 'Nx9bqj'})
        if d_price:
            d_prices.append(d_price.text)
        else:
            d_prices.append("No d_price")
        # Extract product rating (if available)
        rating = product.find('span', attrs={'class': 'Y1HWO0'})
        if rating:
            ratings.append(rating.text.strip())
        else:
            ratings.append("No rating")

        # Extract number of items sold (if available)
        sold = product.find('span', attrs={'class': 'Wphh3N'})
        if sold:
            solds.append(sold.text.strip())
        else:
            solds.append("Not sold")
        
        # Extract product image URL (if available)
        pic = product.find('img', attrs={'class': 'DByuf4'})
        if pic and 'src' in pic.attrs:
            pics.append(pic['src'])
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
df.to_csv('flip_products3.csv', index=False, encoding='utf-8')

# Close the driver
driver.quit()

print("Scraping completed and data saved to flip_products.csv")
