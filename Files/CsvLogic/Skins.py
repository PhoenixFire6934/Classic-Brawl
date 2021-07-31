from Files.CsvReader import CsvReader

class Skins:
    def get_skins_id(self):
        SkinsID = []
        reader = CsvReader()
        rowData = reader.readCsv('GameAssets/csv_logic/skins.csv')
        for row in rowData:
            SkinsID.append(rowData.index(row))

        return SkinsID