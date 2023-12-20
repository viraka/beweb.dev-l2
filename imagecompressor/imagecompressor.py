from PIL import Image
import os

def compress_image(input_image_path, output_image_path, quality=20):
    image = Image.open(input_image_path)
    image.save(output_image_path, optimize=True, quality=quality)

def compress_images_in_directory(input_dir, output_dir, quality=20):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            input_image_path = os.path.join(input_dir, filename)
            output_image_path = os.path.join(output_dir, filename)
            compress_image(input_image_path, output_image_path, quality)

input_directory = "input_images_folder"
output_directory = "compressed_images_folder"

# Adjust the quality level as needed (0-100)
compression_quality = 20

compress_images_in_directory(input_directory, output_directory, compression_quality)
print("Compression completed!")