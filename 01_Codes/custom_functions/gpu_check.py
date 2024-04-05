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
    except (
        Exception
    ):  # this command not being found can raise quite a few different errors depending on the configuration
        print("No Nvidia GPU in system!")
