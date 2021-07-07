<h1 align="center">Welcome to Classic-Brawl 👋</h1>

Open source Brawl Stars server emulator for version 26 of the game!


![ScreenShot](https://cdn.discordapp.com/attachments/704364452891590778/789482341209866280/Screenshot_20201218-151815_Brawl_Client.jpg) 


## What's working ?
- Battles
  - Trophies in offline battles
- Home
  - Unlimited resources
  - Brawlers from boxes  
  - All skins unlocked
  - Gadgets and Star Powers
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
To connect to your server, you need a custom client APK:
- [v26.165](https://mega.nz/file/iGIGkT7S#PnbYOskUa0PGtbry4dcK1ugViwRsbGiDzP92i39KvH4)
- [v26.184](https://mega.nz/file/XeBTXCBB#BN6B9-FcMqn19w6SkgxVgShFwWx1Qb55tgydIL1oLDI)

You'll have to replace the IP in the frida-gadget config with yours (```/lib/armeabi-v7a/libcb.config.so```) ```{"interaction":{"interaction":{"type":"script","path":"libcb.script.so","on_change":"reload","parameters":{"redirectHost":"YOUR_IP"}}}```







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
