from tkinter import *
from newsapi import NewsApiClient
window=Tk()
newsapi = NewsApiClient(api_key='YOUR API')
def query():
    global user_input,news_data
    label=Label(window,text="Enter the Topic Name Below",fg="black",width=100)
    label.pack()
    user_input=Entry(window,width=73,fg="red",font=(40))
    user_input.pack()
    user_submit_1=Button(window,text="MAIN HEADLINES",command=headlines,width=40)
    user_submit_1.pack()
    user_submit_2=Button(window,text="ARTICLES",command=articles,width=40)
    user_submit_2.pack()
    news_data=Text(window,width=115,fg="green",bg="black",height=140)
    news_data.pack()

def headlines():
    data=user_input.get()
    top_headlines = newsapi.get_top_headlines(q=data)
    data_1 = top_headlines['articles']
    news_data.delete(1.0, END)
    for i, article in enumerate(data_1):
        title = article.get('title', 'No title available')
        description = article.get('description', 'No description available')
        url = article.get('url', 'No URL available')
        news_data.insert(END,f"{i+1}. Title: {title}\nDescription: {description}\nURL: {url}\n")

def articles():
    data=user_input.get()
    all_articles = newsapi.get_everything(q=data)
    data_2 = all_articles['articles']
    news_data.delete(1.0, END)
    for i, article in enumerate(data_2):
        title = article.get('title', 'No title available')
        description = article.get('description', 'No description available')
        url = article.get('url', 'No URL available')
        news_data.insert(END,f"{i+1}. Title: {title}\nDescription: {description}\nURL: {url}\n")
window.config(background="black")
query()
window.mainloop()