# MISL-SOC-20-cbrophy

- My project that I am working on over the duration of MISL-SOC-2020 is "**Image Processing with Facial Recognition**".

# Description

- My language that I will be using is *Python* and I will be using a library named *OpenCV*.
- OpenCV is a real-time, open-source computer vision and machine-learning library.

- I want to use these tools to create a mobile phone application with facial recognition and put different filters on top.

# Installation

- My Dad helped me through the installation progress.

### Anaconda

- Download Anaconda so you can create environments with their own seperate packages and python versions. https://docs.anaconda.com/anaconda/install/
- I Initially downloaded Anaconda seperately for both Python 2.7 and 3.7+ thinking I needed to use Python 2.7 but realised later on that I only needed the version for Python 3.7+.

- Since I am using **Windows 10**, I followed the "*Installing on Windows*" guide.
- I installed **for ALL users** because I just prefer to have access, even if restricted, to any program on all accounts on my computer. 
- I also checked the option of **Add Anaconda3 to my Path environment variable** seeing as there was problems with libraries not being found if we didn't. 

- To create, activate, deactivate and switch between environments in Anaconda, I followed this guide: https://docs.anaconda.com/anaconda/user-guide/tasks/switch-environment/

### Creating and Running Programs

- I used Python's *IDLE* as my desired editor for my programs but it doesn't really matter what you use.

- I always ran my code by opening a *Command Prompt* and activating the desired environment, which for me was "py3" for Python v3.8.3 from the previous tutorial. 
Then, I navigated into the directory that contained my desired program and ran **python build.py** (replace build.py with whatever your program is called.) 

### Problems

- Running code through a pre-existing install of Python's *IDLE* means that you will only have the packages installed to **that environment**, so any other packages installed in an Anaconda environment won't be used.
- There was also a problem of libraries still not being found if ran a program through an Anaconda environment, unless I added Anaconda3 to the PATH variable during installation.
