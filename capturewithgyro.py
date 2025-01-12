import os
import time
import subprocess
from picamera2 import Picamera2

REPO_PATH = "/home/BrownianMotion/gitrepo/CubeSat_BM"     #Your github repo path: ex. /home/pi/FlatSatChallenge
FOLDER_PATH = "/home/BrownianMotion/gitrepo/CubeSat_BM/captured_image1.jpg"   #Your image folder path in your GitHub repo: ex. /Images
def take_pic():
	picam2 = Picamera2()
	picam2.configure(picam2.create_still_configuration())
	save_path = os.path.expanduser(FOLDER_PATH)
	picam2.start()
	time.sleep(2)
	picam2.capture_file(save_path)
	picam2.stop()
	print("captured image")

def git_push():
    """
    This function is complete. Stages, commits, and pushes new images to your GitHub repo.
    """
    try:
        subprocess.run(["cd", REPO_PATH], shell=True, check=True)
        subprocess.run(["git", "add", FOLDER_PATH], check=True)
        subprocess.run(["git", "commit", "-m", "First image commit"], check=True)
        subprocess.run(["git", "push"], check=True)
        print('pushed changes')
    except:
        print('Couldn\'t upload to git')

def main():
    take_pic()
    git_push()

if __name__ == '__main__':
    main()
