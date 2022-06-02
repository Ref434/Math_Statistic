import csv

# class which provide all managment with data loading
class DataManager:
    def __init__(self):
        return

    def loadCsvFloat(self, fileName : str, offset : int):
        data = []
        offsetCounter = 0

        with open(fileName) as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            for row in reader:
                if offsetCounter < offset:
                    offsetCounter += 1
                    continue
                data.append([float(row[i]) for i in range(len(row))])

        return data

    def loadData(self, fileName : str, offset : int):
        return self.loadCsvFloat(fileName, offset)
