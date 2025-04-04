from PIL import Image

def decrypt_text_from_image(image_path, key_file_path):
    image = Image.open(image_path)
    pixels = image.load()

    with open(key_file_path, "r") as key_file:
        keys = [line.strip() for line in key_file.readlines()]

    decrypted_text = ""

    for key in keys:
        x, y = map(int, key.split(","))

        r, g, b = pixels[x, y]

        decrypted_char = chr(g)

        decrypted_text += decrypted_char

    return decrypted_text

image_path = "output_image.png"
key_file_path = "keys.txt"

hidden_text = decrypt_text_from_image(image_path, key_file_path)
print(f"Hidden text: {hidden_text}")
