#!usr/local/bin/python

from bs4 import BeautifulSoup
import requests
#------------------------
def parsePage(soup):
    barNamesStr = []
    review_list = []

    barNames = soup.body.find_all("h3", attrs={'class': 'search-result-title'})
    for name in barNames:
        bar = name.find('a', attrs={'class': 'biz-name js-analytics-click'}).find('span').text
        barNamesStr.append(bar)
    location = soup.body.find_all("address")
    reviews = soup.find_all("p", class_="lemon--p__373c0__1hkz1 text__373c0__2pB8f text__373c0__2P1WD alternateStyling__373c0__2ithU text-color--normal__373c0__K_MKN text-align--left__373c0__2pnx_")
    for rev in reviews:
        rev.a.decompose()
        review_list.append(rev)
    return barNamesStr, location, review_list

#---------------------- --
def cleanUpTxt(bars):
    names = bars[0]
    locations = bars[1]
    reviews = bars[2]
    for name, loc in list(zip(names, locations)):
        print(name + ": ", loc.text.strip() + "\n")

#-------------------------
def main():
    zip_code = input("Please enter a five digit zip code: ")
    page = requests.get("https://www.yelp.com/search?find_desc=bar&find_loc=" + zip_code)
    soup = BeautifulSoup(page.content, 'html.parser')
    bars = parsePage(soup)
    cleanUpTxt(bars)

if __name__ == "__main__":
    main()
