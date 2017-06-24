import urllib
import pdb
from urllib import request
from bs4 import BeautifulSoup
import re
dave = []
num = 1

def is_tag(href):
    return href and re.compile("works").search(href)and len(href)<=14 

def one_page(url):
    main = urllib.request.urlopen("http://archiveofourown.org/works/search?utf8=%E2%9C%93&work_search%5Bquery%5D=kudos%3E300+words%3C10000&work_search%5Btitle%5D=&work_search%5Bcreator%5D=&work_search%5Brevised_at%5D=&work_search%5Bcomplete%5D=0&work_search%5Bsingle_chapter%5D=0&work_search%5Bword_count%5D=&work_search%5Blanguage_id%5D=&work_search%5Bfandom_names%5D=&work_search%5Brating_ids%5D=13&work_search%5Bcharacter_names%5D=&work_search%5Brelationship_names%5D=&work_search%5Bfreeform_names%5D=&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Bcomments_count%5D=&work_search%5Bbookmarks_count%5D=&work_search%5Bsort_column%5D=kudos_count&work_search%5Bsort_direction%5D=&commit=Search")
    soup = BeautifulSoup(main.read(), 'html.parser')
    links = soup.find_all(href=is_tag)

    links.pop(0)
    print("start loop")
    for i in links:
        num = num + 1
        tempstr = str(i)
        tempstr = tempstr[16:(-(len(tempstr)-tempstr.index(">"))-1)]
        work = urllib.request.urlopen("http://archiveofourown.org/works/" + tempstr)
        worksoup = BeautifulSoup(work.read(),'html.parser')
        f = open("pormnum" + str(num) + ".txt", 'w')
        f.write(worksoup.prettify(formatter="html"))
        f.close()
        
        


main = urllib.request.urlopen("http://archiveofourown.org/works/search?utf8=%E2%9C%93&work_search%5Bquery%5D=kudos%3E300+words%3C10000&work_search%5Btitle%5D=&work_search%5Bcreator%5D=&work_search%5Brevised_at%5D=&work_search%5Bcomplete%5D=0&work_search%5Bsingle_chapter%5D=0&work_search%5Bword_count%5D=&work_search%5Blanguage_id%5D=&work_search%5Bfandom_names%5D=&work_search%5Brating_ids%5D=13&work_search%5Bcharacter_names%5D=&work_search%5Brelationship_names%5D=&work_search%5Bfreeform_names%5D=&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Bcomments_count%5D=&work_search%5Bbookmarks_count%5D=&work_search%5Bsort_column%5D=kudos_count&work_search%5Bsort_direction%5D=&commit=Search")
soup = BeautifulSoup(main.read(), 'html.parser')



