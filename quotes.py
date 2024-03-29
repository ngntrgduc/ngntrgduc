from urllib.request import urlopen
import random

CONTENT = \
"""
<a href="https://github.com/ngntrgduc/github-stats">
  <img align="right" src="https://github.com/ngntrgduc/github-stats/blob/master/generated/overview.svg"/>
</a>

📖 I'm a junior at the University of Science - VNUHCM, majoring in Mathematics and Computer Science.

🧪 I make [random stuff](https://github.com/ngntrgduc/projects), [blog](https://ngntrgduc.github.io/) whenever I have no deadline (rarely).

🐧 Fun fact: ISFJ-A. Ambivert. Sleep-deprived. Xiangqi player. [Music](https://soundcloud.com/ngntrgduc). Coffee.
"""

url = 'https://raw.githubusercontent.com/ngntrgduc/ngntrgduc.github.io/master/content/quotes.md'
with urlopen(url) as response:
    result = response.read().decode('utf-8')
    quotes = result.split('\n\n')[1:]

with open('README.md', 'r', encoding='utf-8') as f:
    old_content = f.read()
    old_quote = old_content.split('\n\n')[0][5:-3]

new_quote = random.choice(quotes)[2:].strip()
while new_quote == old_quote:
    new_quote = random.choice(quotes)[2:].strip()

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(f'> ***{new_quote}***\n')
    f.write(CONTENT)
