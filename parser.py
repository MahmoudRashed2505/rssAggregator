import feedparser

print()
with open('url.txt') as file:
    urls = file.readlines()
    for url in urls:
        feed = feedparser.parse(url)
        print()
        print(url)
        print()
        for entry in feed.entries:
            print("Title: {}\nPublished Date: {}\nLink: {}\n".format(entry['title'],entry['published'],entry['link']))
