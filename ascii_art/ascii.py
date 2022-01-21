import PIL.Image

#ascii char use to built art in decending order as '@' being dark pixel and '.' being lightest 
ASCII_CHARS = ['@','#','$','%','?','*','+',';',':',',','.']

#resize img according to required width
def resize_image(image,new_width=100):
    width, height = image.size      #get image width and height using size property
    ratio = height/width
    new_height = int(new_width * ratio)
    resize_image = image.resize((new_height,new_width))     #resizing image using resize method which takes tuples as input
    return resize_image

# conveting image into grayscale
def grayify(image):
    grayscale_image = image.convert('L') 
    return grayscale_image

#convet grayscale char to ascii char
def pixel_to_ascii(image):
    pixels = image.getdata()    #return each pixel grayscale value 
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters


def main(new_width=100):
    #cheacking if there is image in given path or not
    path = input('Enter a valid pathname: \n')
    try: 
        image = PIL.Image.open(path)
    except:
        print(path,'is not valid payh: ')

    new_image_data = pixel_to_ascii(grayify(resize_image(image)))

    pixel_count = len(new_image_data)
    ascii_image = '\n'.join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count,new_width))

    print(ascii_image)

    with open('ascii_image.txt','w') as f:
        f.write(ascii_image)

main()


