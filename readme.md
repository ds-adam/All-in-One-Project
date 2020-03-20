# CorporateAutoSearch
### Description
CorporateAutoSearch is a GUI application built in Python to automate accessing corporate filings of publicly traded companies. On a high level, the program enables its users to access vast amounts of public information about a particular company by connecting to third-party APIs (TD Ameritrade), scraping websites (finviz.com) and making necessary calculations (numpy). As you can see below, the program can be said to have two essential parts - inputs on the left and outputs on the right. Inputs consist of entries and buttons, each corresponding to a specific task assigned. Outputs consits of a graph (price histry) and two text boxes - one for fundamental data and the other for SEC Filings list.

![](images/capture.jpg)


### Usage
To activate the program, a user needs a ticker, number of years for stock price history, and number of years for public filings history. Once these inputs are entered, the user should press corresponding buttons, after which results will appear in a short period.   

### Challenges
I encountered several challenges (learning opportunities) in building this program. One of them was embedding a matplotlib graph into an existing tkinter window (a pop-up-window graph is easy to generate). Next was related to data organization and presentation. After accessing third-party APIs, scrapping websites and making calculations, the amount of information and ways to present it meaningfully initially seemed too much. After struggling for some time, I think I managed the overall process well, at least presented information seems to be readable and understandable.   


### License