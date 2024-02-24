from urllib.request import urlopen
import random

CONTENT = \
"""
<a href="https://github.com/ngntrgduc/github-stats">
  <img align="right" src="https://github.com/ngntrgduc/github-stats/blob/master/generated/overview.svg"/>
</a>

📖 I'm an ambivert junior at the University of Science - VNUHCM, Faculty of Mathematics and Computer Science </br>
🧪 I make [random stuff](https://github.com/ngntrgduc/projects), [blog](https://ngntrgduc.github.io/) whenever I have no deadline </br>
🌱 I'm currently learning: Mathematics, Machine learning, and a bit of Computer science </br>
💫 Fun fact: I love listening to [music](https://soundcloud.com/ngntrgduc), sipping coffee while making 🐛 for my code </br>
📫 Connect with me: [Facebook](https://fb.com/nguyenduc1511) | 
[LinkedIn](https://www.linkedin.com/in/ngntrgduc/) | 
[Email](mailto:trungducnguyen1511@gmail.com)
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
