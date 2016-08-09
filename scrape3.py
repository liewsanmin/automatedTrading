import requests
from BeautifulSoup import BeautifulSoup
import lxml.html
import webbrowser

def connectAllPriceTarget():
    global soup
    priceTargetUrl = 'http://klse.i3investor.com/jsp/pt.jsp' # get url
    page = requests.get(priceTargetUrl) # connect to page
    html = page.content # get html content
    soup = BeautifulSoup(html) #beautify the html page

def compileStocksAndLinks():
    table = soup.find('table', {'class': 'nc'})
    #for each row, there are many rows including no table
    global stockNames, priceTargetLinks
    stockNames = []
    priceTargetLinks = []
    for tr in table.findAll('tr'):
        center = tr.find('td', {'class': 'center'}) # for each center
        # not all rows have 'center' (price call)
        if(center and center.text == "BUY" and tr.find('a').get('href') not in priceTargetLinks):
            leftTag = tr.findAll('td', {'class': 'left'}) # find all 'left' that in that row
            stockNames += [leftTag[1].text]
            priceTargetLinks += [tr.find('a').get('href')]

def openPriceTargetLink():
    for link in priceTargetLinks:
        url = 'http://klse.i3investor.com' + link
        webbrowser.open(url, new=0, autoraise=True)

################################################################################
# START HERE                                                                   #
################################################################################
connectAllPriceTarget()
compileStocksAndLinks()
openPriceTargetLink()
