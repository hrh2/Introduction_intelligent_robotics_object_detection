import os

# Path to the grouped datasets directory
DATASET_PATH = 'grouped_datasets'  # Update to your actual path

def rename_grouped_folders():
    """Rename folders in the grouped datasets directory."""
    for folder in os.listdir(DATASET_PATH):
        folder_path = os.path.join(DATASET_PATH, folder)

        # Ensure only directories are processed
        if os.path.isdir(folder_path):
            try:
                # Extract the image count from the current folder name
                parts = folder.split('_')
                if len(parts) >= 3 and parts[2].isdigit():
                    image_count = parts[2]

                    # Create the new folder name
                    new_folder_name = f'dataset_of_{image_count}_images_each_car'
                    new_folder_path = os.path.join(DATASET_PATH, new_folder_name)

                    # Rename the folder
                    os.rename(folder_path, new_folder_path)
                    print(f'Renamed "{folder}" to "{new_folder_name}"')
                else:
                    print(f'Skipped "{folder}" - Invalid format')
            except Exception as e:
                print(f'Error renaming "{folder}": {e}')

if __name__ == '__main__':
    rename_grouped_folders()
