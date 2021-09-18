import webbrowser
import pyautogui
from time import sleep


import pandas as pd

# your word to tweet
data = ['hello', 'hi', '私', 'you', 'I']

# your username twitter
username = ''

webbrowser.open("https://twitter.com/"+username)

sleep(5)

def tweet(text):
    pyautogui.click("img/tomboltweet.png")
    sleep(2)
    df=pd.DataFrame([text])
    df.to_clipboard(index=False,header=False)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.click("img/tweet.png")


for d in data:
    tweet(str(d))
    sleep(2)