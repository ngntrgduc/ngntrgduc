import requests
import random

CONTENT = \
"""
:book: I'm an ambivert junior at the University of Science - VNUHCM, Faculty of Mathematics and Computer Science </br>
:test_tube: I make [random stuff](https://github.com/ngntrgduc/projects), [blog](https://ngntrgduc.github.io/) whenever I have no deadline </br>
:seedling: I'm currently learning: ***Mathematics, Machine learning, and Deep Learning*** </br>
:dizzy: Fun fact: I love listening to [music](https://soundcloud.com/ngntrgduc), sipping coffee while making :bug: for my code </br>
:mailbox: Connect with me: [Facebook](https://fb.com/nguyenduc1511) | [LinkedIn](https://www.linkedin.com/in/ngntrgduc/) | [Email](mailto:trungducnguyen1511@gmail.com)

![](https://github.com/ngntrgduc/github-stats/blob/master/generated/overview.svg)
![](https://github.com/ngntrgduc/github-stats/blob/master/generated/languages.svg)
"""

result = requests.get('https://raw.githubusercontent.com/ngntrgduc/ngntrgduc.github.io/master/content/quotes.md').text
quotes = result.split('\n\n')[1:]

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(f'> ***{random.choice(quotes)[2:].strip()}***\n')
    f.write(CONTENT)
