import requests
imageurl = "http://forsk.in/images/Forsk_logo_bw.png"
r = requests.get(imageurl)
f = open("Forsk_logo_bw.png",'wb')
f.write(r.content)
f.close()
