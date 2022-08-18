[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)



##
# ChaosKobra 🐍
Another Sub-Domain Enumeration Tools for normies written in Python3.

### 🔧 Technologies & Tools

![](https://img.shields.io/badge/OS-Linux-informational?style=flat-square&logo=kali-linux&logoColor=white&color=5194f0&bgcolor=110d17)
![](https://img.shields.io/badge/Editor-VS_Code-informational?style=flat-square&logo=visual-studio&logoColor=white&color=5194f0)
![](https://img.shields.io/badge/Language-python-informational?style=flat-square&logo=python&logoColor=white&color=5194f0&bgcolor=110d17)
![](https://img.shields.io/badge/Python_Version-3.10-informational?style=flat-square&logo=python&logoColor=white&color=5194f0&bgcolor=110d17)

##

### 📚 Requirements
> - Python 3.9+
> - pip3

##

### Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.
if not installed, install it using the following command.
```bash
sudo apt-get install python3-pip
```

> It is advised to install the python requirements in a virtual environment, for that install the venv package.

```bash
    python3 -m pip install venv
    python3 -m venv env
    source env/bin/activate
```
After that run the following commands:
```bash
    python3 -m pip install -r requirements.txt
    sudo python3 setup.py
```
##

### Usage

```bash
python3 main.py -t [domain] -o (Output File)
```
##

### Options

```bash
                -t              Target or Host
                -o              Output Folder (Optional)
```

##

### Example
```bash
1) python3 main.py -t example.com
2) python3 main.py -t example.com -o example
```
> Note: if **-o** is not provided the output folder name is set to the target(DOMAIN).

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
