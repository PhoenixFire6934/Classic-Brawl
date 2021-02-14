import csv

class Characters:

    def get_brawlers_id():

        BrawlersID = []

        with open('GameAssets/csv_logic/characters.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[20] == 'Hero' and row[2].lower() != 'true' and row[1].lower() != 'true' and row[0] != "SpawnerDude":
                        BrawlersID.append(line_count - 2)
                    line_count += 1


            return BrawlersID


    
    def get_brawler_by_skin_id(self, skin_id):
        skins_file =  open('GameAssets/csv_logic/skins.csv')
        csv_reader = csv.reader(skins_file, delimiter=',')
        line_count = 0
        print(skin_id)

        for row in csv_reader:

            if line_count == 0 or line_count == 1:
                line_count += 1
            else:
                line_count += 1
                if line_count == skin_id + 3:
                    conf = row[1]
                    line_count += 1

                    sconf_file = open('GameAssets/csv_logic/skin_confs.csv')
                    csv_reader = csv.reader(sconf_file, delimiter=',')
                    line_count = 0

                    for row in csv_reader:
                        if row[0] == conf:
                            brawler = row[1]

                            char_file = open('GameAssets/csv_logic/characters.csv')
                            csv_reader = csv.reader(char_file, delimiter=',')
                            line_count = 0

                            for row in csv_reader:
                                if line_count == 0 or line_count == 1:
                                    line_count += 1
                                else:
                                    line_count += 1
                                    if row[0] == brawler:
                                        id = line_count - 3

                                        skins_file.close()
                                        sconf_file.close()
                                        char_file.close()

                                        return id


