from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
import time
from PIL import Image
import requests
import io
import pandas as pd

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
food_keyword_list = [
    'Orange juice',
    'Tomato juice',
    'Grape juice',
    'Banana juice',
    'Pineapple juice',
    'Apple juice',
    'Mango juice',
    'Water',
    'Coffee',
    'Decaf coffee',
    'Tea',
    'Green tea',
    'Peach tea',
    'Sweet tea',
    'Lemon tea',
    'Black tea',
    'Ginger tea',
    'Raspberry tea',
    'Pomegranate tea',
    'Soda',
    'Pepsi soda',
    'Sprite soda',
    'Orange soda',
    'Soda coca cola',
    'Diet soda',
    'Lemonade',
    'Limeade',
    'Jelly',
    'Soy milk',
    'Almond milk',
    'Hazelnut milk',
    'Coconut milk',
    'Espresso',
    'Soy latte',
    'Chai latte',
    'Almond milk latte',
    'Hazelnut latte',
    'Milk',
    'Milkshake',
    'Oreo milkshake',
    'Vanilla milkshake',
    'Chocolate milkshake',
    'Strawberry milkshake',
    'Chocolate milk',
    'Vietnamese coffee',
    'Latte',
    'Mocha latte',
    'Nonfat latte',
    'Milk tea',
    'Boba tea',
    'Condensed milk',
    'Hot chocolate',
    'Smoothie',
    'Banana smoothie',
    'Strawberry smoothie',
    'Spinach smoothie',
    'Kiwi smoothie',
    'Tropical smoothie',
    'Pineapple smoothie',
    'Cappuccino',
    'Goi du du',
    'Salad',
    'Lecttuce salad',
    'Spinach salad',
    'Beet salad',
    'Greek salad',
    'Caesar salad',
    'Caprese salad',
    'Edamame salad',
    'Seaweed salad',
    'Pho',
    'Pho ga',
    'Pho nam', 
    'Banh mi',
    'Pork banh mi',
    'Chicken banh mi',
    'Banh goi',
    'Banh can',
    'Banh giay',
    'Banh cuon', 
    'Banh khot', 
    'Banh bot loc', 
    'Banh xeo', 
    'Banh tieu',
    'Banh trang',
    'Banh trung thu',
    'Canh chua', 
    'Bun bo Hue',
    'Bun bo xao',
    'Bun thit nuong', 
    'Cha gio', 
    'Goi cuon',
    'Thit kho nuoc dua',
    'Bao',
    'Fried rice',
    'Kimchi fried rice',
    'Garlic fried rice',
    'Roasted duck',
    'Sushi',
    'Tuna sushi',
    'Salmon sushi',
    'Shrimp sushi',
    'Sushi california',
    'French fries',
    'Sweet potato fries',
    'Chicken burger',
    'Turkey burger',
    'Bacon burguer',
    'Hamburger',
    'Spaghetti',
    'Spaghetti carbonara',
    'Spaghetti bolognese',
    'Sausage spaghetti',
    'Chicken curry',
    'Fried chicken',
    'Fried chicken wing',
    'Fried chicken breast',
    'Fried chicken tenders',
    'Fried chicken drumstick',
    'Nugget',
    'Fish nugget',
    'Bbq chicken wings',
    'Bbq boneless wings',
    'Bbq buffalo wings',
    'Bbq honey wings',
    'Burrito',
    'Bean burrito',
    'Steak burrito',
    'Chicken burrito',
    'Donut',
    'Mapple donut',
    'Sandwich',
    'Ham sandwich',
    'Tuna sandwich',
    'Club sandwich',
    'Bacon sandwich',
    'Turkey sandwich',
    'Salmon sandwich',
    'Chicken sandwich',
    'Lobster roll sandwich',
    'Peanut butter sandwich',
    'Sashimi',
    'Takoyaki',
    'Tacos',
    'Fish tacos',
    'Beef tacos',
    'Chicken tacos',
    'Breakfast tacos',
    'Boiled egg',
    'Soft boiled egg',
    'Fried egg',
    'Deviled egg',
    'Omelette',
    'Stew',
    'Pork stew',
    'Lamb stew',
    'Seafood stew',
    'Chicken stew',
    'Beef stew',
    'Grilled fish',
    'Grilled steak',
    'Grilled salmon',
    'Grilled shrimp',
    'Grilled octopus',
    'Watermelon',
    'Banana',
    'Avocado',
    'Apple',
    'Orange',
    'Mandarins orange',
    'Mango',
    'Jackfruit',
    'Cabbage',
    'Red cabbage',
    'Spinach',
    'Strawberry',
    'Tomato',
    'Cucumber',
    'Carrot',
    'Cauliflower',
    'Broccoli',
    'Grape',
    'Pear',
    'Peach',
    'Pickle',
    'Popcorn',
    'Ramen',
    'Chicken ramen',
    'Tonkatsu ramen',
    'Miso ramen',
    'Miso soup',
    'Imitation crab',
    'Ham',
    'Pad thai',
    'Pork chop',
    'Meetball',
    'Tofu',
    'Fried tofu',
    'Mapo tofu',
    'Pad thai',
    'Cooked rice',
    'Cooked brown rice',
    'Shrimp and grits',
    'Gyoza',
    'Grilled pork chop',
    'Fried pork chop',
    'Bbq pork chop',
    'Prime rib',
    'Beef carpaccio',
    'Salmon carpaccio',
    'Beef tartare',
    'Salmon tartare',
    'Beignet',
    'Bibimbap',
    'Dim sum',
    'Tofu bibimbap',
    'Chicken bibimbap',
    'Ceviche',
    'Mixto ceviche',
    'Ceviche octopus',
    'Shrimp ceviche',
    'Scallop ceviche',
    'Chicken quesadilla',
    'Churros',
    'Clam chowder',
    'Corn chowder',
    'Crab chowder',
    'Seafood chowder',
    'Salmon chowder',
    'Crab cake',
    'Croque madame',
    'Dumpling',
    'Soup dumplings',
    'Fried dumpling',
    'Chicken dumplings',
    'Vegetable dumplings',
    'Shrimp dumpling',
    'Edamame',
    'Egg benedict',
    'Escargot',
    'Falafel',
    'Filet mignon',
    'Fish and chips',
    'Potato chips',
    'Sweet potato chips',
    'Foie gras',
    'Soup',
    'Bean soup',
    'Onion soup',
    'Potato soup',
    'Tomato soup',
    'Chicken soup',
    'Broccoli soup',
    'Garlic bread',
    'Garlic breadstick',
    'Gnocchi',
    'Hot dog',
    'Macaron',
    'Mussels',
    'Paella',
    'Veggie paella',
    'Seafood paella',
    'Samosa',
    'Chicken samosa',
    'Vegetable samosa',
    'Huevos ranchero',
    'Sticky rice',
    'Mango sticky rice',
    'Xoi',
    'Char siu',
    'Mochi',
    'Mango mochi',
    'Strawberry mochi',
    'Daifuku mochi',
    'Yogurt',
    'Greek yogurt',
    'Nonfat yogurt',
    'Ice cream',
    'Ice cream sandwich',
    'Ice cream chocolate',
    'Vanilla ice cream',
    'Pudding',
    'Bread pudding',
    'Banana bread pudding',
    'Pumpkin bread pudding',
    'Nutella bread pudding',
    'Bread pudding chocolate',
    'Banana pudding',
    'Crepe',
    'Chocolate crepe',
    'Fruit crepe',
    'Cheesecake',
    'Cheesecake pudding',
    'Chocolate cheesecake',
    'Strawberry cheesecake',
    'Blueberry cheescake',
    'Cake',
    'Coffee cake',
    'Chocolate cake',
    'Red velvet cake',
    'Carrot cake',
    'Cookie',
    'Oreo cookie',
    'Chocolate chip cookie',
    'Chocolate cookies',
    'Biscuit',
    'Egg biscuit',
    'Chocolate biscuit',
    'Butter biscuit',
    'Waffle',
    'Pancake',
    'Pizza',
    'Pepperoni pizza',
    'Cheese pizza',
    'Chocolate donut',
    'Sour cream donut',
    'Frosted donut',
    'Grilled cheese',
    'Butter popcorn',
    'Custard pie',
    'Custard',
    'Flan',
    'Chocolate',
    'Brownie',
    'Cupcake',
    'Mini cupcake',
    'Matcha cupcake',
    'Pretzel',
    'Croissant',
    'Egg croissant',
    'Chocolate croissant',
    'French toast',
    'Apple pie',
    'Pumpkin pie',
    'Sweet potato pie',
    'Baklava',
    'Cannoli',
    'Mousse',
    'Mango mousse',
    'Lemon mousse',
    'Pumpkin mousse',
    'Strawberry mousse',
    'Peanut butter mousse',
    'Passion fruit mousse',
    'Chocolate mousse',
    'Creme brulee',
    'Lasagna',
    'Beef lasagna',
    'Veggie lasagna',
    'Cheese lasagna',
    'Turkey lasagna',
    'Macaroni and cheese',
    'Lobster bisque',
    'Tomato bisque',
    'Crab bisque',
    'Nachos',
    'Nachos cheese',
    'Fajita nachos',
    'Pork nachos',
    'Steak nachos',
    'Nachos chicken',
    'Veggie nachos',
    'Chili nachos',
    'Onion ring',
    'Tiramisu',
    'Shortcake',
    'Strawberry shortcake',
    'Cherry shortcake',
    'Caramel shortcake',
    'Risotto',
    'Shrimp risotto',
    'Chicken risotto',
    'Pumpkin risotto',
    'Short rib risotto',
    'Mushroom risotto',
    'Mashed potato',
    'Mashed sweet potato',
    'Mashed cauliflower',
    'Poutine',
    'Dark chocolate',
    'Chocolate banana',
    'Chocolate orange',
    'Muffin',
    'Egg muffin',
    'Corn muffin',
    'Bran muffin',
    'Berry muffin',
    'Banana muffin',
    'Rasperry muffin',
    'Chocolate chip muffin',
    'Oils',
    'Palm oils',
    'Sesame oils',
    'Vegetable oils',
    'Coconut oils',
    'Margarine',
    'Butter',
    'Cheese',
    'Blue cheese',
    'Cheese plate',
    'Feta cheese',
    'Goat cheese',
    'Swiss cheese',
    'Cheddar cheese',
    'Parmesan cheese',
    'Mozzarella cheese',
    'Cottage cheese',
    'Khoa',
    'Hu tieu',
    'Bun rieu',
    'Com tam',
    'Banh beo',
    'Bun dau mam tom',
    'Banh gio',
]

image_url_dict={'Name':[],
                'Image url':[]}

save_path = 'D:/Projects/HealthStarRating/Food-data/Urls/'
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

def get_food_image_url(keyword_list):        
    # Configure browser
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    options.set_preference("general.useragent.override","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0")
    driver = webdriver.Firefox(options=options)
    for keyword in keyword_list:
        image_url_dict['name'].append(keyword)
        try:
            query = keyword.replace(" ", "+")
            url = f"https://www.google.com/search?q={query}&sca_esv=580505413&tbm=isch&sxsrf=AM9HkKmXqORwOnhAIyUfA80FanIC-jxpYQ:1699461430039&source=lnms&sa=X&ved=2ahUKEwiF6uKW67SCAxdriverrlYBHeCVA8cQ_AUoAXoECAMQAw&biw=1495&bih=715&dpr=1.25"
            driver.get(url)
        except: 
            break
        thumbnail= driver.find_element(By.XPATH, "//img[contains(@class, 'Q4LuWd')]")
        thumbnail.click()
        time.sleep(1)
        image = driver.find_element(By.XPATH, "//img[contains(@class, 'pT0Scc')]")
        if image.get_attribute('src') and 'http' in image.get_attribute('src'):
            image_url_dict['image url'].append(image.get_attribute('src'))
            print(f'|======== Found {keyword} url =========|')
        else:
            image_url_dict['image url'].append('N/A')
            print(f'|======== Can not find {keyword} url =========|')
    df = pd.DataFrame.from_dict(image_url_dict)
    csv_path = Path('D:/Projects/HealthStarRating/Food-data/Urls/food-image-url-test.csv')
    df.to_csv(csv_path, index = False, mode = 'a', header = not csv_path.exists())    
    driver.quit()   
            
            
# get_google_image_urls(food_keyword_dict, urls_path, 400)
# download_image_from_urls(food_keyword_dict, urls_path, images_path)
# get_food_image_url(food_keyword_list)