from pathlib import Path
import imagehash
from PIL import Image
from pathlib import Path
import splitfolders

folders = [
    'Hu tieu',
    'Pho',
    'Banh mi',
    'Banh cuon',
    'Mi quang',
    'Banh bot loc tran',
    'Banh xeo',
    'Banh tieu',
    'Canh chua',
    'Bun bo hue',
    'Bun thit nuong',
    'Cha gio',
    'Goi cuon',
    'Bun rieu',
    'Chao long',
    'Fried rice',
    'Roasted duck',
    'Sushi',
    'French fries',
    'Hamburger',
    'Spaghetti',
    'Chicken curry',
    'Bbq chicken wings',
    'Pizza',
    'Burrito',
    'Donut',
    'Sandwich',
    'Ramen',
    'Omelette',
    'Pad thai',
    'Dumpling',
    'Waffle',
    'Pancake',
    'Cheesecake',
    'Garlic bread',
]

images_path = 'D:/Images/'
dataset_path = 'D:/Projects/HealthStarRating/Food-data/Images/'


def rename_images(folders, images_path):
    for folder in folders:
        folder_path = images_path + folder + '/'
        if Path(folder_path).is_dir:
            files = Path(folder_path).glob('*.JPEG')
            counter = 0
            folder = folder.replace(' ', '_')
            for file in files:
                new_name = f'{counter}{file.suffix}'
                file.rename(folder_path + new_name)
                counter += 1
                print(f'|- Renamed {file.name} to {new_name}')
        else: 
            print(f'{folder} not exists!')
        print(f'Rename {folder} images finish!')               

def filter_images(folders, images_path, image_size):
    for folder in folders:
        folder_path = images_path + folder
        files = Path(folder_path).glob('*.JPG') 
        for file in files: 
            size0 = Path(file).stat().st_size
            if size0 < image_size*1024:
                Path.unlink(file)

def find_similar_images(folders, images_path, different_points):
    for folder in folders:
        folder_path = images_path + folder
        files = Path(folder_path).glob('*.JPG')
        image_urls = []
        image_hashes= []
        urls_remove = set()
        for file in files:
            try:
                image = Image.open(file)
                ahash = imagehash.average_hash(image)
                phash = imagehash.phash(image)
                dhash = imagehash.dhash(image)
                image_urls.append(file)
                image_hashes.append([ahash, phash, dhash])
            except:
                urls_remove.add(file)
        idx0 = 0
        while idx0 < len(image_urls):
            url0 = image_urls[idx0]
            counter = 0 
            ahash0, phash0, dhash0 = image_hashes[idx0]
            if not (ahash0 and phash0 and dhash0):
                continue
            insert_count = 0
            for idx1 in range(idx0 +1, len(image_urls)):
                url1 = image_urls[idx1]
                ahash1, phash1, dhash1 = image_hashes[idx1]
                if not (ahash1, phash1, dhash1):
                    continue
                distances=[ahash0 - ahash1, phash0 - phash1, dhash0 - dhash1]
                differ_results = sum(distance < different_points for distance in distances)
                if differ_results >=2:
                    print(f'|-- {url0.stem} similar with image: {url1.stem}')
                    new_name = f'{url0.stem}_({counter}){url0.suffix}'
                    new_url = url1.rename(folder_path + '/' + new_name)
                    counter += 1
                    insert_count += 1
                    image_hashes.insert(idx0 + 1, image_hashes[idx1])
                    image_urls.insert(idx0 + 1, image_urls[idx1])
                    del image_hashes[idx1 + 1]
                    del image_urls[idx1 +1]
                    size0 = Path(url0).stat().st_size
                    if size0 <20*1024:
                        urls_remove.add(url0)
                    size1 = Path(new_url).stat().st_size
                    if size1 < 20*1024: 
                        urls_remove.add(new_url)
            idx0 += insert_count + 1
        for url in urls_remove:
            try:
                Path.unlink(url)
            except:
                continue
        print(f'|- {folder} finish!')
    print('Finish!')

# find_similar_images(folders, images_path, 5)
# filter_images(folders, images_path, 15)
# rename_images(folders, images_path)
# splitfolders.ratio(input = images_path, output = dataset_path, seed = 1337, ratio = (.8, .1, .1,), group_prefix= None, move = False)