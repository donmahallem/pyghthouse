# Pyghthouse Examples

This is a loose collection of example scripts for pyghthouse.

Run any script by entering `python <filename>`.

Some scripts have additional dependencies; Check `README.md` in the repository root directory for an installation guide

If you set up config.py with your username and API token, you won't have to enter them every time you run a script.
Be aware that API tokens are only valid for a few days.

##### Beware:
Python imports search for the modules in the current folder and in installed packages. So, if you haven't installed 
pyghthouse as a package, you need to change the imports of the files in this folder to work.

In the repository root directory should be a file called `example.py`. This file shows the usage of imports of 
pyghthouse without having it installed as a package. 
Note: To use the imports the same way as `example.py`, your skript has to be in the same folder.

### Available functions
Here you can find a list of functions containing in this package.

`from_html(html_color)`
Converts an HTML color string like FF7F00 or #c0ffee to RGB

`from_hsv(h: float, s: float, v: float)`
Converts HSV (float values between 0 and 1) colors to RGB.

###### The class `Pyghthouse` with
`Pyghthouse(username: str, token: str, ...)`
Set up the `Pyghthouse` object. Needed arguments are `username` and `token`. Optional arguments and further explanation
can be found in the class definition (see `pyghthouse\ph.py`)

`Pyghthouse.empty_image()`
Creates a black image.
This function can also be called with an instance of the `Pyghthouse` object (*`<instance name>.empty_image()`*)

`<instance name>.set_image(image)`
Sends the given `image`.

`<instance name>.close()`
Closes the connection. 

*More functions can be found in `pyghthouse\ph.py`*