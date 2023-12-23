import requests
import re
from bs4 import BeautifulSoup as BS

url = "https://itemscout.io"
agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"

response = requests.get(url = url, headers = {"User-Agent":agent})

if response.status_code == 200:
    # html = requests.get(url).content
    # bsObj = BS(re.sub("<!--|-->","", html), "lxml")
    # officials = bsObj.find_all("table")

    # print(officials)

    res_text = response.text
    res_content = response.content
    parsed_res_text = BS(res_content, features="html.parser")
    print(parsed_res_text.prettify())
    print(parsed_res_text.find("ul"))

else:
    print(response.status_code)
print(type(response))