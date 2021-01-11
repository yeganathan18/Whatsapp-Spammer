# Whatsapp Spammer 🔫

Want to spam your friend on Whatsapp!? then you're probably in the right place. Follow the below few steps and you're ready to go❗️

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the necessary module to run the python script.

```bash
pip3 install selenium
```
Get the chrome driver for chrome browser based on the version you have [here](https://chromedriver.chromium.org).

### Note
We can also use other browsers with this python script, but before doing so install the necessary browser driver.

## Usage

```python
import selenium

# Give your chrome driver path (relative path) in the executable_path argument
driver = webdriver.Chrome(executable_path='')

name = input("Name:") # name as per in the WhatsApp contact
message = input("Message:") # message that you want to spam
i = int(input("How many Spam Text: ")) # count of spam message
```

## Finally 🎉

Successfully spammed our friend😌