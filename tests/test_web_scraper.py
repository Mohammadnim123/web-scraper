from web_scraper import __version__
from web_scraper.scraper import *

def test_version():
    assert __version__ == '0.1.0'

def test_correct_count_of_citations():
    expected = 5
    actual = get_citations_needed_count('https://en.wikipedia.org/wiki/Petra')
    assert expected == actual

def test_verify_that_preceding_passage():
    expected = "\n\n\nthe line before:   The high salt concentration of the Dead Sea has been proven therapeutic for many skin diseases\n\nThe whole paragraph: Jordan has been a medical tourism destination in the Middle East since the 1970s. A study conducted by Jordan's Private Hospitals Association found that 250,000 patients from 102 countries received treatment in Jordan in 2010, compared to 190,000 in 2007, bringing over $1\xa0billion in revenue. Jordan is the region's top medical tourism destination, as rated by the World Bank, and fifth in the world overall.[203] The majority of patients come from Yemen, Libya and Syria due to the ongoing civil wars in those countries. Jordanian doctors and medical staff have gained experience in dealing with war patients through years of receiving such cases from various conflict zones in the region.[204]  Jordan also is a hub for natural treatment methods in both Ma'in Hot Springs and the Dead Sea. The Dead Sea is often described as a 'natural spa'. It contains 10 times more salt than the average ocean, which makes it impossible to sink in. The high salt concentration of the Dead Sea has been proven therapeutic for many skin diseases.[citation needed] The uniqueness of this lake attracts several Jordanian and foreign vacationers, which boosted investments in the hotel sector in the area.[205] The Jordan Trail, a 650\xa0km (400\xa0mi) hiking trail stretching the entire country from north to south, crossing several of Jordan's attractions was established in 2015.[206] The trail aims to revive the Jordanian tourism sector.[206]\n"
    actual = get_citations_needed_report('https://en.wikipedia.org/wiki/Jordan')
    assert expected == actual
    
