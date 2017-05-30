import tkinter
import os
import urllib.request
import MinerUtils as mutils

config = open("config.txt", 'a')
window = tkinter.Tk()
window.title("Acdop100 & ExpertDash's AIO Miner tool")
window.geometry("620x830")

mutils.setMainWindow(window)

print("420 test it memescope dorito")
proc = "none"
standardInstructionsMessage = "Open the app and follow the on-screen instructions. They're pretty straight forward"

# Updates the program with inputted information
def infoupdate():  
    coinLabel.configure(text="Coin = " + coinOption.box.get())
    proc = str(processorBox.get())

#Saves something to the config file
def saveToConfig(txt): config.write("-" + txt + "\n")

# Save an individual option to the config file
def saveOptionToConfig(name, option): saveToConfig(name + " " + option.box.get())

# Writes variables to the miner's config file
def savetofile():
    config = open("config.txt", 'a')
    isDual = dualOption.box.get() == 'y'

    saveOptionToConfig("epool", poolOption)
    saveOptionToConfig("ewal", walletOption)
    saveOptionToConfig("epsw", passwordOption)
    saveOptionToConfig("tt", tempOption)

    saveToConfig("mode 0" if isDual else "mode 1")
    if isDual:
        saveToConfig("mode 0")
        saveOptionToConfig("dcoin", coinOption)
        saveOptionToConfig("dpool", poolOption)
        saveOptionToConfig("dwal", walletOption)
        saveOptionToConfig("dpsw", coinPasswordOption)

    saveOption.label.configure(text="Saved!")

# Configure options command

def configureOptions(pool, wallet, password, temperature, dual, coin, coinWallet, coinPool, coinPassword, save, saveButtonText, saveButtonCommand):
    poolOption.label.configure(text=pool)
    walletOption.label.configure(text=wallet)
    passwordOption.label.configure(text=password)
    tempOption.label.configure(text=temperature)
    dualOption.label.configure(text=dual)
    coinOption.label.configure(text=coin)
    coinWalletOption.label.configure(text=coinWallet)
    coinPoolOption.label.configure(text=coinPool)
    coinPasswordOption.label.configure(text=coinPassword)
    saveOption.label.configure(text=save)
    saveButton.configure(text=saveButtonText, command=saveButtonCommand)

def downloadProgramForCoin(shouldConfigureOptions, url, name, wlength, instructions):
     if(len(url) > 0 and len(name) > 0): urllib.request.urlretrieve(url, name)
     if(len(instructions) > 0): instructionsLabel.configure(text=instructions, wraplength=wlength)
     return shouldConfigureOptions

#Returns true if the name matches the coin entered by the user
def isCoin(name): return str(coinOption.box.get()) == name

# Bunch of if/else statements to decide which program to download
def dwnld():
    coinLabel.configure(text="Downloading!")
    osLabel.configure(text="Tool(s) will download to the same directory as this tool")

    shouldConfigureOptions = False
    
    # Windows programs
    if os.name == 'nt':
        # NiceHashMiner
        if isCoin("NHM"):
            shouldConfigureOptions = downloadProgramForCoin(
                False,
                "https://github.com/nicehash/NiceHashMiner/releases/download/1.7.5.12/NiceHashMiner_v1.7.5.12.zip",
                "NiceHashMiner_v1.7.5.12.zip",
                0,
                ""
            )
        
        # Ethereum
        elif isCoin("ETH"): shouldConfigureOptions = downloadProgramForCoin(True, "", "", 350, standardInstructionsMessage)

        # Dashcoin
        elif isCoin("DASH"):
             shouldConfigureOptions = downloadProgramForCoin(
                False,
                "https://github.com/dashminer/dashminer/releases/download/2.1.1/DashMiner211x.zip",
                "DashMiner211x",
                350,
                standardInstructionsMessage
            )
        
        # Ethereum Classic :(
        elif isCoin("ETC"): shouldConfigureOptions = downloadProgramForCoin(True, "", "", 350, standardInstructionsMessage)
        
        # Monero
        elif isCoin("XMR"): 
            subURL = ""
            subName = ""
            if proc == "CPU":
                subURL = "https://github.com/jwinterm/monerospelunker/releases/download/0.1/monerospelunker_v01.zip"
                subName = "monerospelunker_v01.zip"
            elif proc == "AMD":
                subURL = "https://github.com/fireice-uk/xmr-stak-amd/releases/download/v1.0.0-1.3.1/xmr-stak-amd-win64.zip"
                subName = "xmr-stak-amd-win64.zip"
            elif proc == "NVD":
                subURL = "https://github.com/fireice-uk/xmr-stak-nvidia/releases/download/v1.1.1-1.4.0/xmr-stak-nvidia.zip"
                subName = "xmr-stak-nvidia.zip"
            shouldConfigureOptions = downloadProgramForCoin(
                False,
                subURL,
                subNAME,
                350,
                standardInstructionsMessage
            )
        # Zcash
        elif isCoin("ZEC"): shouldConfigureOptions = downloadProgramForCoin(True, "", "", 350, standardInstructionsMessage)
        
        # Siacoin AKA SiaCloud
        elif isCoin("SC"):
            shouldConfigureOptions = downloadProgramForCoin(
                False,
                "https://siamine.com/files/marlin/win64/marlin-1.0.0-win64.zip",
                "marlin-1.0.0-win64.zip",
                350,
                standardInstructionsMessage
            )

    # Linux/GNU programs
    else:  
        if isCoin("ETH"): shouldConfigureOptions = downloadProgramForCoin(True, "", "", 350, standardInstructionsMessage)
        elif isCoin("DASH"): shouldConfigureOptions = downloadProgramForCoin(True, "", "", 350, standardInstructionsMessage)
        elif isCoin("ETC"): shouldConfigureOptions = downloadProgramForCoin(True, "", "", 350, standardInstructionsMessage)
        elif isCoin("XMR"): shouldConfigureOptions = downloadProgramForCoin(True, "", "", 350, standardInstructionsMessage)
        elif isCoin("ZEC"): shouldConfigureOptions = downloadProgramForCoin(True, "", "", 350, standardInstructionsMessage)

        elif isCoin("SC"):
            shouldConfigureOptions = downloadProgramForCoin(
                True,
                "https://siamine.com/files/marlin/linux-amd64/marlin-1.0.0-linux-amd64.tar.gz",
                "marlin-1.0.0-linux-amd64.tar.gz",
                350,
                "Load the IPA file into Cydia Impactor and then use Cydia Impactor to sideload the app"
            )

    if(shouldConfigureOptions):
        configureOptions(
                "Pool Address",
                "Wallet Address",
                "Pool Password",
                "Target GPU Temperature",
                "Are You Dual Mining? (y/n)",
                "If So, Which Coin?",
                "2nd Coin Wallet Address",
                "2nd Coin Pool Address",
                "2nd Coin Pool Password",
                "Ready So Save",
                "Save To Config.txt",
                savetofile
            )

#Info
mutils.createLabelWithFont(("Helvetica", 18), "Input the currency symbol for the coin you want to mine")
mutils.createLabelWithFont(("Helvetica", 9), "For example, ETH for Ethereum or NHM for NiceHash Miner")
mutils.createLabelWithFont(("Helvetica", 9), "Some miners are windows only, if a program doesn't download switch coin")
mutils.createLabelWithFont(("Helvetica", 18), "Are you mining on your CPU or GPU(s)?")
mutils.createLabelWithFont(("Helvetica", 9), "Write CPU, or for GPU write AMD or NVD' ",)

#<describe this alex>
cpuBox = mutils.createBox()
processorBox = mutils.createBox()
updateButton = mutils.createButton("Update coin info to program", infoupdate)
coinLabel = mutils.createLabel(" ")
osLabel = mutils.createLabel(" ")
mutils.createButton("Download corresponding Tool", dwnld)
instructionsLabel = mutils.createLabel("Instructions will appear here")
mutils.createLabel("Configuration file creation will appear here")

#Mining Options
poolOption = mutils.createOption("Pool")
walletOption = mutils.createOption("Wallet")
passwordOption = mutils.createOption("Password")
tempOption = mutils.createOption("Temperature")
dualOption = mutils.createOption("Dual")
coinOption = mutils.createOption("Coin")
coinWalletOption = mutils.createOption("Coin Wallet")
coinPoolOption = mutils.createOption("Coin Pool")
coinPasswordOption = mutils.createOption("Coin Password")
saveOption = mutils.createOption("Save")

#<describe this alex>
saveButton = mutils.createButton("When Config is filled above, Save To Config.txt", savetofile)

#Pack & Begin Update
mutils.packAll()
window.mainloop()