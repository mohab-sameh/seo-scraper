## handy functions
#####

def writeJson( data, name ):
	with open(name+'.json', 'w') as out:
		json.dump(data, out, sort_keys=True, indent='\t')

def parseURLToSoup(URL_in):
    # HTTP request
    r = requests.get(URL_in)
    # parsing html
    soup = BeautifulSoup(r.text, features='lxml')

    return soup

#####

# 3rd-party libraries
import requests
from bs4 import BeautifulSoup
import json, csv

# constants
BASEURL = "https://www.best10mattress.com"
MATTRESSREVIEWSURL = "/mattress-reviews"


# read mattress reviews page as a soup
soup = parseURLToSoup(BASEURL + MATTRESSREVIEWSURL)

# traverse HTML nodes path by their classes, to fetch list of reviews headlines
reviewsList = soup.select(".individual-reviews-wrapper > .links > .w-dyn-list > .w-dyn-items")[0].contents

# loop on each review title
for reviewTitle in reviewsList:
    # fetch the title
    title = reviewTitle.select(".link-text")[0].string
    # fetch the link
    link = reviewTitle.find("a")['href']
    # complete link concatenated after the base url
    link = BASEURL + link

    # request the link as a soup
    soup = parseURLToSoup(link)

    # list of paragraphs
    paragraphsList = soup.select(".article-content-wrapper.no-cta")[0].next_sibling.contents

    # store data as a dictionary
    dict_data = {
        "title": None,
        "description": None,
        "paragraphs": []
    }

    # title and initial description of the page
    dict_data["title"] = title.string
    dict_data["description"] = paragraphsList[3].getText()
    # consideration and skipping recommendations
    consider = paragraphsList[4]
    skip = paragraphsList[5]

    # loop on each paragraph 
    for para in paragraphsList[6:-1]:
        paraDict = {}

        tem = para.find_all("div")
        # subtitle
        paraDict["subtitle"] = tem[0].find("h2").string
        # content
        paraDict["subcontent"] = tem[1].find("p").getText() if tem[1].find("p") is not None else "NONE" # in some cases retrieved none
        
        dict_data["paragraphs"].append(paraDict)
    
    # for testing only one review is scraped
    break


# write as a json file
writeJson(dict_data, 'out')

# write as csv file
with open('out.csv', 'w') as csvfile:
    csvWriter = csv.writer(csvfile, delimiter=',')

    data_list = []
    for para in dict_data["paragraphs"]:
        data_list.append(para["subtitle"])
        data_list.append(para["subcontent"])

    csvWriter.writerow(data_list)