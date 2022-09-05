import os
from PIL import Image,ImageStat
import time
import os
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


start = time.time()
image_folder = r'D:\anime&running man & movie\photo\for check'
location = r'D:\anime&running man & movie\photo\for check'
final_location = r'D:\anime&running man & movie\photo_check_no_repeat_version_2022\2017'

image_files = [_ for _ in os.listdir(image_folder) if _.endswith('png') ]

collection = []
duplicate_file = []

for file_org in image_files:

    if not file_org in duplicate_file:

        image_org = Image.open(os.path.join(image_folder,file_org))

        pix_mean1 = ImageStat.Stat(image_org).mean


        for file_check in image_files:
            if file_check != file_org:
                image_check = Image.open(os.path.join(image_folder,file_check))
                pix_mean2 = ImageStat.Stat(image_check).mean

                if pix_mean1 == pix_mean2:
                    duplicate_file.append(file_org)
                    duplicate_file.append(file_check)

                    duplicate_path = os.path.join(location, file_check)
                    os.remove(duplicate_path)
                    index = image_files.index(file_check)
                    image_files.pop(index)

# try again 

end = time.time()
print(end - start)



