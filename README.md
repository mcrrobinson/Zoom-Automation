# Zoom Automation

## Introduction
This application gets passed in the zoom links and times. It'll run constantly and once you should be attending a lecture it'll automatically join the lecture and start recording the screen in the coordinates of the lecture.

## Pre-run
Replace the filename "template_conf.py" to "conf.py", the template is there to give an idea on how the config file is meant to be layed out. Additionally change the encoding method in the file named ffmpeg_options. If you have a Nvidia graphics card you require: ```hevc_nvenc```, if you use AMD you need ```hevc_amf```.

## Usage
In order to use the application one must first install by running the command -
```
python main.py install
```
Running this will install the python packages required for the application. The contents are located in the requirements.txt file in the root of the file path. After all the configuration files are configured correctly. You can then run the application:
```
python main.py run
```
It'll then output in the console and saved to a debug file when attmepting to join a lecture. In the future this should be set to be a tray based application.
