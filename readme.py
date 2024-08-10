import feedparser
import time

URL = "http://eunajung01.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POSTS = 5

markdown_text = """## 🐟
![header](https://capsule-render.vercel.app/api?type=waving&color=0:FFFFFF,100:674b61&height=170&section=header)

<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FeunaJung01&count_bg=%23674B61&title_bg=%23332A2A&icon=&icon_color=%23E7E7E7&title=hello&edge_flat=false"/></a>

이화여자고등학교 131기  
건국대학교 컴퓨터공학부 20학번

### Latest Blog Posts
"""

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POSTS:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"- [{time.strftime('%Y-%m-%d', feed_date)}: {feed['title']}]({feed['link']}) <br/>\n"

markdown_text += """
[![Solved.ac 프로필](http://mazassumnida.wtf/api/v2/generate_badge?boj=christinejung10)](https://solved.ac/christinejung10)
"""

f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
