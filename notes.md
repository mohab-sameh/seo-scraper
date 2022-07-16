**running the code**
- build a python virtual environment
- install packages by `pip install -r requirements.txt`
- activate the environment, then run `python main.py`

**references**
- [beautifulsoup doc](https://www.crummy.com/software/BeautifulSoup/bs4/doc)
- [requests doc](https://requests.readthedocs.io/)

**archived code**
```
#individualReviewsWrapperSoup = soup.find("div", attrs={"class":"individual-reviews-wrapper"})
#linksSoup = individualReviewsWrapperSoup.find("div", attrs={"class":"links"})
#wDynListSoup = linksSoup.find("div", attrs={"class":"w-dyn-list"})
#wDynItemsSoup = wDynListSoup.find("div", attrs={"class":"w-dyn-items"})
#itemListSoup = wDynItemsSoup.contents
#print( itemListSoup[1].prettify() )
#print( itemListSoup[1].find("a")['href'] )

#itemsList = soup.select(".individual-reviews-wrapper > .links > .w-dyn-list > .w-dyn-items")[0]
#item = itemsList.contents[0]
#print(item.find("a")['href'])
```
