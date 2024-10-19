**ANPR Dataset Creation from Video Footage(In-Transit-Vehicle-Plate-Captures-\[001\].mp4)**

**Overview**

This project involved creating a dataset for an Automatic Number Plate Recognition (ANPR) system by processing raw video footage. The task was to extract 10 distinct frames per car where the number plate was clearly visible. The extracted frames were then organized into folders, with each car’s images placed in its own folder. The project required both automated tools and manual efforts to complete.

**Tools and Methods Used**

    Python: For frame extraction and organizing datasets based on image counts.
    Batch Script (.bat): For automating the creation of car folders.
    VLC Player: For manual frame-by-frame extraction of missing images.
    Manual Review: For filtering out frames with unreadable plates and organizing the data.
_**Step-by-Step Process**_

**1. Frame Extraction using Python**

I used the extract_car_frames.py script to automate the initial frame extraction. This script relied on OpenCV to detect cars and save relevant frames into an output folder. This process gave me more than 7000 frames, but not all were useful. Some frames contained cars with:

Plates that were not visible or readable.
Multiple cars with visible plates, making classification difficult.
At this point, I moved to manually filtering to select only the relevant frames.

**2. Organize Frames from the Output Folder into Each Car’s Folder**

After filtering the extracted frames, I used the create_car_folders.bat script to create additional car folders. This script:

Generated new folders following the naming convention car_[index], starting from the highest existing index.
For example, if the last folder in the output directory was car_40, the script created new folders from car_41 onwards.
This gave me enough folders to sort the remaining frames properly.
Once the folders were created, I manually moved frames of the same car into the same folder. If I ran out of folders during sorting, I used the .bat script to create more folders as needed. This process ensured that each car’s frames were placed in a dedicated folder for further analysis.

**3. Handling Repeated Cars in Different Frames**

The footage was captured from a moving car, so:

Some cars appeared multiple times under different lighting conditions and at varying angles.
Changes in lighting (e.g., shadows, sunlight) made it necessary to treat some occurrences of the same car as separate cars to maintain dataset consistency.
To manage this, I created separate folders for instances where the same car appeared differently across frames. This avoided confusion in the dataset and ensured each folder contained consistent images of the same car.

**4. Grouping Car Folders Based on Image Count**

After organizing the frames into their respective car folders, I ran a Python script to group folders based on the number of images they contained.

Folders with exactly 10 images were moved into a directory named dataset_of_10_images_each_car.
This organization made it easier to identify which folders needed more images.
If a folder had fewer than 10 images, I marked it for further manual review and completion.

**5. Final Review and VLC Screenshots**

To ensure that every folder had exactly 10 images, I concentrated only on folders with 8 or 9 images. Using VLC Player, I manually captured additional frames from the original video to fill in the gaps.

This step required careful, frame-by-frame extraction to maintain consistency and accuracy in the dataset. After completing this review, I successfully filled 42 folders, ensuring that each contained exactly 10 images.

**Challenges Faced**

_**Frames with Multiple Cars_**

Some frames contained two or more cars with visible plates, which made it challenging to determine how to classify them.
To resolve this, I only kept frames where the main target car’s plate was clearly visible, discarding those with conflicting content.
Cars Appearing in Multiple Frames under Different Conditions

Since the camera was mounted on a moving vehicle, some cars appeared in multiple frames but under different lighting conditions or at different angles.
To handle this, I created separate folders for instances of the same car appearing differently across frames. This helped maintain consistency and avoid misclassification.
Manual Effort for Classification and Organization

While automation helped extract frames, the task still required significant manual work to review the frames and group them correctly.
The batch script made it easier to create additional car folders, but I had to manually move frames of the same car into the correct folders, which was time-consuming.

_**Conclusion**_

This project involved a combination of automated tools and manual effort to create an ANPR dataset from video footage. The task required careful attention to detail, especially in filtering out unreadable plates and dealing with cars appearing under varying conditions. After completing the process, I organized **42** folders with exactly **10** images each, ready for further development and evaluation.

How to Run the Scripts

**1. Extract Frames from the Video**

Use the provided extract_car_frames.py script to extract frames containing cars from the footage.


    python extract_car_frames.py
**2. Create Car Folders for Classification**

Use the `create_car_folders.bat` script to generate new car folders for manual classification.

    create_car_folders.bat 
The script creates folders starting from the next available index based on the current car folders.
**3. Group Car Folders by Image Count**

Use the Python script to group car folders with the same number of images.

    python classify_car_folders.py
**4. Rename Grouped Dataset Folders**

Run the following script to rename folders using the new naming convention.

bash
Copy code
python rename_grouped_folders.py

**Directory Structure**

grouped_datasets/

│

├── dataset_of_10_images_each_car/

│   ├── car_1/

│   ├── car_2/

│   └── ...

├── dataset_of_7_images_each_car/

│   ├── car_3/

│   ├── car_4/

│   └── ...


**Conclusion**

This  provides a detailed explanation of the entire process I followed to create the ANPR dataset. 
From automated frame extraction to manual classification and final review, each step was crucial to 
ensuring the dataset met the required standards. The biggest challenges were dealing with multiple cars
in one frame and handling cars appearing under different conditions, but these were addressed through
manual filtering and consistent folder management. The final result is a well-organized dataset ready for use in ANPR development.

