'''
This file is to download the pdfs from the conference day and translate the abstracts into Chinese.


Author: Yifu Liu

'''

import requests 
from bs4 import BeautifulSoup
from hashlib import md5
import random
import re
import json
def translate_api(input_text):
    # Set your own appid/appkey.
    appid = '20230313001597935'
    appkey = 'wB4JNZosLeez2G3Vbx_k'
    def make_md5(s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()
    # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
    from_lang = 'en'
    to_lang = 'zh'
    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path

    query = 'Hello World! This is 1st paragraph.\nThis is 2nd paragraph.'

    # Generate salt and sign
    def make_md5(s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)

    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()

    return json.dumps(result, indent=4, ensure_ascii=False)

def getAbstract(paperUrls):
    abstract = []
    for url in paperUrls:
        response = requests.get(url)
        bs = BeautifulSoup(response.text,"html.parser")
        abstract.append(bs.find(id="abstract").text.strip())
    return abstract

def translate_abstracts(abstracts):
    translated_abstracts = []
    for abstract in abstracts:
        translated = translate_api(abstract)
        translated_abstracts.append(translated)

    return translated_abstracts

def write2txt(path,title,raw_text,contents):
    with open(path,"w") as f:
        for ti,raw,con in zip(title,raw_text,contents):
            f.write(ti+"\n")
            f.write(raw+"\n")
            f.write(con+"\n")
            f.write("\n")

def getUrl(url):
    response = requests.get(url)
    pdfUrl = []
    count = 0
    bs = BeautifulSoup(response.text,"html.parser")
    pdfs = bs.find_all(href=re.compile('/content/.*html'))
    names = []
    for tag in pdfs:
        if count < 20: 
            pdfUrl.append("https://openaccess.thecvf.com"+tag.get("href"))
            count = count+1
            names.append(re.split('[./]', tag.get("href"))[-2][:-16].replace("_"," "))
        else: break
    return names,pdfUrl
# URL of the conference day
url = 'https://openaccess.thecvf.com/ICCV2021?day=2021-10-12'



url_list = getUrl(url)
print(url_list)
# Extract, translate, and write abstracts
names,pdfurls = url_list
abstracts = getAbstract(pdfurls)
translated_abstracts = translate_abstracts(abstracts)
write2txt("abstract.txt",names,abstracts,translated_abstracts)
