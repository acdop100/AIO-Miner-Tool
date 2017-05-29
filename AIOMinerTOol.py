import tkinter
import os
import urllib.request

window = tkinter.Tk()
window.title("Acdop100 & ExpertDash's AIO Miner tool")
window.geometry("420x800")


def infoupdate():  # updates the program with inputted information
    coin2lbl.configure(text="Coin = " + coin.get())
    gpulbl.configure(text="Processor type = " + processor.get())


def savetofile():  # writes variables to the miner's config file
    savelbl.configure(text="Saved!")
    config = open("config.txt", 'a')
    ethpool = poolwindow.get()
    ethwallet = walletwindow.get()
    ethpswd = pswdwindow.get()
    temp = tempwindow.get()
    dual = dualwindow.get()
    dcoin = coinwindow.get()
    dpool = coinpoolwindow.get()
    dwal = coinwalletwindow.get()
    dpswd = coinpswdwindow.get()
    config.write("-epool " + ethpool + "\n")
    config.write("-ewal " + ethwallet + "\n")
    config.write("-epsw " + ethpswd + "\n")
    config.write("-tt " + temp + "\n")
    if dual == 'y':
        config.write("-mode 0" + "\n")
        config.write("-dcoin " + dcoin + "\n")
        config.write("-dpool " + dpool + "\n")
        config.write("-dwal " + dwal + "\n")
        config.write("-dpswd " + dpswd + "\n")

    else:
        config.write("-mode 1" + "\n")


def labelclay():
    poollbl.configure(text="Pool Address")

    walletlbl.configure(text="Wallet Address")

    pswdlbl.configure(text="Pool Password")

    templbl.configure(text="Target GPU Temperature")

    duallbl.configure(text="Are You Dual Mining? (y/n)")

    coinlbl.configure(text="If So, Which Coin?")

    coinwalletlbl.configure(text="2nd Coin Wallet Address")

    coinpoollbl.configure(text="2nd Coin Pool Address")

    coinpswdlbl.configure(text="2nd Coin Pool Password")

    savelbl.configure(text="Ready So Save")

    savebtn.configure(text="Save To Config.txt", command=savetofile)


def savetosia():
    savelbl.configure(text="Saved!")
    config = open("start.bat", 'a')
    ethpool = poolwindow.get()
    ethwallet = walletwindow.get()
    intensity = tempwindow.get()
    config.write("-H " + ethpool + "\n")
    config.write("-u " + ethwallet + "\n")
    config.write("-I " + intensity + "\n")


def labelsia():
    poollbl.configure(text="Pool Address")

    walletlbl.configure(text="Wallet/Worker Address")

    templbl.configure(text="Target Work Intensity")

    savelbl.configure(text="Ready So Save")

    savebtn.configure(text="Save To Config.txt", command=savetosia)


def labeldash():
    poollbl.configure(text="Pool Address")

    walletlbl.configure(text="Wallet/Worker Address")

    pswdlbl.configure(text="Pool Password")

    savelbl.configure(text="Ready So Save")

    savebtn.configure(text="Save To Config.txt", command=savetodash)


def savetodash():
    savelbl.configure(text="Saved!")
    config = open("config.txt", 'a')
    ethpool = poolwindow.get()
    ethwallet = walletwindow.get()
    dashword = pswdwindow.get()
    config.write("-o " + ethpool + "\n")
    config.write("-u " + ethwallet + "\n")
    config.write("-p " + dashword + "\n")


def dwnld():  # bunch of if/else statements to decide which program to download
    coin2lbl.configure(text="Downloading!")
    gpulbl.configure(text="Tool(s) will download to the same directory as this tool")
    if os.name == 'nt':  # Windows programs
        if str(coin.get()) == "NHM":  # NiceHashMiner
            urllib.request.urlretrieve("https://github.com/nicehash/NiceHashMiner/releases/download/1.7.5.12/"
                                       "NiceHashMiner_v1.7.5.12.zip", "NiceHashMiner_v1.7.5.12.zip")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)

        elif str(coin.get()) == "ETH":  # Ethereum
            urllib.request.urlretrieve("https://github.com/nanopool/Claymore-Dual-Miner/releases/download/v9.4/"
                                       "Claymore.s.Dual.Ethereum.Decred_Siacoin_Lbry_Pascal.AMD.NVIDIA.GPU.Miner"
                                       ".v9.4.zip", "Claymore.s.Dual.Ethereum.Decred_Siacoin_Lbry_Pascal.AMD.NVIDIA."
                                                    "GPU.Miner.v9.4.zip")
            instructions.configure(
                text="Drop the generated config file into the folder that the miner is in",
                wraplength=350)

            labelclay()

        elif str(coin.get()) == "DASH":  # Dashcoin
            urllib.request.urlretrieve(
                "https://github.com/dashminer/dashminer/releases/download/2.1.1/DashMiner211x.zip", "DashMiner211x")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)

            labeldash()

        elif str(coin.get()) == "ETC":  # Ethereum Classic :(
            urllib.request.urlretrieve("https://github.com/nanopool/Claymore-Dual-Miner/releases/download/v9.4/"
                                       "Claymore.s.Dual.Ethereum.Decred_Siacoin_Lbry_Pascal.AMD.NVIDIA.GPU.Miner"
                                       ".v9.4.zip", "Claymore.s.Dual.Ethereum.Decred_Siacoin_Lbry_Pascal.AMD.NVIDIA."
                                                    "GPU.Miner.v9.4.zip")
            instructions.configure(
                text="Drop the generated config file into the folder that the miner is in",
                wraplength=350)

            labelclay()

        elif str(coin.get()) == "XMR":  # Monero
            if str(processor.get()) == "CPU":
                urllib.request.urlretrieve("https://github.com/jwinterm/monerospelunker/releases/download/0.1/"
                                           "monerospelunker_v01.zip", "monerospelunker_v01.zip")

            elif str(processor.get()) == "AMD":
                urllib.request.urlretrieve("https://github.com/fireice-uk/xmr-stak-amd/releases/download/"
                                           "v1.0.0-1.3.1/xmr-stak-amd-win64.zip", "xmr-stak-amd-win64.zip")
            elif str(processor.get()) == "NVD":
                urllib.request.urlretrieve("https://github.com/fireice-uk/xmr-stak-nvidia/releases/"
                                           "download/v1.1.1-1.4.0/xmr-stak-nvidia.zip", "xmr-stak-nvidia.zip")

        elif str(coin.get()) == "ZEC":  # Zcash
            if str(processor.get()) == "AMD":
                urllib.request.urlretrieve("https://github.com/nanopool/ClaymoreZECMiner/releases/download/v12.5/"
                                           "Claymore.s.ZCash.AMD.GPU.Miner.v12.5.zip", "Claymore.s.ZCash.AMD.GPU.Miner"
                                                                                       ".v12.5.zip")
                print("3")

            elif str(processor.get()) == "NVD":
                urllib.request.urlretrieve("https://github.com/nanopool/ewbf-miner/releases/download/v0.3.3b/"
                                           "Zec.miner.0.3.3b.zip", "KBZec.miner.0.3.3b.zip")

            instructions.configure(
                text="Drop the generated config file into the folder that the miner is in",
                wraplength=350)

            labelclay()

        elif str(coin.get()) == "SC":  # Siacoin AKA SiaCloud
            instructions.configure(
                text="Load the IPA file into Cydia Impactor and then use Cydia Impactor to sideload the app",
                wraplength=350)
            urllib.request.urlretrieve("https://siamine.com/files/marlin/win64/marlin-1.0.0-win64.zip",
                                       "marlin-1.0.0-win64.zip")
            labelsia()

    else:  # Linux/GNU programs

        if str(coin.get()) == "ETH":
            urllib.request.urlretrieve("https://github.com/nanopool/Claymore-Dual-Miner/releases/download/v9.4/"
                                       "Claymore.s.Dual.Ethereum.Decred_Siacoin_Lbry_Pascal.AMD.NVIDIA.GPU.Miner.v9.4.-"
                                       ".LINUX.tar.gz", "Claymore.s.Dual.Ethereum.Decred_Siacoin_Lbry_Pascal"
                                                        ".AMD.NVIDIA.GPU.Miner.v9.4.-.LINUX.tar.gz")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)
            poollbl.configure(text="Pool Address")

            labelclay()

        elif str(coin.get()) == "DASH":
            urllib.request.urlretrieve("", "")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)

        elif str(coin.get()) == "ETC":

            urllib.request.urlretrieve("https://github.com/nanopool/Claymore-Dual-Miner/releases/download/v9.4/"
                                       "Claymore.s.Dual.Ethereum.Decred_Siacoin_Lbry_Pascal.AMD.NVIDIA.GPU.Miner.v9.4.-"
                                       ".LINUX.tar.gz", "Claymore.s.Dual.Ethereum.Decred_Siacoin_Lbry_Pascal"
                                                        ".AMD.NVIDIA.GPU.Miner.v9.4.-.LINUX.tar.gz")
            instructions.configure(
                text="Drop the generated config file into the folder that the miner is in",
                wraplength=350)

            labelclay()

        elif str(coin.get()) == "XMR":
            urllib.request.urlretrieve("", "")
            instructions.configure(
                text="Open the app and follow the on-screen instructions. They're pretty straight forward",
                wraplength=350)

        elif str(coin.get()) == "ZEC":

            if str(processor.get()) == "AMD":
                urllib.request.urlretrieve("https://github.com/nanopool/ClaymoreZECMiner/releases/download/v12.5/"
                                           "Claymore.s.ZCash.AMD.GPU.Miner.v12.5.-.LINUX.tar.gz",
                                           "Claymore.s.ZCash.AMD.GPU.Miner.v12.5.-.LINUX.tar.gz")
                print("3")

            elif str(processor.get()) == 'NVD':
                urllib.request.urlretrieve("https://github.com/nanopool/ewbf-miner/releases/download/v0.3.3b/"
                                           "Zec.miner.0.3.3b.Linux.Bin.tar.gz", "Zec.miner.0.3.3b.Linux.Bin.tar.gz")

            instructions.configure(
                text="Drop the generated config file into the folder that the miner is in",
                wraplength=350)

            labelclay()

        elif str(coin.get()) == "SC":
            instructions.configure(
                text="Load the IPA file into Cydia Impactor and then use Cydia Impactor to sideload the app",
                wraplength=350)
            urllib.request.urlretrieve("https://siamine.com/files/marlin/linux-amd64/marlin-1.0.0-linux-amd64.tar.gz",
                                       "marlin-1.0.0-linux-amd64.tar.gz")
            labelsia()

pleaselbl = tkinter.Label(window, text="Input currency symbol for the coin you want mined",
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

coin2lbl = tkinter.Label(window, text=" ")
gpulbl = tkinter.Label(window, text=" ")
downloadbtn = tkinter.Button(window, text="Download corresponding Tool", command=dwnld)

instructions = tkinter.Label(window, text="Instructions will appear here")

poollbl = tkinter.Label(window, text="Configuration file creation will appear here")
poolwindow = tkinter.Entry(window)

walletlbl = tkinter.Label(window, text="")
walletwindow = tkinter.Entry(window)

pswdlbl = tkinter.Label(window, text="")
pswdwindow = tkinter.Entry(window)

templbl = tkinter.Label(window, text="")
tempwindow = tkinter.Entry(window)

duallbl = tkinter.Label(window, text="")
dualwindow = tkinter.Entry(window)

coinlbl = tkinter.Label(window, text="")
coinwindow = tkinter.Entry(window)

coinwalletlbl = tkinter.Label(window, text="")
coinwalletwindow = tkinter.Entry(window)

coinpoollbl = tkinter.Label(window, text="")
coinpoolwindow = tkinter.Entry(window)

coinpswdlbl = tkinter.Label(window, text="")
coinpswdwindow = tkinter.Entry(window)

savelbl = tkinter.Label(window, text="")
savewindow = tkinter.Entry(window)

savebtn = tkinter.Button(window, text="When Config is filled above, Save To Config.txt", command=savetofile)

pleaselbl.pack()
please2lbl.pack()
coin.pack()
please3lbl.pack()
please4lbl.pack()
processor.pack()
updatebtn.pack()
coin2lbl.pack()
gpulbl.pack()
downloadbtn.pack()
instructions.pack()
poollbl.pack()
poolwindow.pack()
walletlbl.pack()
walletwindow.pack()
pswdlbl.pack()
pswdwindow.pack()
templbl.pack()
tempwindow.pack()
duallbl.pack()
dualwindow.pack()
coinlbl.pack()
coinwindow.pack()
coinwalletlbl.pack()
coinwalletwindow.pack()
coinpoollbl.pack()
coinpoolwindow.pack()
coinpswdlbl.pack()
coinpswdwindow.pack()
savelbl.pack()
savebtn.pack()

window.mainloop()
