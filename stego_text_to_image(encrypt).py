import random
from PIL import Image

def hide_text_in_image(text, image_path, output_image_path, output_key_path):
    image = Image.open(image_path)
    pixels = image.load()

    ascii_values = [ord(char) for char in text]

    width, height = image.size
    used_pixels = set() 
    keys = [] 

    for char_ascii in ascii_values:
        while True:
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)

            if (x, y) not in used_pixels:
                used_pixels.add((x, y))

                r, g, b = pixels[x, y]

                new_g = char_ascii

                new_g = min(max(new_g, 0), 255)

                pixels[x, y] = (r, new_g, b)

                keys.append((x, y))
                break

    image.save(output_image_path)

    with open(output_key_path, "w") as key_file:
        for key in keys:
            key_file.write(f"{key[0]},{key[1]}\n")

    print(f"Text hidden in {output_image_path}")
    print(f"Keys saved to {output_key_path}")


text_to_hide = """
The Python interpreter is easily extended with new functions and data types 
implemented in C or C++ (or other languages callable from C). Python is also 
suitable as an extension language for customizable applications.
"""
image_path = "input_image.png" 
output_image_path = "output_image.png"
output_key_path = "keys.txt"

hide_text_in_image(text_to_hide, image_path, output_image_path, output_key_path)
print(f"Process completed successfully!")
