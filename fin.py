
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import pandas as pd
def gen(rel,k=5):
    urls=[]
    for i in range(1,k):
        urls.append(rel+str(i))
    return urls
urls_avbl=[ "https://www.flipkart.com/books/~best-selling-books/pr?sid=bks&wid=14.productCard.PMU_V2_12&page=",
            "https://www.flipkart.com/books/~cs-4o0e8nd3z4/pr?sid=bks&collection-tab-name=Classics&fm=neo%2Fmerchandising&iid=M_eec1c101-888b-4ce4-8a3d-02ceb4fbe016_1.XBUQ20UJNF0Z&ppt=dynamic&ppn=dynamic&ssid=2endo75ga80000001578413984242&otracker=dynamic_omu_infinite_Bestselling%2BBooks_9_1.dealCard.OMU_INFINITE_XBUQ20UJNF0Z&cid=XBUQ20UJNF0Z&page=",
            "https://www.flipkart.com/search?q=best+sellin+books&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="

            ]       

bnames=[]
anames=[]
fl=0
def crawler(urls):
    for url in urls:
        url_open=(url)
        url_data= urlopen(url_open)
        url_html=url_data.read()
        soup_data= soup(url_html,'html.parser')
        title=soup_data.findAll('a',{'class':'_2cLu-l'})
        authors=soup_data.findAll('div',{'class':'_1rcHFq'})
        #img_div=soup_data.findAll('img',{'class':'_1Nyybr _30XEf0'})
        book_names=[]
        author_names=[]
        for i in range (len(authors)):
            author_names.append(authors[i].text[19:])
        for i in range (len(title)):
            book_names.append(title[i].text)
        bnames.append(book_names)
        anames.append(author_names)
    print(bnames)
    print(anames)
    with open("bookn_fdata.csv",'a') as f:
        strin=''
        for i in range(len(bnames)):
            strin=",\n".join(bnames[i])
            f.write(strin)
    with open("authorn_fdata.csv",'a') as fs:
        strin=''
        for i in range(len(anames)):
            strin=",\n".join(anames[i])
            fs.write(strin)
    
for n in range(len(urls_avbl)):
    crawler(gen(urls_avbl[n]))