from PIL import Image
import os


def crop_images(folder_path, output_folder, target_size=(200, 200)):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # List all files in the input folder
    files = os.listdir(folder_path)

    for file_name in files:
        # Construct the full path to the image
        input_path = os.path.join(folder_path, file_name)

        # Open the image
        image = Image.open(input_path)

        # Get the center coordinates for cropping
        width, height = image.size
        left = (width - target_size[0]) // 2
        top = (height - target_size[1]) // 2
        right = (width + target_size[0]) // 2
        bottom = (height + target_size[1]) // 2

        # Crop the image
        cropped_image = image.crop((left, top, right, bottom))

        # Save the cropped image to the output folder
        output_path = os.path.join(output_folder, file_name)
        cropped_image.save(output_path)


if __name__ == "__main__":
    # Replace 'your_images_folder' with the path to your 'images' folder
    images_folder = 'images'

    # Replace 'your_output_folder' with the path where you want to save the cropped images
    output_folder_oranges = 'images_cropped/oranges'
    output_folder_non_oranges = 'images_cropped/non-oranges'

    # Crop images in the 'oranges' folder
    crop_images(os.path.join(images_folder, 'oranges'), output_folder_oranges)

    # Crop images in the 'non-oranges' folder
    crop_images(os.path.join(images_folder, 'non-oranges'),
                output_folder_non_oranges)
