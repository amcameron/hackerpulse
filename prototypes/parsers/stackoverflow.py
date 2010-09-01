try:
    import json
except ImportError:
    import simplejson as json
import urllib2
import StringIO, gzip

# API endpoint
# http://api.stackoverflow.com/1.0/users/{user_id}/timeline
#
# Notes:
# -has all relevant activity that we should need
# -the user_id can be obtained with additional API requests
#     or we can just make the user enter it for now
# 
# Limitations:
# -per IP-basis
# -limits: 300 per day anonymous, 10000 per day with key (should use a key)
# -keep requests limited to 30 requests per 5 seconds

def run(user_id):
    url = "http://api.stackoverflow.com/1.0/users/%s/timeline" % user_id

    #urllib2 doesnt play nicely with gzip and all SO responses are gzipped
    request = urllib2.Request(url, headers={'Accept-Encoding': 'gzip'})
    req_open = urllib2.build_opener()

    #get the response
    gzipped_data = req_open.open(request).read()

    #build a buffer to decompress into
    buffer = StringIO.StringIO(gzipped_data)
    gzipper = gzip.GzipFile(fileobj=buffer)

    #a dictionary of the data
    return json.loads(gzipper.read())
    

if __name__ == '__main__':
    data = run(184609) #swanson's user_id
    
    for item in data['user_timelines']:
        print item['action'], item['description'], item['creation_date']
