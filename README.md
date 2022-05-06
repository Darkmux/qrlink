# QRLink - Enlace a Código QR
Generator and converter of links to QR codes.
> This tool can be run on all Linux distributions.
## Preview in Termux
![QRLink](https://github.com/Darkmux/qrlink/blob/main/images/QRLink.jpg)
## QR Code Generated
![QRFacebook](https://github.com/Darkmux/qrlink/blob/main/images/facebook.png)
## Requirements
* Linux terminal
* Python3 installed
## Installation in Termux
> Update Termux repositories.
```bash
yes|pkg update && pkg upgrade
```
> Grant storage permissions to Termux.
```bash
termux-setup-storage
```
> Install "git" and "python3".
```bash
yes|pkg install git python
```
> Clone github repository.
```bash
git clone https://github.com/Darkmux/qrlink
```
> Access the cloned "qrlink" folder.
```bash
cd qrlink
```
> Grant execute permissions to all files with extension (.sh).
```bash
chmod 777 *.sh
```
> Install python3 modules.
```bash
python3 -m pip install -r requirements.txt
```
## Usage:
> Run the file, assign a link as the first argument and the path to save the image to as the second argument.
```bash
bash qrlink.sh <link> <path>
```
## Example:
```bash
bash qrlink.sh https://google.com /sdcard/google.png
```
## Or Usage:
> You can use the tool in the interactive console, to use it you just need to run the main file.
```bash
bash qrlink.sh
```
## Social Media Links
* [YouTube](https://youtube.com/channel/UCfMjNcFvJae_9g7wQI2W7EA)
* [Facebook](https://www.facebook.com/whitehacks00 "WHITE HACKS")
* [TikTok](https://tiktok.com/@whitehacks00 "WHITE HACKS")
* [Telegram](https://t.me/whitehacks00 "WHITE HACKS")
* [WhatsApp](https://wa.me/+593981480757 "Darkmux")
# Coded by: @Darkmux
# © WHITE HACKS
