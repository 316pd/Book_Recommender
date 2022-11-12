import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests
from itertools import cycle

def fetch_poster(books_name):
    return books_image['Image-URL-M'][books_name]

def recommend_books(books):
  recommend_list = []
  recommend_posters = []
  index = pt.index(books)
  sim_books = sorted(list(enumerate(books_dict[index])), key=lambda x:x[1], reverse=True)[1:9]
  for i in sim_books:
    recommend_list.append(pt[i[0]])
    recommend_posters.append(fetch_poster(pt[i[0]]))
  return recommend_list, recommend_posters

books_dict = pickle.load(open('books_dict.pkl',"rb"))
books_image = pickle.load(open('books_image.pkl',"rb"))
pt = pickle.load(open('pt.pkl',"rb"))

books_list = books_image['Image-URL-M'].keys()

st.title('Book Recommendation System')
select_book_name = st.selectbox('Select the Book you liked', books_list)

if st.button('Recommend'):
    names, posters = recommend_books(select_book_name)
    cols = cycle(st.columns(4)) # st.columns here since it is out of beta at the time I'm writing this
    for idx, filteredImage in enumerate(posters):
        next(cols).image(filteredImage, width=150, caption=names[idx])