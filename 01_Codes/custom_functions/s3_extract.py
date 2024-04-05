"""
To extract the Zip files from S3 Folder to local directory
"""

import zipfile
import os


def extract_s3_zip(file_name, temp=True):
    """
    Extract the Zip files from S3 Folder to local directory
    """
    # saving the current directory
    current_dir = os.getcwd()

    # changing the directory to the root directory for easier extraction
    os.chdir("/workspaces/Diabetic-Retinopathy")

    if not os.path.exists("aws_s3"):
        print(
            f"The aws_s3 directory does not exist, please download the data first using the s3_pull.sh script"
        )
        return None

    if ".zip" in file_name:
        file_name = file_name.split(".zip")[0]

    # creating the directory to extract the files
    if temp:
        dest_path = "aws_s3"
    else:
        # os.mkdir(file_name)
        dest_path = "./"

    source_path = "aws_s3/" + file_name + ".zip"

    with zipfile.ZipFile(source_path, "r") as zip_ref:
        zip_ref.extractall(dest_path)
    print(f"Extracted the files to {dest_path}")

    # Deleting the __MACOSX folder if it exists
    if os.path.exists(dest_path + "/__MACOSX"):
        os.system(f"rm -r {dest_path}/__MACOSX")

    os.chdir(current_dir)
    return None


if __name__ == "__main__":
    # list of all zip files in the aws_s3 directory
    for i in os.listdir("aws_s3"):
        if ".zip" in i:
            extract_s3_zip(i, True)
