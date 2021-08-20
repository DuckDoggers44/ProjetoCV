# Web Scraping Application

import requests
from bs4 import BeautifulSoup
import pandas as pd

list_posts = []

response = requests.get('https://g1.globo.com/economia/tecnologia/')

content = response.content

web = BeautifulSoup(content, 'html.parser')

#print(web.prettify())

posts = web.findAll('div', attrs={'class': 'bastian-feed-item'})

#print(posts)

#print(post.prettify())

for post in posts:

    title = post.find('a', attrs={'class': 'feed-post-link'})
    #print(title.text)
#print(post.prettify())
    
    subtitle = post.find('div', attrs={'class': 'feed-post-body-resumo'})

    if (subtitle):
       # print(subtitle.text)

        #print(title['href'])

     if (subtitle):
        list_posts.append([title.text, subtitle.text, title['href']])
     else:
        list_posts.append([title.text, '', title['href']])

news = pd.DataFrame(list_posts, columns=['Title', 'Subtitle', 'Link'])

news.to_excel('posts.xlsx', index=False)

#print(news)











#print('Status code:', response.status_code)
#print('Header')
#print(response.headers)

#print('/n Content')
#print(response.content)
#print(type(response.content))


