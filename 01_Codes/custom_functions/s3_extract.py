"""
To extract the Zip files from S3 Folder to local directory
"""
import zipfile
import os

def extract_s3_zip(file_name, temp=True):
    """
    Extract the Zip files from S3 Folder to local directory
    """
    #saving the current directory
    current_dir = os.getcwd()
    print("Initial Directory: ", current_dir)
    
    #changing the directory to the root directory for easier extraction
    os.chdir('/')
    print("Current Directory: ", os.getcwd())
    return None
    # if os.path.exists('aws_s3'):
    # if temp:
    #     dest_path = 
    # with zipfile.ZipFile(file_name+".zip", 'r') as zip_ref:
    #     zip_ref.extractall()
    # if temp:
    #     os.remove(file_name)
    # return None

if __name__ == '__main__':
    extract_s3_zip('aws_s3')