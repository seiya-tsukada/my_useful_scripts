# coding: utf-8

import webbrowser

url_list = list()
url_list = [
"https://medium.com/",
"https://www.vocabulary.com/",
"https://www.codecademy.com/learn"

]

for url in url_list:
    print ("open url: {0}".format(url))
    webbrowser.open_new_tab(url)
