import os
import shutil

# Define the path to the directory containing the car_index folders
CAR_INDEX_PATH = 'classified_images'  # Update this to the correct path
DATASET_PATH = 'grouped_datasets'  # Path to store grouped datasets


def create_directory(path):
    """Create a directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)


def classify_folders_by_image_count():
    """Group car folders by the number of images they contain."""
    # Create the base directory for grouped datasets
    create_directory(DATASET_PATH)

    # Iterate over all folders in the car_index directory
    for folder in os.listdir(CAR_INDEX_PATH):
        folder_path = os.path.join(CAR_INDEX_PATH, folder)

        # Ensure we're processing only directories
        if os.path.isdir(folder_path):
            image_count = len([f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))])

            # Create a new directory named by the image count (e.g., dataset_with_10_images)
            target_dir = os.path.join(DATASET_PATH, f'dataset_with_{image_count}_images')
            create_directory(target_dir)

            # Move the current car folder to the appropriate grouped dataset directory
            shutil.move(folder_path, os.path.join(target_dir, folder))
            print(f'Moved {folder} to {target_dir}')


if __name__ == '__main__':
    classify_folders_by_image_count()
