import requests
from bs4 import BeautifulSoup
import json

def get_citations_needed_count(URL):
    
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup = soup.findAll(text='citation needed')
    return len(soup)

def get_citations_needed_report(URL):

    def _chick(x):
        """
        to take aline before the [citation needed]
        """
        y = x.split('.')
        i = 0 
        while i < len(y):
            if y[i].__contains__('[citation needed]'):
                return y[i-1]
            i+=1

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_="mw-parser-output").find_all('p')
    new_result = ''
    for elem in results:
        try:
            if elem.find_all('span', string = lambda text: 'citation needed' in text.lower()):
                
                new_result = new_result + f'\n\n\nthe line before:  {_chick(str(elem.text))}\n\nThe whole paragraph: {elem.text}'
                
        except:
            continue    
    
    return new_result

        
    






if __name__ == "__main__":
    print(get_citations_needed_report('https://en.wikipedia.org/wiki/History_of_Mexico'))
    
