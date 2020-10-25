# Zoom Automation

## Pre-run
Replace the filename "template_conf.py" to "conf.py", the template is there to give an idea on how the config file is meant to be layed out. Additionally change the encoding method in the file named ffmpeg_options. If you have a Nvidia graphics card you require: ```hevc_nvenc```, if you use AMD you need ```hevc_amf```.

## Usage
In order to use the application one must first install by running the command -
```
python main.py install
```
Running this will install the python packages required for the application. The contents are located in the requirements.txt file in the root of the file path.
