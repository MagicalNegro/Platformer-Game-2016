import json

class Files:
    #Add a something to start new game

    #Call File with the Save File Path e.g. file = File(Save File Path)
    #Call the Save Procedure with the data and a name to refrence the data by e.g. Save (name, Data)
    #Call Load Function with the name that refrences the data to return a specfic piece of data from File e.g. Load(name)
    def __init__(self, path):
        self.__path = path
        try:
            self.__raw_data = self.__readJSONFromFile()
        except FileNotFoundError:
            #print("Save File not found")
            self.__raw_data = {}
            self.__writeJSONToFile(self.__raw_data)

    def Save(self, name, data):
        self.__raw_data[name] = data
        self.__writeJSONToFile(self.__raw_data)

    def Load(self, name):
        #self.raw_data = self.__readJSONFromFile()
        data = self.__raw_data.get(name)
        if data == None:
            #print("File Error: The Data your looking for was not found")
            return None
        else:
            return data
        return None

    def __writeJSONToFile(self, theData):
        fhw = open(self.__path, 'w')
        json.dump(theData, fhw)
        fhw.close()

    def __readJSONFromFile(self):
        fhr = open(self.__path, 'r')
        theData = json.load(fhr)
        fhr.close()
        return theData

savefile = Files("res/GameData.txt")
