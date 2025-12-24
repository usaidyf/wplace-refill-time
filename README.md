# Remaining Time

A simple script to calculate remaining time of Wplace paint charges refill.

## Create Standalone Executable (.exe)

To create a standalone `.exe` file, follow these steps:

1.  **Install PyInstaller**:
    ```bash
    pip install pyinstaller
    ```

2.  **Build the Executable**:
    Run the following command in your terminal:
    ```bash
    pyinstaller --onefile main.py
    ```

3.  **Locate the File**:
    The generated `.exe` file will be in the `dist` folder.

## Create a script to copy it to desired location

```
#!/bin/bash
source venv/Scripts/activate # Virtual environment should already exist
py -m pip install pyinstaller

pyinstaller --onefile main.py

rm -f "<path_to/desired_location/including/an_optional_custom_name>.py"
cp dist/main.exe "<path_to/desired_location/including/an_optional_custom_name>.py"
```
