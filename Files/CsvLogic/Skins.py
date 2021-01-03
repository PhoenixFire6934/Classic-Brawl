import csv

class Skins:

    def get_skins_id():

        SkinsID = []

        with open('GameAssets/csv_logic/skins.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    SkinsID.append(line_count - 2)
                    line_count += 1


            return SkinsID


