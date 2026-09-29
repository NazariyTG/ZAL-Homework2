



def writeTextToFile(argument:str):
    
    filename:str = "my_file.txt"

    STATICKY_TEXT = "This is my static text which must be added to file. It is very long text and I do not know what they want to do with this terrible text. "

    CombinedText = STATICKY_TEXT + argument

    file = open(filename, "w", encoding="utf-8")
    file.write(CombinedText)

    


writeTextToFile("fjdksalafd")

