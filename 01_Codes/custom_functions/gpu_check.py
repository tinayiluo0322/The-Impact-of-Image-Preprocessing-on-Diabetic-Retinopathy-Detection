"""
To check if GPU is available or not
"""

import subprocess


def gpu_check():
    """
    Check if Nvidia GPU is available or not
    """
    try:
        subprocess.check_output("nvidia-smi")
        print("Nvidia GPU detected!")
        return 1
    except (
        Exception
    ):  # this command not being found can raise quite a few different errors depending on the configuration
        print("No Nvidia GPU in system!")
        return 0

def tf_version():
    """
    Check the version of Tensorflow
    """
    import tensorflow as tf
    print(tf.version.VERSION)
    print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
if __name__ == "__main__":
    if gpu_check():
        tf_version()
    pass
        
