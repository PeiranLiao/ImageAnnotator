# Image Annotator


## Introduction

This is an image captioning annotation project designed for annotating images with 5 descriptive sentences. The software allows users to open an image folder, annotate each image with 5 captions, and save the information in a JSON file format. This README file provides guidance on how to use the software and its features.

## Installation

Before running the software, make sure you have the required packages and dependencies installed. Navigate to the software directory and run the following command to install the necessary packages:

```
pip install -r requirements.txt
```

## Usage

To start using the software, follow the steps below:

1. Launch the software by executing the following command:

```
python ImageAnnotator.py
```

2. The software's interface will open, the screenshot is shown below. Click on "Browse Path" and navigate to the images you wish to annotate.

   ![ScreenShot](https://github.com/PeiranLiao/ImageAnnotator/blob/main/ScreenShot/ScreenShot.png)

3. Once the image is selected, the image will be displayed. Next to the image, you will find 5 input fields to enter the captions. Write your captions in these fields.

4. After finishing the annotation for the first image, click the "Save Captions" button to save the captions in a JSON file format, and you can click the "Next Image" or "Previous Image" button to move to the next or previous image in the folder.(Clicking "Next/Previous Image" button will also save the captions!)

5. The JSON file will be saved at  `./Annotation/` . The JSON file will have the following structure:

```
[
    {
        "image_name": "example_image_1.jpg",
        "captions": [
            {
                "caption_id": 0,
                "caption": "Caption 1_1"
            },
            {
                "caption_id": 1,
                "caption": "Caption 1_2"
            },
            {
                "caption_id": 2,
                "caption": "Caption 1_3"
            },
            {
                "caption_id": 3,
                "caption": "Caption 1_4"
            },
            {
                "caption_id": 4,
                "caption": "Caption 1_5"
            }
        ]
    }
    {
        "image_name": "example_image_2.jpg",
        "captions": [
            {
                "caption_id": 0,
                "caption": "Caption 2_1"
            },
            {
                "caption_id": 1,
                "caption": "Caption 2_2"
            },
            {
                "caption_id": 2,
                "caption": "Caption 2_3"
            },
            {
                "caption_id": 3,
                "caption": "Caption 2_4"
            },
            {
                "caption_id": 4,
                "caption": "Caption 2_5"
            }
        ]
    }
]
```

## Support

If you encounter any issues or have questions about the usage of the software, please feel free to open an issue on the GitHub repository or contact the developers via email.

## License

This software is provided under the MIT License. Please refer to the [LICENSE](LICENSE) file for more information.
