from Files.CsvReader import CsvReader


class Characters:
    def __init__(self):
        self.reader = CsvReader()
        self.characters_csv_path = 'GameAssets/csv_logic/characters.csv'
        self.skins_csv_path = 'GameAssets/csv_logic/skins.csv'
        self.skin_confs_csv_path = 'GameAssets/csv_logic/skin_confs.csv'

        # Load all brawlers data once on initialization
        self.all_brawlers_raw_data = self.reader.readCsv(self.characters_csv_path)

    def get_all_brawlers_data(self):
        return self.all_brawlers_raw_data

    def get_brawlers_id(self):
        BrawlersID = []
        rowData = self.all_brawlers_raw_data

        if rowData:
            for i, row in enumerate(rowData):
                if i == 0:
                    continue

                if len(row) > 20 and row[20] == 'Hero' and \
                   len(row) > 2 and row[2].lower() != 'true' and \
                   len(row) > 1 and row[1].lower() != 'true':
                    BrawlersID.append(i) 
        return BrawlersID


    def get_brawler_by_skin_id(self, skin_id):
        skinsData = self.reader.readCsv(self.skins_csv_path)
        skinsConfsData = self.reader.readCsv(self.skin_confs_csv_path)
        charsData = self.all_brawlers_raw_data 

        if skinsData:
            skins_data_rows = skinsData[1:] if len(skinsData) > 1 else skinsData
            
            for i, row in enumerate(skins_data_rows):
                if 0 <= skin_id < len(skinsData):
                    
                    selected_skin_row = skinsData[skin_id]
                    if len(selected_skin_row) > 1:
                        conf = selected_skin_row[1]
                        if skinsConfsData:
                            skins_confs_data_rows = skinsConfsData[1:] if len(skinsConfsData) > 1 else skinsConfsData
                            for conf_row_idx, conf_row in enumerate(skins_confs_data_rows):
                                if len(conf_row) > 1 and conf_row[0] == conf: 
                                    brawler_item_name_from_conf = conf_row[1]
                                    if charsData:
                                        chars_data_rows = charsData[1:] if len(charsData) > 1 else charsData
                                        for char_i, char_row in enumerate(chars_data_rows):
                                            if len(char_row) > 0 and char_row[0] == brawler_item_name_from_conf:
                                                return char_i + (1 if len(charsData) > 1 else 0)
        return None