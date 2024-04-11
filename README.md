# ML Final Project

[![CI](https://github.com/nogibjj/Diabetic-Retinopathy/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Diabetic-Retinopathy/actions/workflows/cicd.yml)


## 1. Instructions

### 1.0 Set Up Bash

```bash
bash setup.sh
```

### 1.1 Downloading Data from AWS

Option 1: Downloading Data from AWS using the ``s3_download.py`` script
This will download indvidual files from the AWS S3 bucket folder.

run the s3_download.py script using the following command:
```bash
python3  ./01_Codes/custom_functions/s3_download.py <Data Name>
```
The Data Name can be one of the following:
- Messidor_Raw
- Messidor_Resized
- Idrid
- Ddr

Option 2: Downloading Data from AWS using the ``s3_pull.sh`` script
This will download all the files from the AWS S3 bucket folder.

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
it temp is set to False, the files will be extracted to the project root directory and will be tracked by git which is not recommended.

**Recomended Usage**:

```bash
python3  ./01_Codes/custom_functions/s3_extract.py All
```
