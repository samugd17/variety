# Installation of QRCreator

To access the contents of this application, clone this repository to your local storage. To do this, open your command terminal and insert this command:

```console
git clone https://github.com/samugd17/variety
```

## Linux 
For linux users, it is enough to have Python on your system and to have installed the [``qrcode``] dependency.

This is done with the following command:

```console
pip install "qrcode[pil]"
```

Once this is done, the only thing left to do is to run the application with Python:

```console
python qr.py
```

## Windows
For Windows users, I have converted the Python code into a `.exe` application, which executes the script by automatically opening the system command console and asking for all the data needed to generate the QR code. This will create the image in the same folder in which it was executed, giving then the option to repeat the process or terminate the program.

![WinShell](/QRCreator/img/qr_creator_windows.png)

If you have Python installed on your system, as in linux, you can also download the `.py` file and run it directly with Python itself after having installed the qrcode dependency.

```console
pip install "qrcode[pil]"
```

```console
python qr.py
```

### Useful links

- [pip](https://pip.pypa.io/en/stable/getting-started/)

- [qrcode](https://pypi.org/project/qrcode/)

- [auto-py-to-exe](https://github.com/brentvollebregt/auto-py-to-exe)