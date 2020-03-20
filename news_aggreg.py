from azure.cognitiveservices.search.newssearch import NewsSearchClient
from msrest.authentication import CognitiveServicesCredentials

import sys
sys.path.insert(0, r'C:\Users\19293\Desktop\DS File\News App MS\Keys')
import keys_seven as ks

#Subscription key was created on 3/20/20 with an expiration period of 7 days.
#Thefore, it needs to be updated once the 7-day period passes on 3/28/20.
subscription_key = ks.key_one


def search(search_term):
    """A function to search articles on the Web using a specific term. 
    Results include a headline and url of every article (# = count parameter)
    """
    search_term = search_term

    #Azure Cognitive Service Part
    endpoint = "https://api.cognitive.microsoft.com"
    client = NewsSearchClient(endpoint=endpoint, credentials=CognitiveServicesCredentials(subscription_key))
    news_result = client.news.search(query=search_term, market="en-us", count=10, freshness="day")
    
    #Local Python Part
    if news_result.value:
        for article in news_result.value:
            print(f"\n{article.name}")
            print(article.url)
            # print(article.description)
            # print(article.date_published)
            # print(article.provider[0].name)
    else:
        print("News is not found!")

# Example
# search("unemployment")

