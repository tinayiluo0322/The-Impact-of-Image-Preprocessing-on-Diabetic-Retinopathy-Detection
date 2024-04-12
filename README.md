# ML Final Project

[![CI](https://github.com/nogibjj/Diabetic-Retinopathy/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Diabetic-Retinopathy/actions/workflows/cicd.yml)


## 1. Instructions

### 1.1 Downloading Data from AWS

#### Option 1: Downloading Data from AWS using the ``s3_download.py`` script
This will download the Selected folder from the AWS S3 bucket.

run the s3_download.py script using the following command:
```bash
python3  ./01_Codes/custom_functions/s3_download.py <Data Name>
```

The {Data Name} can be constructed using the following levels, as required, separated by a '/':

A. The Base Folders are:
- Messidor
- Idrid
- Ddr

B. The Subfolders Within Messidor and Idrid are:
- {Messidor/Idrid}_Raw.zip : The Raw Images, Big in Size **DON'T** download unless needed
- Resized_512 : Images Resized to 512x512 for use with CNN512
- Resized_224 : Images Resized to 224x224 for use with EfficientNetB0

C. Within the Resized_XXX folders, there will be 4 files, all of them will be of size (XXX, XXX):
- {Messidor/Idrid}_XXX_CN.zip : Color Normalized
- {Messidor/Idrid}_XXX_IENR.zip : Image Enhancement and Noise Reduction
- {Messidor/Idrid}_XXX_Crop.zip : Cropped Images
- {Messidor/Idrid}_XXX_Raw.zip : Only Resized Images

I would suggest to download at the level of the Resized_XXX folders, so that we don't download the large raw images and we get the 4 files required to run our part of the project.

**Recomended Usage**: Run this in the terminal from the project root directory.

```bash
python3  ./01_Codes/custom_functions/s3_download.py {Data}/Resized_{Size}/
```

- Data: Messidor or Idrid
- Size: 512 or 224

This will download the 4 files to the aws_s3 folder in the project root directory.


#### Option 2: Downloading Data from AWS using the ``s3_pull.sh`` script
This will download all the files from the AWS S3 bucket folder. this is **NOT** recommended as it will download all the files from the AWS S3 bucket.

run the s3_pull.sh script from the home directory using the following command:
```bash
bash s3_pull.sh
```

**Note**: It is recomended to download the data using the s3_downlaod script so that only the required data is downloaded, else it will take a long time to download all the data if you are not planning to use all of it.

### 1.2 Downloaded Data Extraction

use the s3_extract funtion to extract the downloaded data, this will extract from the zip file and save the data in regular folders.

- In case no file is specified, it will extract all the zip files in the aws_s3 folder.
- In case no arguement is passed for the temp variable, by default it will extract the files within the aws_s3 folder.

It is recommended to keep the temp variable as True, so that the files are extracted within the aws_s3 folder which is not tracked by git.      
if temp is set to False, the files will be extracted to the project root directory and will be tracked by git which is not recommended.

**Recomended Usage**:

```bash
python3  ./01_Codes/custom_functions/s3_extract.py All
```

### 1.3 Tensorflow

execute the following command in the terminal so that you will avoid the error of "Failed Copying Input Tensor"

```bash
export PATH="${PATH}:/usr/local/nvidia/bin:/usr/local/cuda/bin"
```

