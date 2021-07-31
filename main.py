from os import system
from Core.Networking.Server import Server

def main():
    system("title " + "BrawlStars Server Emulator")

    print(r"""
__________                      .__      _________ __                       
\______   \____________ __  _  _|  |    /   _____//  |______ _______  ______
 |    |  _/\_  __ \__  \\ \/ \/ /  |    \_____  \\   __\__  \\_  __ \/  ___/
 |    |   \ |  | \// __ \\     /|  |__  /        \|  |  / __ \|  | \/\___ \ 
 |______  / |__|  (____  /\/\_/ |____/ /_______  /|__| (____  /__|  /____  >
        \/             \/                      \/           \/           \/     

    """)

    Server("0.0.0.0", 9339).start()



if __name__ == '__main__':
    main()