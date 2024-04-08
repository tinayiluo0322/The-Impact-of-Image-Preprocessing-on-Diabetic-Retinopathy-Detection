"""
To Download the Zip files from the S3 Bucket to the local directory
input: The data to be downloaded from the S3 Bucket : Idrid, Messidor, Ddr
Output: The Zip files are downloaded to the local in the aws_s3 directory
"""

import os
import sys
import argparse


def download(data):
    # lower case the data
    data = data.lower()

    # making only the first letter of the data to be capital
    data = data.capitalize()

    # checking if zip is in the data name and removing it
    if "zip" in data:
        data = data.replace(".zip", "")

    if data not in ["Idrid", "Messidor", "Ddr"]:
        print("Please enter the correct data: Idrid, Messidor, Ddr")
        return 0

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
    print("Downloading Data")

    # downloading the data from the S3 Bucket
    os.system(
        f"aws s3 --no-sign-request sync s3://ml-diabetic-retinopathy/{data} aws_s3"
    )

    # changing the directory back to the original directory
    os.chdir(current_dir)
    print(f"Changed Directory back to: {current_dir}")
    return 1


def main():
    args = sys.argv[1:]
    parser = argparse.ArgumentParser(description="Download the data from the S3 Bucket")
    parser.add_argument(
        "data",
        type=str,
        help="The data to be downloaded from the S3 Bucket : Idrid, Messidor, Ddr",
    )
    args = parser.parse_args(args)
    x = download(args.data)
    if x == 1:
        print("The data has been downloaded successfully")
    else:
        print("No data has been downloaded")


if __name__ == "__main__":
    main()
