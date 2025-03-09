import pandas as pd

df = pd.read_csv('films_info.csv')
genres_column = df['Genres']

all_genres = genres_column.str.cat(sep=', ')
words = all_genres.split(', ')

words = [word.strip() for word in words]
words = [word for word in words if word]

unique_words = set(words)
for word in unique_words:
    print(word)