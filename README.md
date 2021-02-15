<h1 align="center">Welcome to Classic-Brawl 👋</h1>

Open source Brawl Stars server emulator for version 20 of the game!


![ScreenShot](https://media.discordapp.net/attachments/711412740199022603/810659435285315625/Screenshot_20210214-185101_Brawl_Stars.png) 


## What's working ?
- Battles
  - Trophies in offline battles
- Home
  - Unlimited resources
  - Brawlers from boxes  
  - All skins unlocked
  - Star Powers
- Shop
  - Special offers
  - Boxes
  - Gold and other resources 
- Club
  - Join
  - Leave
  - Chat
  - Update settings
  - Bot commands

...and much more!


## Prerequisites

- python 3.7




## Run Server
- On Windows:
    - Download Python 3.7 or newer version from official page.
    - Download the server and extract it.
    - In a terminal type: ```pip install tinydb```
    - Execute "main.py" file
- On Linux:
    - Open Terminal and install Python by executing following command:
    ```sudo apt-get update && sudo apt-get install python3 python3-pip```
    - Download the server and extract it.
    - In a terminal type: ```pip install tinydb```
    - Execute "main.py" file
- On Android:
    - Download and install PyDroid app from Google Play.
    - Open PyDroid and wait until Python installs.
    - Download the server and extract it.
    - In PyDroid go in the "pip" section, type ```tinydb```, then click install.
    - In PyDroid open and execute "main.py" file


## Configure client
To connect to your server, you need a custom client. Here the only solution is to use a [pre-made client](http://download1644.mediafire.com/a1ut3eusl3ig/r6cph3wgimtvvqs/Brawl+Stars_24.142.apk). Just replace the IP in the frida-gadget config with yours (```/lib/armeabi-v7a/libgg.config.so```) ```{"interaction":{"interaction":{"type":"script","path":"libscript.so","on_change":"reload","parameters":{"redirectHost":"YOUR_IP"}}}```




#### Need help? Join [our Discord support server](https://discord.gg/2t4QXyuSKW)




## Authors

👤 **PhoenixFire** (main developer)

* Github: [@PhoenixFire6879](https://github.com/PhoenixFire6879)
* Discord: PhoenixFire#6879

👤 **Crazor**

* Github: [@CrazorCLB](https://github.com/CrazorCLB)
* Discord: Crazor#7395

Special thanks to:
- [VitalikObject](https://github.com/VitalikObject)
- [Rostik](https://github.com/RostikDevv) and [Vorono4ka](https://github.com/Vorono4ka) for their [scdocs](https://github.com/RostikDevv/scdocs)


## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/PhoenixFire6879/Classic-Brawl/issues).

## Show your support

Give a ⭐️ if this project helped you!
