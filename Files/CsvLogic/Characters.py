from Files.CsvReader import CsvReader


class Characters:
    def get_brawlers_id(self):
        BrawlersID = []
        reader = CsvReader()
        rowData = reader.readCsv('GameAssets/csv_logic/characters.csv')
        for row in rowData:
            if row[20] == 'Hero' and row[2].lower() != 'true' and row[1].lower() != 'true':
                BrawlersID.append(rowData.index(row))

        return BrawlersID


    def get_brawler_by_skin_id(self, skin_id):
        reader = CsvReader()
        charsData  = reader.readCsv('GameAssets/csv_logic/characters.csv')
        skinsData = reader.readCsv('GameAssets/csv_logic/skins.csv')
        skinsConfsData = reader.readCsv('GameAssets/csv_logic/skin_confs.csv')
        for row in skinsData:
            if skinsData.index(row) == skin_id:
                conf = row[1]
                for row in skinsConfsData:
                    if row[0] == conf:
                        brawler = row[1]
                        for row in charsData:
                            if row[0] == brawler:
                                return charsData.index(row)