import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize

sample_text ='I Love Programming!'
tokens= word_tokenize(sample_text)

print('Tokens: ', tokens)

