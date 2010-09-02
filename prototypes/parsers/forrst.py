import urllib2
import json
from parsers import BaseParser, BaseFeedItem

class ForrstParser(BaseParser):
    '''
    A parser for forrst user's code posts based on GitHubParser.
    The API is still very young and could change at any time. http://forrst.com/apidocs.html

    Retrieves all public posts of type 'code' of the user.

    Since Forrst is invite-only (at the time of writing),
    only posts marked as 'public' can be retrieved by the API.
    '''
    url_prefix = 'http://api.forrst.com/api/v1/users/posts?username='
    post_type = 'code'
    title_tag = 'title'
    link_tag = 'post_url'
    timestamp_tag = 'created_at'
    post_type_tag = 'post_type'

    def run(self):
        forrst_list = []
        try:
            posts = urllib2.urlopen(self.url_prefix + self.username)
        except HTTPError as e:
            if e.code == 404:
                raise e
            else:
                raise e

        tree = json.load(posts)

        for post in tree['resp']['posts']:
            if post[self.post_type_tag] == self.post_type:
                timestamp = post[self.timestamp_tag]
                title = post[self.title_tag]
                link = 'http://forrst.com' + post[self.link_tag]

                item = BaseFeedItem(timestamp, title, link)
                forrst_list.append(item)

        return forrst_list


