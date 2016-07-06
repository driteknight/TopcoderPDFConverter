__author__ = 'driteknight'
from bs4 import BeautifulSoup
import urllib2
import os

topcoder_link = "https://www.topcoder.com/community/data-science/data-science-tutorials/";
soup = BeautifulSoup(urllib2.urlopen(topcoder_link).read(), 'html.parser');
all_tds = soup.findAll("td");
algorithm_pages_td = [];
for td in all_tds:
    if str(td).startswith('<td><a href="https://www.topcoder.com/community/data-science/data-science-tutorials/'):
        algorithm_pages_td.append(td);
for td in algorithm_pages_td: 
    for algorithm_page in td.findAll("a"):
        link = algorithm_page['href'];
        file_name = link.split('tutorials')[1][1:-1]  
        print link
        os.system("wkhtmltopdf "+link+" "+ "PDFFiles/" + file_name + ".pdf");


