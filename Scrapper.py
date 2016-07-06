__author__ = 'driteknight'
from bs4 import BeautifulSoup
import urllib2
import os
class Scrapper:
    def convertPage(self):
        topcoder_link = "https://www.topcoder.com/community/data-science/data-science-tutorials/";
        soup = BeautifulSoup(topcode_link, 'html.parser');
        all_tds = soup.findAll("td");
        algorithm_pages_td = [];
        for td in all_tds:
            if str(td).startswith('<td><a href="https://www.topcoder.com/community/data-science/data-science-tutorials/'):
                algorithm_pages_td.append(td);
        for td in algorithm_pages_td: 
            for algorithm_page in td.findAll("a"):
                atag = algorithm_page.get_text()
                link = atag['href'][0:-1];
                file_name = tmp.split('tutorials')[1][1:-1]  
                print link
                os.system("wkhtmltopdf --no-stop-slow-scripts "+link+" "+ "PDFFiles/" + file_name + ".pdf");