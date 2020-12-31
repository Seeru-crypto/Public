import pywhatkit as kit

#details - https://pywhatkit.herokuapp.com
# "PhoneNr", "text", hours, min, timeMsgIsSentAfterOpeningWa
#kit.sendwhatmsg("+372 5648 5582", "test2", 17, 28, 5, True)



MsgText = "\n Hei \n Ma ei hakkanud sulle helistama, kuna ... you know oled Saksamaal. \n Nii et järgmine parim asi saadan WhatsAppi teel. \n  Happy New Year you filty animal XD \n PS: Loodetavasti saame järgmine aasta uuesti metsas sauna vaime ära ajada"
DestinationPhoneNr = "+372 5648 5582"
TestingPhoneNr = "+1 (415) 523-8886"
kit.sendwhatmsg(DestinationPhoneNr, MsgText, 00, 00, 5, True)
