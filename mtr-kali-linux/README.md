kali-linux mtr GUI Open Problem:	[If you want to use cli mtr in kali-linux but by default mtr gui opens]
	sudo apt install mtr
	whereis mtr		[most probably the file location is /usr/bin/mtr. If not then change "/usr/bin/" to the output received]
	sudo cd /usr/bin
	sudo mv mtr mtr.BAK
	sudo wget https://files.catbox.moe/o6w0hc -O mtr		[Exracted from Ubuntu 22.04]
	sudo chmod +x mtr