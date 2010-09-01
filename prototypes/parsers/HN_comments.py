import httplib2
from BeautifulSoup import BeautifulSoup


def HN_comments(username):
"""
Basic prototype for pulling comments off of HN. Needs some more features still, mainly timestamps, but should provide a decent base for a Hacker News class. Pulling submissions should be pretty similar.
"""

    all_comments = []
    h = httplib2.Http(".cache")
    base_url = "http://news.ycombinator.com/threads?id="
    username = str(username)
    url = base_url + username

    response, content  = h.request(url)

    soup = BeautifulSoup(content)
    headings = soup.findAll("span", {"class":"comhead"})

    for heading in headings:
        comment_anchors = []
        for a in heading('a'):
            comment_anchors.append(a)
    
        if (len(comment_anchors) == 4):
            submission_title = comment_anchors[3].string

            comment = {}
            comment['user'] = comment_anchors[0].string
            comment['link'] = comment_anchors[1]['href']
            comment['submission_title'] = submission_title
            all_comments.append(comment)

    return all_comments

username = 'chunkbot'
all_comments = HN_comments(username)
for comment in all_comments:
    print comment
    print '\n'
