# Web Scraping Application

import requests
from bs4 import BeautifulSoup
import pandas as pd
from tkinter import *
from tkinter import tix
from PySimpleGUI import PySimpleGUI
from time import sleep




list_posts = []

def web_scrapping():
   response = requests.get('https://g1.globo.com/economia/tecnologia/')

   content = response.content

   web = BeautifulSoup(content, 'html.parser')

   sleep(5)
#print(web.prettify())

   posts = web.findAll('div', attrs={'class': 'bastian-feed-item'})

   sleep(5)

   print(posts)

#print(post.prettify())

   for post in posts:

      title = post.find('a', attrs={'class': 'feed-post-link'})
      print(title.text)
#print(post.prettify())
      
      subtitle = post.find('div', attrs={'class': 'feed-post-body-resumo'})

      if (subtitle):
         print(subtitle.text)

         print(title['href'])

         if (subtitle):
            list_posts.append([title.text, subtitle.text, title['href']])
         else:
            list_posts.append([title.text, '', title['href']])

         news = pd.DataFrame(list_posts, columns=['Title', 'Subtitle', 'Link'])
         news.to_excel('posts.xlsx', index=False)

print()



def close():
   exit()

window_news = Tk()

window_news.title("Notícias Recentes")
window_news.geometry('600x400')

title_text = Label(window_news, text="Title")
title_text.grid(column=0, row=0)


subtitle_text = Label(window_news, text="Subtitle")
subtitle_text.grid(column=1, row=0)


link_text = Label(window_news, text="Link")
link_text.grid(column=2, row=0)

button_close = Button(window_news, text="Close", command=close)
button_close.grid(column=0, row=800)


button_execute = Button(window_news, text="Execute", command=web_scrapping)
button_execute.grid(column=8, row=800)

info_scrapping = Label(window_news, text="" )
info_scrapping.grid(column=0, row=1)

window_news.mainloop()



#print('Status code:', response.status_code)
#print('Header')
#print(response.headers)

#print('/n Content')
#print(response.content)
#print(type(response.content))


