# MISL-SOC-20-cbrophy

My project that I am working on over the duration of MISL-SOC-2020 is "**Image Processing with Facial Recognition**".

# Description

- My language that I will be using is *Python* and I will be using *Kivy* and *OpenCV*.
- OpenCV is a real-time, open-source computer vision and machine-learning library.

- I want to use these tools to create a mobile phone application with facial recognition and put different filters on top.

# Installation

My Dad helped me through the installation process.

### Anaconda

- Download Anaconda so you can create environments with their own seperate packages and python versions. https://docs.anaconda.com/anaconda/install/
- I Initially downloaded Anaconda seperately for both Python 2.7 and 3.7+ thinking I needed to use Python 2.7 but realised later on that I only needed the version for Python 3.7+.

- Since I am using **Windows 10**, I followed the "*Installing on Windows*" guide.
- I installed **for ALL users** because I just prefer to have access, even if restricted, to any program on all accounts on my computer. 
- I also checked the option of **Add Anaconda3 to my Path environment variable** seeing as there was problems with libraries not being found if we didn't. 

- To create, activate, deactivate and switch between environments in Anaconda, I followed this guide: https://docs.anaconda.com/anaconda/user-guide/tasks/switch-environment/

### Installing OpenCV

- The tutorial I followed is for Python 2.7, however, following the same steps works for 3.7+.
- I followed the steps from *Installing OpenCV from prebuilt binaries* from https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html

### Installing Kivy
- Kivy only works in Python3 versions 3.5 to 3.7. I had to reinstall all my packages on a new virtual environment which was in python 3.7.7 instead of 3.8.3.
- I followed the steps *Installing the kivy stable release* from https://kivy.org/doc/stable/installation/installation-windows.html#install-win-dist

### Creating and Running Programs

- I am using PyCharm as my IDE for my programs because: 
	- Git is integrated into it 
	- Has a helpful project view to show all your files
	- Can run different projects from specific environments with out much modification.
	
- Running programs is easy with PyCharm:
	- "Run -> Run -> *MyProgram.py*"

### Creating APK's for your device

- I am using *bulldozer* which is Linux-only so I used WSL or Windows Subsystem for Linux to run it.