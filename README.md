# Quick-Calc
## A simple calculator app with Tkinter UI and basic functionality
The program provides a minimal interface with all the basic functionality of a smile calculator program.
The program allows to input to variables via keyboard and then get the result for addition, subtraction, multiplication or division.
The program also allows to clear every entry and set it to zero.
## Setup instructions
To run this program you'll need to install python 3.12 or later, pip, tkinter package, and pytest for the testing capabilities.
### For Windows:
```
winget search --id Python.Python
winget install Python.Python.3 --scope machine
C:> py -m ensurepip --upgrade
pip install tkinter
pip install pytest
```
Or by downloading the packages from the official Python website and package repositories.
### For Linux (e.g. Ubuntu):
```
sudo apt install python3
python -m ensurepip --upgrade
pip install tkinter
pip install pytest
```
After you've installed Python 3 and all program dependencies, the program can be run either via
a python IDE like WingIDE, PyCharm, VS Code, or by (on Windows) double-clicking the calc_ui.py file.

## Testing Instructions
To run the tests, you need to set up the virtual python environment, and run the command:
```
pytest
```
## Testing Framework
For this project pytest was chosen as the testing framework as it allows for an easy setup process, straightforward test code,
and robust performance. Moreover, the pytest command allows for a very easy way to run the tests and see the results immediately.

Unittest on the other hand, would allow for not relying on a third-party package, as it's built-in into Python. However,
the test code for unittest is too complicated for a project of this scope and would make the development and testing longer.

For this project pytest fits better as it's more lightweight, and easier to manage as the testing framework.