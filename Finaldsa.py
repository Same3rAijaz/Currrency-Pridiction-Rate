from bs4 import BeautifulSoup
import pandas as pd
import requests
from datetime import datetime
from collections import OrderedDict

url='https://www.exchangerates.org.uk/USD-PKR-exchange-rate-history-full.html'



r = requests.get(url)

html_content = r.text

soup = BeautifulSoup(html_content,"html.parser")
i=1


tss = soup.find('table').find_all('tr', attrs={'class':'colone'})
tss += soup.find('table').find_all('tr', attrs={'class':'coltwo'})
# data = {'Date':[],'Rate':[]}
data = {}
for trs in tss:
    i=i+1
    if trs.text.split(" ",-1)[7]=="PKRUSD":
        data[trs.text.split(" ",-1)[-1]] = trs.text.split(" ",-1)[6]
#         data["Date"].append(trs.text.split(" ",-1)[-1])
#         data["Rate"].append(trs.text.split(" ",-1)[6])
#         date=({"Date":trs.text.split(" ",-1)[-1],"Rate":trs.text.split(" ",-1)[6]})
#         dates.append(date)
    else:
        data[trs.text.split(" ",-1)[-1]] = trs.text.split(" ",-1)[7]
#         data["Date"].append(trs.text.split(" ",-1)[-1])
#         data["Rate"].append(trs.text.split(" ",-1)[7])
        
ordered_data = sorted(data.items(), key = lambda x:datetime.strptime(x[0], '%d/%m/%Y'))
final_data = dict(ordered_data)
full_data = {"Date":list(final_data.keys()),"Rate":list(final_data.values())}
full_data
fdata = pd.DataFrame(full_data)
fdata.to_csv('DatasetDLRtoPKR.csv',index=False)
# ffdata =fdata.to_dict(orient='split')
# ffdata
        
#         date=({"Date":trs.text.split(" ",-1)[-1],"Rate":trs.text.split(" ",-1)[7]})
#         dates.append(date)

# ordered_data = OrderedDict(
#     sorted(dates[].items(), key = lambda x:datetime.strptime(x[0], '%d-%m-%Y')) )

# dates
