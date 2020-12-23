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
                    if row[20] == 'Hero' and row[2].lower() != 'true' and row[1].lower() != 'true':
                        BrawlersID.append(line_count - 2)
                    line_count += 1

            return BrawlersID