import pywhatkit as kit

#details - https://pywhatkit.herokuapp.com
# "PhoneNr", "text", hours, min, timeMsgIsSentAfterOpeningWa
#kit.sendwhatmsg("+372 5648", "test2", 17, 28, 5, True)

FirstText = ""
DestinationPhoneNr = ""
kit.sendwhatmsg(DestinationPhoneNr, FirstText, 23, 59, 10, True)

SecondText = ""
DestinationPhoneNr2 = ""
kit.sendwhatmsg(DestinationPhoneNr2, SecondText, 00, 00, 10, True)


