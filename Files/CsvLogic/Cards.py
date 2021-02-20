import csv

class Cards:

    def get_spg_id():

        CardSkillsID = []

        with open('GameAssets/csv_logic/cards.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[5].lower() == '4' or row[4].lower() != 'true':
                        CardSkillsID.append(line_count - 2)
                    line_count += 1


            return CardSkillsID


    def get_spg_by_brawler_id(self, brawler_id, type):
        char_file =  open('GameAssets/csv_logic/characters.csv')
        csv_reader = csv.reader(char_file, delimiter=',')
        line_count = 0

        for row in csv_reader:
            if line_count == 0 or line_count == 1:
                line_count += 1
            else:
                line_count += 1
                if line_count == brawler_id + 3:
                    name = row[0]
                    line_count += 1

                    cards_file = open('GameAssets/csv_logic/cards.csv')
                    csv_reader = csv.reader(cards_file, delimiter=',')
                    line_count = 0

                    for row in csv_reader:
                        if line_count == 0 or line_count == 1:
                            line_count += 1
                        else:
                            line_count += 1
                            if type == 4:
                                if row[5].lower() == '4' and row[3] == name:
                                    id = line_count - 3
                                    char_file.close()
                                    cards_file.close()
                                    return id

                            elif type == 5:
                                if row[3] == name and row[5].lower() == '5':
                                    id = line_count - 3
                                    char_file.close()
                                    cards_file.close()
                                    return id


    def get_unlocked_spg(self, brawler_id):
        char_file =  open('GameAssets/csv_logic/characters.csv')
        csv_reader = csv.reader(char_file, delimiter=',')
        line_count = 0
        id = []

        for row in csv_reader:
            if line_count == 0 or line_count == 1:
                line_count += 1
            else:
                line_count += 1
                if line_count == brawler_id + 3:
                    name = row[0]
                    line_count += 1

                    cards_file = open('GameAssets/csv_logic/cards.csv')
                    csv_reader = csv.reader(cards_file, delimiter=',')
                    line_count = 0

                    for row in csv_reader:
                        if line_count == 0 or line_count == 1:
                            line_count += 1
                        else:
                            line_count += 1
                            if row[5].lower() == '4' and row[3] == name and row[4] != "true":
                                id.append(line_count - 3)

                    return id
                    char_file.close()
                    cards_file.close()


    def get_brawler_unlock():

        CardUnlockID = []

        with open('GameAssets/csv_logic/cards.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[5].lower() == '0':
                        CardUnlockID.append(line_count - 2)
                    line_count += 1


            return CardUnlockID