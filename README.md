# Classic Brawl

Simple Brawl Stars v26.184 server emulator written in Python.

![ScreenShot](https://cdn.discordapp.com/attachments/704364452891590778/789482341209866280/Screenshot_20201218-151815_Brawl_Client.jpg) 

### Requirements:
- Python 3.7 or higher
- pymongo
- dnspython
- colorama

### MongoDB configuration
First you'll need to put your MongoDB connection string in `config.json`. If you don't know how to get it here's a quick tutorial https://imgur.com/a/3kKedyy

### Running the server
In a terminal, type __`pip install -r requirements.txt`__ then __`python main.py`__

### Configuring the client app
To connect to your server, a **patched client** is required. 
Download this [base APK](https://mega.nz/file/OL5SAD6Q#70_56frFtBDO5DC-g1qOzuzFv4txx_rT6Sr4m49-0NA) and change the IP in `libcb.config.so`

### Need help?
Open an issue or contact me on **Discord**: PhoenixFire#6879

### Special thanks
- [athemm](https://github.com/athemm) - for making the patcher.
