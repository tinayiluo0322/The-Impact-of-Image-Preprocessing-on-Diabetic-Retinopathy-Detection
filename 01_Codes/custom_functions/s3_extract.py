"""
To extract the Zip files from S3 Folder to local directory
"""

import zipfile
import os
import sys
import argparse


def extract_s3_zip(file_name, temp=True):
    """
    Extract the Zip files from S3 Folder to local directory
    """
    # saving the current directory
    current_dir = os.getcwd()
    temp_dir = current_dir
    print(f"Current Directory: {current_dir}")

    # changing the directory to the root directory for easier extraction
    # Navingating upto the "Diabetic-Retinopathy" directory
    while not temp_dir.endswith("Diabetic-Retinopathy"):
        # incase we are in a directory higher than the "Diabetic-Retinopathy" directory, break
        if "Diabetic-Retinopathy" not in temp_dir:
            print("Please navigate to the Diabetic-Retinopathy directory")
            return 0

        # move one directory up
        temp_dir = os.path.dirname(temp_dir)
    print(f"Changing Directory to: {temp_dir}")

    if not os.path.exists("aws_s3"):
        print(f"The aws_s3 directory does not exist, please download the data first")
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
    print(f"Changed Directory back to: {current_dir}")
    return None


def main():
    args = sys.argv[1:]
    parser = argparse.ArgumentParser(
        description="Extract the Zip files from S3 Folder to local directory"
    )
    parser.add_argument(
        "file_name",
        help="Name of the file to be extracted from the S3 Bucket, enter 'All' to extract all files",
    )
    parser.add_argument(
        "--temp",
        help="Whether to extract the files to the aws_s3 directory or the current directory",
        default=True,
    )

    args = parser.parse_args(args)
    if args.file_name == "All" or args.file_name == None:
        for i in os.listdir("aws_s3"):
            if ".zip" in i:
                extract_s3_zip(i, args.temp)
    else:
        for i in ["idrid", "messidor", "ddr"]:
            if i in args.file_name.lower():
                extract_s3_zip(args.file_name, args.temp)
                return None
        print("Please enter the correct file name: Idrid, Messidor, Ddr, All")

    return None


if __name__ == "__main__":
    # list of all zip files in the aws_s3 directory
    main()
