from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
import time
from PIL import Image
import requests
import io

food_keyword_dict={
    'Dumpling': ['dumpling', 'sủi cảo'],
    'Waffle': ['waffle', 'bánh waffle'],
    'Pancake': ['pancake', 'bánh pancake'],
    'Cheesecake': ['cheesecake', 'bánh cheesecake'],
    'Garlic bread': ['garlic bread', 'bánh mì bơ tỏi'],
    'Cha gio':['chả giò', 'fried spring rolls'],
    'Fried rice':['cơm chiên', 'fried rice'],
    'Roasted duck':['vịt quay', 'roasted duck'],
    'Sushi':['sushi', '寿司'],
    'French fries':['khoai tây chiên', 'homemade french fries'],
    'Hamburger':['hamburger', 'bánh mì hamburger'],
    'Spaghetti':['mì spaghetti','spaghetti'],
    'Chicken curry':['cà ri gà', 'chicken curry'],
    'Bbq chicken wings':['bbq chicken wings', 'cánh gà nướng bbq'],
    'Pizza':['pizza', 'bánh pizza'],
    'Burrito':['burrito', 'bánh burrito'],
    'Donut':['donut', 'bánh donut'],
    'Sandwich':['sandwich', 'bánh sandwich kep'],
    'Ramen':['ramen', '拉麺'],
    'Omelette':['omelette', 'オムレツ'],
    'Pad thai':['pad thai', 'mì xào kiểu thái']
}

urls_path = 'D:/Projects/HealthStarRating/Food-data/Urls/'
images_path = 'D:/Images/'


def scroll_down(driver, delay):
    prev_height = -1
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(delay)
        new_height = driver.execute_script('return document.body.scrollHeight;')
        if new_height == prev_height:
            try:
                driver.find_element(By.XPATH,"//input[@value='Show more results']").click()
                scroll_down(driver, delay)
            except:
                break
        prev_height=new_height        

# Return the source of each google image thumbnails
def get_google_image_urls(keyword_dict, save_path, max_images):
    # Configure browser
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    options.set_preference("general.useragent.override","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0")
    driver = webdriver.Firefox(options=options)
    for item in keyword_dict.keys():
        total_image_urls =set()
        file_path = save_path + item + ".txt"
        for keyword in keyword_dict[item]:
            try:
                query = keyword.replace(" ", "+")
                url = f"https://www.google.com/search?q={query}&sca_esv=580505413&tbm=isch&sxsrf=AM9HkKmXqORwOnhAIyUfA80FanIC-jxpYQ:1699461430039&source=lnms&sa=X&ved=2ahUKEwiF6uKW67SCAxdriverrlYBHeCVA8cQ_AUoAXoECAMQAw&biw=1495&bih=715&dpr=1.25"
                driver.get(url)
                image_skips = 0
                counter = 0
                image_urls = set()
            except:
                break
            scroll_down(driver, 2.5)
            thumbnails= driver.find_elements(By.XPATH, "//img[contains(@class, 'Q4LuWd')]")
            for img in thumbnails[len(image_urls) + image_skips : max_images]:
                try:
                    img.click()
                    time.sleep(1)
                except:
                    continue
                images = driver.find_elements(By.XPATH, "//img[contains(@class, 'pT0Scc')]")
                for image in images:
                    if image.get_attribute('src') in total_image_urls:
                        max_images += 1
                        image_skips += 1
                        break
                    if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                        image_urls.add(image.get_attribute('src'))
                        counter += 1
                        print(f'|-- Found {len(image_urls)} url --|')
            total_image_urls.update(image_urls)
        with open(file_path,'w') as f:
            for image_url in total_image_urls:
                f.write(f"{image_url}\n")
            f.close()   
        print(f'Get image urls {item} complete!')
    driver.quit()


# Create image folder for each item
def create_image_folders(folder_path, items):
    for item in items:
        file_path = folder_path + f"{item}"
        Path(file_path).mkdir(parents=True, exist_ok=True)


# Download images from their source urls 
def download_image_from_urls(items, urls_path, download_path):
    create_image_folders(download_path, items)
    for item in items:
        item_name= item.replace(" ", "_")
        folder_path = download_path + f'{item}'
        url_path = urls_path + f'{item}.txt'
        with open(url_path, 'r') as f:
            urls = [line.rstrip() for line in f]
            f.close()
        for i,url in enumerate(urls):
            try:
                image_name = f'{item_name}_{i}.JPG'
                image_path = folder_path + '/' + image_name
                url_content = requests.get(url, timeout = 60).content
                url_file = io.BytesIO(url_content)
                image = Image.open(url_file)
                with open(image_path, 'wb') as f:
                    image.save(f)
            except:
                continue
        print(f'Download {item} images complete!')

# get_google_image_urls(food_keyword_dict, urls_path, 400)
download_image_from_urls(food_keyword_dict, urls_path, images_path)
