# kali-linux remove mtr GUI:	
## If you want to use mtr in cli mode in kali-linux but by default mtr in gui mode opens.
Files extracted form Ubuntu 22.04
1. Install mtr using apt
```sh
sudo apt install mtr
```
2. Check mtr file location
```sh
whereis mtr
```
3. Change pwd to the file location found in Step: 2
> Note: most probably the file location is /usr/bin/mtr. If not then change "/usr/bin/" to the output received
```sh
sudo cd /usr/bin
```
4. Make Backup of the default mtr binary
```sh
sudo mv mtr mtr.BAK
```
5. Download and rename the cli version of mtr
```sh
sudo wget https://files.catbox.moe/o6w0hc -O mtr
```
6. Make it executable
```sh
sudo chmod +x mtr
```
