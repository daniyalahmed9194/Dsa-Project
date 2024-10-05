from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Fix the path to Chrome WebDriver
service = Service(executable_path=r'C:\\Users\\lenovo\Desktop\\gmd\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)
prices = []  
ratings = []  
solds = []  
pics = []  
titles = []
discounts = []
d_prices = []

# Navigate to Flipkart
driver.get('https://www.daraz.pk/catalog/?q=handfree')
try:
    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'im-app__cont-minimize'))
    )
    close_button.click()
    time.sleep(1)  # Wait for the element to minimize
except Exception as e:
    print(f"Popup not found or could not be closed: {e}")

# Extract page source and parse it using BeautifulSoup
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

page_number = 1

while page_number <= 85: 
    for product in soup.findAll('div', attrs={'class': 'Bm3ON'}):  # Targeting correct product container
        # Extract product title
        title = product.find('div', attrs={'class': 'RfADt'})
        if title:
            titles.append(title.text)
        else:
            titles.append("No title")
        
        # Extract product price
        price = product.find('span', attrs={'class': 'ooOxS'})
        if price:
            prices.append(price.text)
        else:
            prices.append("No price")

        discout = product.find('span', attrs={'class': 'IcOsH'})
        if discout:
            discounts.append(discout.text)
        else:
            discounts.append("No discount")
        d_price = product.find('span', attrs={'class': 'ooOxS'})
        if d_price:
            # Clean up the price text by removing commas and currency symbols
            cleaned_price = d_price.text.replace(',', '').replace('Rs.', '').replace('$', '').strip()
            # Convert to float and then multiply
            d_prices.append(0.5 * float(cleaned_price))
        else:
            d_prices.append("No d_price")
        # Extract product rating (if available)
        rating = product.find('div', attrs={'class': 'mdmmT _32vUv'})
        if rating:
            ratings.append(rating.text.strip())
        else:
            ratings.append("No rating")

        # Extract number of items sold (if available)
        sold = product.find('span', attrs={'class': '_1cEkb'})
        if sold:
            solds.append(sold.text.strip())
        else:
            solds.append("Not sold")
    
         #Extract product image URL (if available)
        #pic = product.find('img', attrs={'class': '_95X4G'})
        #if pic and pic.has_attr('src'):
        #    pics.append(pic['src'])
        #else:
        #    pics.append("No image")
        #pic = product.find('img', attrs={'type': 'product'})
        #if pic and 'src' in pic.attrs:
        #    pics.append(pic['src'])
        #else:
        #    pics.append("No image")
        # Find the img tag directly
        pic = product.find('img')
        #
        ## Check if the img tag exists and if it has a 'src' attribute
        if pic and pic.has_attr('src'):
            pics.append(pic['src'])  # Extract only the src attribute
        else:
            pics.append("No image")


        
          
           
    try:
        if page_number < 102:
            # Wait until the pagination element (li with title equal to page_number + 1) is clickable
            next_page_li = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//li[@title='{page_number + 1}']"))
            )
            next_page_link = next_page_li.find_element(By.TAG_NAME, "a")  # Find the <a> link inside the <li> tag
            
            # Scroll the next page link into view before clicking
            driver.execute_script("arguments[0].scrollIntoView(true);", next_page_link)
            time.sleep(1)  # Add a small delay to ensure the element is scrolled into view

            # Force-click the next page link using JavaScript to avoid any element intercept
            driver.execute_script("arguments[0].click();", next_page_link)

            page_number += 1  # Increment page number
            time.sleep(3)  # Wait for the next page to load fully
        else:
            break
    except Exception as e:
        print(f"Error: {e}")
        break



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
df.to_csv('Daraz2.csv', index=False, encoding='utf-8')

# Close the driver
driver.quit()