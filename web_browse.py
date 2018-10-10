# coding: utf-8

import webbrowser

url_list = list()
url_list = [
"https://www.nw-siken.com/",
"https://medium.com/",
"https://www.vocabulary.com/",
"https://www.codecademy.com/learn",
"http://overthewire.org/wargames/"

]

for url in url_list:
    print ("open url: {0}".format(url))
    webbrowser.open_new_tab(url)
