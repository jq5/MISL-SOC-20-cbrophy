# MISL-SOC-20-cbrophy

My project that I am working on over the duration of MISL-SOC-2020 is "**Image Processing with Facial Recognition**".

## Description

    - My language that I will be using is *Python* and I will be using *Kivy*, *Buildozer* and *OpenCV*.
    
    - Kivy is a Python library for developing applications on multiple platforms such as Android, IOS, Linux and Windows. 
    - Buildozer is tool to package mobile applications on Android and IOS easily. 
    - OpenCV is a real-time, open-source computer vision and machine-learning library.
    
    - I chose to use Kivy because it's a Python library which is my preferred language currently and it is really easy to pick up and use.
    - I chose to use Buildozer because it was recommended on the Kivy documentation and doesn't seem too complicated.
    - I chose to use OpenCV because it has a easy-to-understand documentation and many tutorials.
    
    - I want to use these tools to create a Android application with facial recognition and put different filters over the subject.

## Installation

My Dad helped me through the installation process.

### Anaconda:
    - Download Anaconda so you can create environments with their own seperate packages and python versions. https://docs.anaconda.com/anaconda/install/
    - I Initially downloaded Anaconda seperately for both Python 2.7 and 3.7+ thinking I needed to use Python 2.7 but realised later on that I only needed the version for Python 3.7+.
    
    - Since I am using **Windows 10**, I followed the "*Installing on Windows*" guide.
    - I installed **for ALL users** because I just prefer to have access, even if restricted, to any program on all accounts on my computer. 
    - I also checked the option of **Add Anaconda3 to my Path environment variable** seeing as there was problems with libraries not being found if we didn't. 
    
    - To create, activate, deactivate and switch between environments in Anaconda, I followed this guide: https://docs.anaconda.com/anaconda/user-guide/tasks/switch-environment/

### OpenCV:
    - The tutorial I followed is for Python 2.7, however, following the same steps works for 3.7+.
    - I followed the steps from *Installing OpenCV from prebuilt binaries* from https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html

### Kivy:
    - Kivy only works in Python3 versions 3.5 to 3.7. I had to reinstall all my packages on a new virtual environment which was in python 3.7.7 instead of 3.8.3.
    - I followed the steps *Installing the kivy stable release* from https://kivy.org/doc/stable/installation/installation-windows.html#install-win-dist
	- Just running "pip install kivy" won't work on it's own, you have to folow the above or similar guide.

## Creating and Running Programs/Apps

### To create programs:
    - I am using PyCharm as my IDE for my programs because: 
        - Git is integrated into it 
        - Has a helpful project view to show all your files
        - Can run different projects from specific environments with out much modification.
        
    - Running programs is easy with PyCharm:
        - See tests/README.md for a descriptive tutorial on running programs on PyCharm.

### To build and run APK's on your device:
    - I am using *buildozer* which is **Linux-only** so I used *WSL (Windows Subsystem for Linux)* to run it. https://kivy.org/doc/stable/guide/packaging-android.html
    - The same commands can be applied with minor changes (such as "yum" instead of "apt-get") to any other Linux distribution.
    
    - Install dependencies (Ubuntu and WSL): 
        - Run "sudo apt-get update && sudo apt-get install python3 python3-pip git cython".
        - And "sudo pip3 install cython".
        
        - Run "git clone https://github.com/kivy/buildozer.git" in /home/user or whatever directory you want to save your buildozer files in.
        - Then "cd buildozer"
        - Finally, "sudo python3 setup.py install". Make sure it is **python3** not just **python** or it won't work.

### To copy files in any drive on your computer to WSL:
	- Use "cd /" to go to the base directory of WSL.
	- "cd mnt" to go into a mount point of Windows 10.
	- Then, you can choose your drive, find your file and use the "cp" command to copy it
		- Example: "sudo cp /mnt/c/Users/chris/Documents/data.txt /home/chris"
		- sudo means "super user do" like "Running as Administrator" on Windows.
		- cp is the copy command
		- /mnt/... is the location of the data I want to copy
		- /home/chris is where I want to copy my files to.
		
### To build, push and run the APK on your Android Device:
	- Installing ADB (Android Debug Bridge)
		- The ADB lets your computer connect to your computer and have software pushed straight to it from command-line.
		
		- WSL/Windows 10:
			- WSL can't access your device from USB ports but can still have the ADB installed.
				- To bypass this, we get the same version ADB on Windows 10 as well as on WSL.
				- If you use a Linux system anyway, then this isn't an issue.
			
			- I followed this tutorial for installing Windows 10 ADB:  https://www.auslogics.com/en/articles/install-adb-driver-on-windows-10/
			- Installing ADB on WSL: http://defrances.co/post/adbwsl/
			- I had previously tried installing ADB drivers for my device previously that caused it to not be found. To rectify this, I uninstalled the device in *Device Manager*.
		
		- Linux (Ubuntu):
			- Installing adb on Ubuntu 20.04 is really simple.
			- Run "sudo apt-get android-tools-adb"
		
		- Run "adb devices" on both Windows 10 CMD and WSL to make sure it works.
	
	- Pushing APK
		- Navigate into the directory containing your project files.
		- Run "sudo buildozer init". This creates "buildozer.spec".
		- Run "sudo nano buildozer.spec" and customise properties such as the name to your liking.
		- Run "sudo buildozer android debug deploy run" to build, push and run the APK on your Android device.
		