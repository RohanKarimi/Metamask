
## Introduction
This package is created to automate metamask wallet extension using selenium webdriver. 

#### To Install The Package:



```sh
pip install ./selenium_metamask_automation
```
Check if the package exists
```sh
pip list
```

## Functions

#### 1. To download the extension:

```sh
selenium_metamask_automation.downloadMetamaskExtension()
```
This function has to be run once before all functions to download the metamask extension. If you change the directory or create your python file somewhere else, this needs to be run first otherwise following exception will be thrown:

“Path to extension does not exist”

#### 2. To launch the extension use the function below
```sh
selenium_metamask_automation.launchMetamaskExtension(args)
```
args: path to chrome webdriver



This function returns a value which contains the driver. You can retrieve it like:
```sh
driver = launchSeleniumWebdriver(r‘C:\Drivers\chromedriver_win32\chromedriver.exe’)
```

Now use can call any selenium method using this driver variable
```sh
driver.get("https://google.com")
```
#### 3. To import wallet
```sh
selenium_metamask_automation.metamaskSetup(arg1, arg2)
```
arg1 : seed phrase of wallet
arg2: password of wallet


#### 4. To Change the metamask Network:
```sh
selenium_metamask_automation.changeMetamaskNetwork(arg)
```

arg: network name

The network names are mentioned below. On selecting any other network, it will throw an error.

- Ethereum Mainnet
- Ropsten Test Network
- Kovan Test Network
- Rinkeby Test Network
- Goerli Test Network


