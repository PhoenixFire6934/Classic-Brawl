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
                    if row[5].lower() == '4' or row[5].lower() == '5':
                        CardSkillsID.append(line_count - 2)
                    line_count += 1


            return CardSkillsID



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