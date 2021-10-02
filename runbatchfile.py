import subprocess
import os

def directory():
    curr_dir = os.getcwd()
    return curr_dir


def runBlender():
    # subprocess.call([r'C:\\Users\\Mathilde\\OneDrive\\Dokumente\\hackathon2021\\renderfile1.bat'])
    subprocess.call([r'renderfile1.bat'])

