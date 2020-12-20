import sys
import logging.config

class LetraDni:
    digits = 0
    mod_to_letter = {
        "0" : "T",
        "1" : "R",
        "2" : "W",
        "3" : "A",
        "4" : "G",
        "5" : "M",
        "6" : "Y",
        "7" : "F",
        "8" : "P",
        "9" : "D",
        "10" : "X",
        "11" : "B",
        "12" : "N",
        "13" : "J",
        "14" : "Z",
        "15" : "S",
        "16" : "Q",
        "17" : "V",
        "18" : "H",
        "19" : "L",
        "20" : "C",
        "21" : "K",
        "22" : "E"
    }
    def __init__(self, digits):
        self.digits = int(digits)
    def calculate(self):
        mod = self.digits % len(self.mod_to_letter)
        logger.debug('Mod is: '+ str(mod))
        return self.mod_to_letter[str(mod)]

if __name__ == '__main__':
    logging.config.fileConfig('letra_dni/logging.conf')
    logger = logging.getLogger('calcularLetraDNILogger')
    myDni = LetraDni(sys.argv[1])
    print(myDni.calculate())