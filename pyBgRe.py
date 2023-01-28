from rembg import remove
from PIL import Image
import os

def remove_bg(img_path, img_name, output_dir):
    output_path = output_dir + '\\' + img_name 
    input = Image.open(img_path)
    bg_remove_img = remove(input)
    image_size = bg_remove_img.size
    width = image_size[0]
    height = image_size[1]
    print("-----")
    print(img_name)
    if width != height:
        bigside = width if width > height else height
        print(img_name + "of bg removed!")
        background = Image.new('RGBA', (bigside, bigside), (255, 255, 255, 255))
        offset = (int(round(((bigside - width) / 2), 0)), int(round(((bigside - height) / 2), 0)))
        background.paste(bg_remove_img, offset, bg_remove_img)
        background.save(output_path, "PNG")
        print(img_name + " has been resized !")
    else:
        bg_remove_img.save(output_path, "PNG")


if __name__ == "__main__":
    print("start")
    input_path = '.\\input_dir'
    output_path = '.\\output_dir'
    for img_file in os.listdir(input_path):
        print(img_file)
        remove_bg(input_path+".\\"+img_file, img_file, output_path)

    print("end")