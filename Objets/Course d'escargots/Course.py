class Escargot :
    def __init__ (self, name, look, distance, motivation, endurance)
        self.__nom = name
        self.__apparence = look
        self.__distanceParcourue = distance
        self.__motive = motivation
        self.__end = endurance
    def getName(self):
        return self.nom
    def getLook(self) :
        return self.apparence
    def getDistance(self) :
        return self.distanceParcourue
    def move(self) :
        return self.motive
    def tired(self):
        return self.end

escargot1 = Escargot("Joe", , ) 
escargot2 = 