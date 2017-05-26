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

        elif str(coin.get()) == "902":
            urllib.request.urlretrieve("http://dl.pangu.25pp.com/jb/Pangu9_v1.3.2.exe", "Pangu9_v1.3.2.exe")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)

        elif str(coin.get()) == "813":
            urllib.request.urlretrieve("http://res.taig.com/installer/en/TaiGJBreak_EN_v245_5266.exe",
                                       "TaiGJBreak_EN_v245_5266")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)

        elif str(coin.get()) == "712":
            urllib.request.urlretrieve("https://www.dropbox.com/s/4mgj37hernjn188/evasi0n7-win-1.0.7.zip?dl=1",
                                       "evasi0n7-win-1.0.7.zip")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)

        elif str(coin.get()) == "613":
            urllib.request.urlretrieve("http://p0sixspwn.co/p0sixspwn-v1.0.8-win.zip", "p0sixspwn-v1.0.8-win.zip")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)

        elif str(coin.get()) == "511":
            urllib.request.urlretrieve("hhttps://sites.google.com/site/greenpois0nabsinthe/"
                                       "absinthe-win-2.0.4.zip?attredirects=0&d=1", "absinthe-win-2.0.4.zip")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)

        elif str(coin.get()) == "1001":
            instructions.configure(
                text="Load the IPA file into Cydia Impactor and then use Cydia Impactor to sideload the app",
                wraplength=350)
            urllib.request.urlretrieve("https://yalu.qwertyoruiop.com/yalu102_beta7.ipa", "yalu102_beta7.ipa")

    else:  # OS X programs
        if str(coin.get()) == "933":
            print("memes")

        elif str(coin.get()) == "1001":
            instructions.configure(
                text="Load the IPA file into Cydia Impactor and then use Cydia Impactor to sideload the app",
                wraplength=350)
            urllib.request.urlretrieve("https://yalu.qwertyoruiop.com/yalu102_beta7.ipa", "yalu102_beta7.ipa")

        elif str(coin.get()) == "902":
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)
            urllib.request.urlretrieve("https://www.dropbox.com/s/d6rr4aa2obbvvnj/pangu9_mac_v1.1.1%202.dmg?dl=1",
                                       "pangu9_mac_v1.1.1.dmg")

        elif str(coin.get()) == "813":
            urllib.request.urlretrieve("http://res.taig.com/installer/mac/TaiGjailbreak_V110.dmg",
                                       "TaiGjailbreak_V110.dmg")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)

        elif str(coin.get()) == "712":
            urllib.request.urlretrieve("http://randomsite.com/file.gz", "file.gz")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)

        elif str(coin.get()) == "613":
            urllib.request.urlretrieve("http://posixspwndownload.com/downloads/p0sixspwn-v1.0.7-mac.zip",
                                       "p0sixspwn-v1.0.7-mac.zip")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)
        elif str(coin.get()) == "511":
            urllib.request.urlretrieve("https://sites.google.com/site/greenpois0nabsinthe/"
                                       "absinthe-mac-2.0.4.dmg?attredirects=0&d=1", "absinthe-mac-2.0.4.dmg")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)


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
