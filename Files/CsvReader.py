import csv

class CsvReader:
    def readCsv(self, filename):
        self.rowData = []
        self.lineCount = 0
        with open(filename) as csvFile:
            self.csvReader = csv.reader(csvFile, delimiter=',')
            for row in self.csvReader:
                if self.lineCount == 0 or self.lineCount == 1:
                    self.lineCount += 1
                else:
                    self.rowData.append(row)
                    self.lineCount += 1
        return self.rowData
