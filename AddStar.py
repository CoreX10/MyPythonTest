#! python3

"""
clipboard content：

Lists of animails
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
"""

import pyperclip

BeginWords = pyperclip.paste()
list_words = BeginWords.split('\n')
for i in range(len(list_words)):
    list_words[i] = ' * '+list_words[i]
EndWords = '\n'.join(list_words)
pyperclip.copy(EndWords)
