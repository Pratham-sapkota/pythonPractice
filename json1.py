import json
import urllib.request,urllib.parse,urllib.error

serviceurl='https://maps.googleapis.com/maps/api/js?'

while True:
    address=input('ENter location:')
    if len(address)<1:break
    
    url=serviceurl+urllib.parse.urlencode({'address':address})

    print('retreiving',url)
    uh=urllib.request.urlopen(url)
    data=uh.read().decode()
    print('retrieved',len(data),'characters')

    try:
        js=json.loads(data)
    except:
        js=None
    if not js or 'status' not in js or js['status']!='OK':
        print('===failure to retrieve===')
        print(data)
        continue
    print(json.dumps(js,indent=4))

    #lat=js["results"]
