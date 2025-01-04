
import os
import time
from picamera2 import Picamera2

REPO_PATH = "/home/BrownianMotion/gitrepo/CubeSat_BM"     #Your github repo path: ex. /home/pi/FlatSatChallenge
FOLDER_PATH = "/home/BrownianMotion/images/captured_image.jpg"   #Your image folder path in your GitHub repo: ex. /Images
def take_pic():
	picam2 = Picamera2()
	picam2.configure(picam2.create_still_configuration())
	save_path = os.path.expanduser("/home/BrownianMotion/images/captured_image.jpg")
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
        repo = Repo(REPO_PATH)
        origin = repo.remote('origin')
        print('added remote')
        origin.pull()
        print('pulled changes')
        repo.git.add(REPO_PATH + FOLDER_PATH)
        repo.index.commit('New Photo')
        print('made the commit')
        origin.push()
        print('pushed changes')
    except:
        print('Couldn\'t upload to git')

def main():
    take_pic()
    git_push()

if __name__ == '__main__':
    main()
