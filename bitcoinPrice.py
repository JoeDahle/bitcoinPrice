###############################################################################
# Get the current price of bitcoins
###############################################################################

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
#from kivy.uix.button import Button
from bs4 import BeautifulSoup as bs
from kivy.config import Config
import urllib2

Config.set('graphics', 'width', '150')
Config.set('graphics', 'height', '75')


class BitcoinPriceGUI(FloatLayout):

    def __init__(self, **kwargs):
        super(BitcoinPriceGUI, self).__init__()

        mtgox = 'https://mtgox.com/'
        openPage = urllib2.urlopen(mtgox)
        page = openPage.read()
        openPage.close()
        soup = str(bs(page))
        lastPriceStartLoc = soup.find("price:<span>")
        lastPriceEndLoc = soup[lastPriceStartLoc:].find("</span>")
        price = soup[lastPriceStartLoc + 12:lastPriceEndLoc +
        lastPriceStartLoc]
        priceLbl = Label(
            text=price,
            size_hint=(1., 1.),
            pos=(0, 0))
        self.add_widget(priceLbl)


class BitcoinPrice(App):

    def build(self):
        return BitcoinPriceGUI()


if __name__ == '__main__':
    BitcoinPrice().run()

#try:
    #mtgox = 'https://mtgox.com/'
    #openPage = urllib2.urlopen(mtgox)
    #page = openPage.read()
    #openPage.close()
    #soup = str(bs(page))
    ##print soup
    #lastPriceStartLoc = soup.find("price:<span>")
    #lastPriceEndLoc = soup[lastPriceStartLoc:].find("</span>")
    #print soup[lastPriceStartLoc + 12:lastPriceEndLoc + lastPriceStartLoc]

#except Exception:
    #print 'error'
