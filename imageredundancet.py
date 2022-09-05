import os
from tkinter import image_names
from PIL import Image,ImageStat
import time
from tabulate import tabulate
from prettytable import PrettyTable
import os
import shutil
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


start = time.time()
image_folder = r'D:\anime&running man & movie\photo\for check'
location = r'D:\anime&running man & movie\photo\for check'
final_location = r'D:\anime&running man & movie\photo_check_no_repeat_version_2022\2017'

#  the r is stringprefix    
# r prefix on strings stands for “raw strings
#  r is raw string make the \ got meaning 
#  the first step is to tell where is the folder

image_files = [_ for _ in os.listdir(image_folder) if _.endswith('png') ]
# image_files = [_ for _ in os.listdir(image_folder) if _.endswith(('.jpg', '.jpeg',png)) ]

#  must space after _ 
#  _ got many meaning , here is like all meaning 
#  this part is to make a list of image files , take from iamge folder , where the imagetype end with jpg

# print(image_files)
collection = []
duplicate_file = []
#  now make a empty list of duplicate files first 

for file_org in image_files:
    #  let all image files == file org 
    if not file_org in duplicate_file:
        # now here is compare file org and duplicate file 
        # here is want the files is orginal only 
        image_org = Image.open(os.path.join(image_folder,file_org))
        #  this image org = imagefolder + file org 
        #   the open is just need to open the file to let them join together 
        pix_mean1 = ImageStat.Stat(image_org).mean
        # Calculate statistics for the given image. 
#  this part is assume all files is original , then calculate all the statistics  of image 

        for file_check in image_files:
            if file_check != file_org:
                image_check = Image.open(os.path.join(image_folder,file_check))
                #  now here is image check = image_folder + flie check 
                pix_mean2 = ImageStat.Stat(image_check).mean

                if pix_mean1 == pix_mean2:
                    duplicate_file.append(file_org)
                    duplicate_file.append(file_check)
                    # collection.append([file_org])
                    # collection.append([file_check])
                    duplicate_path = os.path.join(location, file_check)
                    os.remove(duplicate_path)
                    index = image_files.index(file_check)
                    image_files.pop(index)
                    # image_files.pop([file_check])
                    
        # for x in duplicate_file:
        #     print(collection)
        # path = os.path.join(location, file_check)
        # os.remove(path)

# head = ["Name"]                    
# print(tabulate(collection, headers=head, tablefmt="grid"))
# print(duplicate_file)
# for files in os.listdir(location):
#     shutil.move(image_folder + files , final_location + files)
        # path = os.path.join(location, file_check)
        # os.remove(path)
end = time.time()
print(end - start)



