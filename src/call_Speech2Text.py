import urllib.request
import http
def speech2text(feedid_list):
    url='10.51.179.116'

    h1=http.client.HTTPConnection(url,8080,timeout=500)

    url_rest='/getsubtitle?feedids'
    #for feedid in feedid_list:
    #    url_rest+=feedid+'|'
    #url_rest=url_rest.strip('|')
    h1.request('GET','/')
    res=h1.getresponse()
    print(res.status,res.reason)
    data=res.read()
    print(data)



feed_id=['Bpveyrl6Rfs0AM12gRgBII','BpvgQvhNy8pgew3Ca5l1BZ']
speech2text(feed_id)
