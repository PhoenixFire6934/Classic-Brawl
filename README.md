# Classic Brawl

Simple Brawl Stars v26.184 server emulator written in Python.

![Screenshot](screenshot.png) 

## Server Features

### Account System
- New player registration with unique ID and token
- All progress saved to MongoDB
- Multiplayer support — each player has independent data
- Full data loading on login (name, resources, brawlers, skins, records)

### Battle System
- **3v3 Battles with Bots** — full matches with rewards
- **Solo Showdown** — battle royale with 9 bots
- **Duo Showdown** — duo mode with bot teammate
- Trophy calculation based on match result and current rank
- Tokens (box currency) awarded after each battle
- Experience points earned and saved
- Battle result animations (trophies, tokens, experience)
- Brawler personal bests and global player records

### Gacha System (Boxes)
- **Brawl Box** (for tokens) — standard box
- **Big Box** (for tokens) — large box
- **Mega Box** (for gems) — mega box
- Brawler rarities: Common, Rare, Super Rare, Epic, Mythic, Legendary
- Different drop rates for each box type
- Trophy Road brawlers excluded from boxes and shop

### Shop
- Buy boxes for gems (Big Box, Mega Box)
- Buy gold for gems
- Buy token doubler
- Special offers with skins, brawlers, and resources

### Player Profile
- View your own profile (trophies, records, brawlers)
- Statistics: experience level, trophies
- Profile icon and name color

### Customization
- Change name
- Select profile icon
- Select name color
- Select brawler skins
- Last selected brawler and skin saved between sessions

### Progress Saving
- All data saved to MongoDB
- Persists between sessions: selected brawler, skin, resources, trophies
- Survives server restarts

### Technical Features
- Configurable `config.json` (starting resources, region, theme)
- Configurable `shop.json` (offers, prices) - static offers
- Configurable `events.json` (game events) - WIP
- IP ban system
- Maintenance mode

---

### Requirements:
- Python 3.7 or higher
- pymongo
- dnspython
- colorama

### MongoDB configuration
First you'll need to put your MongoDB connection string in `config.json`. If you don't know how to get it here's a quick tutorial: https://imgur.com/a/oXI34dA

### Running the server
In a terminal, type __`pip install -r requirements.txt`__ then __`python main.py`__

### Configuring the client app
To connect to your server, a **patched client** is required. 
Download this [base APK](https://mega.nz/file/zDQzDYyB#V7GkrTFQpTfhTk_gOroMfdps5VFl8Lnn-CBX-bbnjlw) and change the IP in `libcb.config.so`, if you want to use Classic Brawl locally on your device, you can use "127.0.0.1" as the IP. If not, then you can use your device's IPv4 address. 

#### The APK was recently updated to support Android 13+ and Emulators.

---

### Need help?
Join us on [Discord](https://discord.gg/9rQPMTfJgt)

### Credits
- [athemm](https://github.com/athemm) - for making the patcher.
- [PhoenixFire](https://github.com/PhoenixFire6934) - the creator of Classic Brawl
- [CrazorTheCat](https://github.com/CrazorTheCat) - Contributor and other versions developer
- [8-bitHacc](https://github.com/8-bitHacc) - Contributor & Developer of new features
- [Asperrion](https://github.com/Asperrion) - Developer of new features