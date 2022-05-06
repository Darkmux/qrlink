# QRLink - Enlace a Código QR
Generator and converter of links to QR codes.
> This tool can be run on all Linux distributions.
# Preview in Termux
![QRLink](https://github.com/Darkmux/qrlink/blob/main/images/QRLink.jpg)
# QR Code Generated
![QRFacebook](https://github.com/Darkmux/qrlink/blob/main/images/facebook.png)
# Requirements
* Linux terminal
* Python3 installed
# Installation in Termux
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
# Usage
> Run the file, assign a link as the first argument and the path to save the image to as the second argument.
```bash
bash qrlink.sh <link> <path>
```
