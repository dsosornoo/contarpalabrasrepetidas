import urllib.request
from collections import Counter


def word_counter(func):
    def counter(*args, **kwargs):
        data = func(*args, **kwargs)    
        total_words = data.split()
        stopwords = ['y','Y','la','de','una','los','me','No','con','que','el','un','es','en','Que','muy','al','a','él','le','quiere','A','da','faltan','Mas','bien']
        words = [word for word in total_words if word not in stopwords]
        wordcount = Counter(words)
        print('\n>>> TOP FIVE WORDS IN THIS SONG <<<\n')
        for w in wordcount.most_common(5):
            print(f"{w[0]}: {w[1]}")
    return counter


@word_counter
def text_reader(url):  
    data = urllib.request.urlopen(url).read().decode('utf_8') 
    return data



chilanga_banda = 'https://raw.githubusercontent.com/isabelyb/word_counter/main/chilanga_banda_lyrics.txt'
p_to = 'https://raw.githubusercontent.com/isabelyb/word_counter/main/pto.txt'
ciclon = 'https://raw.githubusercontent.com/isabelyb/word_counter/main/ciclon.txt'

# Output

text_reader(chilanga_banda)
# >>> TOP FIVE WORDS IN THIS SONG <<<
# bailan: 8
# tibiritábara: 8
# Pachucos: 4
# cholos: 4
# chundos: 4

text_reader(p_to)
# >>> TOP FIVE WORDS IN THIS SONG <<<
# Puto,: 26
# machino: 8
# Marica: 4
# nena: 4
# putino: 4

text_reader(ciclon)
# >>> TOP FIVE WORDS IN THIS SONG <<<
# rueda: 8
# vueltas: 7
# flecha: 6
# Gira: 6
# Dios: 3