from requests import get   #package to import optifine website html code
from win10toast import ToastNotifier   #package that send windows notifications

#Optifine downloads page url
url = "https://optifine.net/downloads"
response = get(url)

source = response.text
Toast = ToastNotifier()

#variable that decide if the program must stop
running = True

while (running == True) :
    #look for "<h2>Minecraft 1.17.1</h2>" in the html code
    #you can change "1.17.1" to "1.17.2" or higher if you want
    if (source.__contains__("<h2>Minecraft 1.17.1</h2>") == True) :

        #send the notification (title , message , duration)
        Toast.show_toast("OptiFine for 1.17.1 is here !", "This notification was offered by the great DimenSpace"
                 "\nGo check the official Optifine website"
                 , duration=10)
        running = False   #stop the code by changing the variable to False