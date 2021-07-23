import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
print(res)
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.head)
# print(soup.find_all('div'))
# print(soup.find_all('a'))
# print(soup.title)
# print(soup.find(id="score_27922728"))
# print(links, votes)
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def sorted_news(news_list):
    return sorted(news_list, key=lambda k: k['points'], reverse=True)


def custom_news(links, subtext):
    news = []
    news_links = []
    point_list = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        story_links = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points >= 100:
                # news.update(
                #     {'title': title, 'link': story_links, 'points': points})
                news.append(title)
                news_links.append(story_links)
                point_list.append(vote[0].getText().replace(' points', ''))
            # print(point_list)
    count = 0
    # for i, x, y in map(news, news_links, point_list):
    #     print(f'Title: {i} \nlink: "{x}" \npoints {y}.')
    #     print('\n')
    for i in (news):
        print(
            f'Title: {i} \nlink: "{news_links[count]}" \npoints {point_list[count]}.')
        print('\n')
        count = count + 1
    #     print(i)
    # print('')
    # return sorted_news(news)


# pprint.pprint(custom_news(links, subtext))
print(custom_news(links, subtext))
