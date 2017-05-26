import tkinter
import os
import urllib.request

window = tkinter.Tk()
window.title("Acdop100 & ExpertDash's AIO Miner tool")
window.geometry("380x630")

print("test")


def infoupdate():  # updates the program with inputted information
    coinlbl.configure(text="Coin = " + coin.get())


def dwnld():  # bunch of if/else statements to decide which program to download
    coinlbl.configure(text="Downloading!")
    oslbl.configure(text="Tool(s) will download to the same directory as this tool")
    if os.name == 'nt':  # Windows programs
        if str(coin.get()) == "933" or str(coin.get()) == "930" or str(coin.get()) == "9":
            print("memes")

        elif str(coin.get()) == "ETh":
            urllib.request.urlretrieve("", "")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)

        elif str(coin.get()) == "DASH":
            urllib.request.urlretrieve("", "")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)

        elif str(coin.get()) == "ETC":
            urllib.request.urlretrieve("", "")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)

        elif str(coin.get()) == "XMR":
            urllib.request.urlretrieve("", "")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)

        elif str(coin.get()) == "ZEC":
            urllib.request.urlretrieve("", "")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)

        elif str(coin.get()) == "SC":
            instructions.configure(
                text="Load the IPA file into Cydia Impactor and then use Cydia Impactor to sideload the app",
                wraplength=350)
            urllib.request.urlretrieve("", "")

    else:  # OS X programs
        if str(coin.get()) == "GAME":
            urllib.request.urlretrieve("", "")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)

        elif str(coin.get()) == "ETh":
            urllib.request.urlretrieve("", "")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)

        elif str(coin.get()) == "DASH":
            urllib.request.urlretrieve("", "")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)

        elif str(coin.get()) == "ETC":
            urllib.request.urlretrieve("", "")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)

        elif str(coin.get()) == "XMR":
            urllib.request.urlretrieve("", "")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)

        elif str(coin.get()) == "ZEC":
            urllib.request.urlretrieve("", "")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)

        elif str(coin.get()) == "SC":
            instructions.configure(
                text="Load the IPA file into Cydia Impactor and then use Cydia Impactor to sideload the app",
                wraplength=350)
            urllib.request.urlretrieve("", "")


pleaselbl = tkinter.Label(window, text="Input the currency symbol for the coin you want to mine",
                          font=("Helvetica", 18))
please2lbl = tkinter.Label(window, text="For example, ETH for Ethereum or SC for Siacoin' ",
                           font=("Helvetica", 9))

coin = tkinter.Entry(window)
updatebtn = tkinter.Button(window, text="Update coin info to program", command=infoupdate)

coinlbl = tkinter.Label(window, text=" ")
oslbl = tkinter.Label(window, text=" ")
downloadbtn = tkinter.Button(window, text="Download corresponding Tool", command=dwnld)

instructions = tkinter.Label(window, text="Intructions for your tool will go here")

pleaselbl.pack()
please2lbl.pack()
coin.pack()
updatebtn.pack()
coinlbl.pack()
oslbl.pack()
downloadbtn.pack()
instructions.pack()
