from Files.CsvReader import CsvReader

class Regions:
    def get_region_string(self, region_id):
        reader = CsvReader()
        rowData = reader.readCsv('GameAssets/csv_logic/regions.csv')
        for row in rowData:
            if rowData.index(row) == region_id:
                return row[0]