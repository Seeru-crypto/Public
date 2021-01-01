import pywhatkit as kit

#details - https://pywhatkit.herokuapp.com
# "PhoneNr", "text", hours, min, timeMsgIsSentAfterOpeningWa
#kit.sendwhatmsg("+372 5648 5582", "test2", 17, 28, 5, True)

# TestingPhoneNr = "+1 (415) 523-8886"  


AinText = ""
DestinationPhoneNr = ""
kit.sendwhatmsg(DestinationPhoneNr, AinText, 23, 59, 10, True)

KasparText = ""
DestinationPhoneNr2 = ""
kit.sendwhatmsg(DestinationPhoneNr2, KasparText, 00, 00, 10, True)


