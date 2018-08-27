# Zayd Haque
# Script to get top 50 movies from imdb of the year 
# puts into a text file with users name
# using beautifulSoup


# import for pool manager which helps with HTTP requests
import urllib3
# needed to give access to vars and functs that interact strongly with interpreter
import sys
# importing the actual web scraping api (HTML parser)
from bs4 import BeautifulSoup 
# for progress bar
from tqdm import tqdm 



# get name
name = input('Enter your name: ')

# get year
year = str(int(input('Enter the year: ')))

# creating and opening a text file - outputting to file
sys.stdout = open(name + '_IMDB_Top_50_' + year + '_urllib3.txt', 'w')

# the url we will use 
url = "http://www.imdb.com/search/title?release_date=" + year + "," + year + "&title_type=feature"

# get data from imdb 
r = urllib3.PoolManager().request('GET', url).data
# the actual scarping
soup = BeautifulSoup(r, "html.parser")
article = soup.find('div', attrs={'class': 'article'}).find('h1')
print (article.contents[0] + ':')
lister_list_contents = soup.find('div', attrs={'class': 'lister-list'})


# index for FOR loop
i = 1

# figure out what these  statements do !!!
movieList = soup.findAll('div', attrs = {'class': 'lister-item mode-advanced'})

# for loop for finding and printing
# tqdm(movielist) shows a progressbar and updates for each item done
for div in tqdm(movieList):
    # prints the number index EX - "1. "
    print (str(i) + '.') , 
    header = div.findChildren('h3', attrs = {'class' : 'lister-item-header'})
    # another for loop
    for items in header:
        title = header[0].findChildren('a')
        print ('Movie: ' + str(title[0].contents[0]))
    genre = div.findChildren('span', attrs={'class' : 'genre'})
    genre_text = genre[0].text.encode('utf-8').decode('ascii', 'ignore')
    print ('Genre: ' + genre_text.strip('\n'))
    p_all = div.findAll('p', attrs={'class': 'text-muted'})
    desc = p_all[1].text.encode('utf-8').decode('ascii','ignore')
    print ('Description: ' + desc.strip('\n'))
    
    # increment
    i += 1
