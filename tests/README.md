# Description of Tests

### Third Kivy Example

- This is an example of using kivy to have multiple screens on one app and basic TextInput and Labels.

- This example has two components: kivy_third_test.py and third.kv.

	- kivy_third_test.py
		- Instantiates two separate screens
		- Instantiates the manager for those screens
		- Loads third.kv
		- Runs the application
		
	- third.kv
		- Associates the two separate screens with the screen manager
		- Defines the layout of the main screen
			- Label "Name" with text input beside it
			- Button to transition to the second screen
		
		- Defines the layout of the second screen
			- Just a button to transition back to the main screen


### OpenCV Video Test Example

- This is an example of using OpenCV image manipulation capabilities while capturing video from your screen.

- This example has only one component: video_test.py
    
    - First, it grabs a screenshot of your entire screen. It then converts it to a Numpy array because OpenCV only works with numpy arrays.
    - Then it applies a black-and-white filter to that image.
    - Finally, it displays the image in a window.
    - It will loop through this until the "q" key is pressed.