import feedparser

URL = "http://eunajung01.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POSTS = 5

markdown_text = """## 🐟
### Latest Blog Posts
"""

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx >= MAX_POSTS:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"- [{feed['title']}]({feed['link']}) <br/>\n"

markdown_text += """
[![Solved.ac 프로필](http://mazassumnida.wtf/api/v2/generate_badge?boj=christinejung10)](https://solved.ac/christinejung10)
"""

f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
