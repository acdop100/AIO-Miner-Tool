import tkinter
import os
import urllib.request

window = tkinter.Tk()
window.title("Acdop100 & ExpertDash's AIO Miner tool")
window.geometry("380x630")

print("test")
proc = "none"

def infoupdate():  # updates the program with inputted information
    coinlbl.configure(text="Coin = " + coin.get())
    proc = str(processor.get())

def dwnld():  # bunch of if/else statements to decide which program to download
    coinlbl.configure(text="Downloading!")
    oslbl.configure(text="Tool(s) will download to the same directory as this tool")
    if os.name == 'nt':  # Windows programs
        if str(coin.get()) == "NHM":
            urllib.request.urlretrieve("https://github.com/nicehash/NiceHashMiner/releases/download/1.7.5.12/"
                                       "NiceHashMiner_v1.7.5.12.zip", "NiceHashMiner_v1.7.5.12.zip")

        elif str(coin.get()) == "ETH":
            urllib.request.urlretrieve("", "")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)

        elif str(coin.get()) == "DASH":
            urllib.request.urlretrieve(
                "https://github.com/dashminer/dashminer/releases/download/2.1.1/DashMiner211x.zip", "DashMiner211x")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)

        elif str(coin.get()) == "ETC":
            urllib.request.urlretrieve("", "")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)

        elif str(coin.get()) == "XMR":
            if proc == "CPU":
                urllib.request.urlretrieve("https://github.com/jwinterm/monerospelunker/releases/download/0.1/"
                                           "monerospelunker_v01.zip", "monerospelunker_v01.zip")
                instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)
            elif proc == "AMD":
                urllib.request.urlretrieve("https://github.com/fireice-uk/xmr-stak-amd/releases/download/"
                                           "v1.0.0-1.3.1/xmr-stak-amd-win64.zip", "xmr-stak-amd-win64.zip")
                instructions.configure(
                    text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                    wraplength=350)

            elif proc == "NVD":
                urllib.request.urlretrieve("https://github.com/fireice-uk/xmr-stak-nvidia/releases/"
                                           "download/v1.1.1-1.4.0/xmr-stak-nvidia.zip", "xmr-stak-nvidia.zip")
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
            urllib.request.urlretrieve("https://siamine.com/files/marlin/win64/marlin-1.0.0-win64.zip",
                                       "marlin-1.0.0-win64.zip")

    else:  # Linux/GNU programs

        if str(coin.get()) == "ETh":
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
            urllib.request.urlretrieve("https://siamine.com/files/marlin/linux-amd64/marlin-1.0.0-linux-amd64.tar.gz",
                                       "marlin-1.0.0-linux-amd64.tar.gz")


pleaselbl = tkinter.Label(window, text="Input the currency symbol for the coin you want to mine",
                          font=("Helvetica", 18))
please2lbl = tkinter.Label(window, text="For example, ETH for Ethereum or NHM for NiceHash Miner",
                           font=("Helvetica", 9))
please5lbl = tkinter.Label(window, text="Some miners are windows only, if a program doesn't download switch coin",
                           font=("Helvetica", 9))

please3lbl = tkinter.Label(window, text="Are you mining on your CPU or GPU(s)?", font=("Helvetica", 18))
please4lbl = tkinter.Label(window, text="Write CPU, or for GPU write AMD or NVD' ", font=("Helvetica", 9))

coin = tkinter.Entry(window)
processor = tkinter.Entry(window)
updatebtn = tkinter.Button(window, text="Update coin info to program", command=infoupdate)

coinlbl = tkinter.Label(window, text=" ")
oslbl = tkinter.Label(window, text=" ")
downloadbtn = tkinter.Button(window, text="Download corresponding Tool", command=dwnld)

instructions = tkinter.Label(window, text="Intructions for your tool will go here")

pleaselbl.pack()
please2lbl.pack()
coin.pack()
please3lbl.pack()
please4lbl.pack()
processor.pack()
updatebtn.pack()
coinlbl.pack()
oslbl.pack()
downloadbtn.pack()
instructions.pack()
