from MaltegoTransform import *
import json,requests
emailT=sys.argv[1]
import os
trx = MaltegoTransform()
from holehe import *
import random
import string

websites=[adobe,ebay,facebook,instagram,tumblr,pastebin,github,twitter,pinterest,lastfm,spotify,firefox,office365,live]
for website in websites:
    infos=website(emailT)
    i=str(website).split(" ")[1].split(" ")[0]
    if infos["exists"]==True:
        web = trx.addEntity("megadose."+i,"Found")
        if infos["emailrecovery"]!= None:
            email = trx.addEntity("maltego.EmailAddress",infos["emailrecovery"])
            email.setLinkLabel("Found in "+i)
        if infos["phoneNumber"]!= None:
            email = trx.addEntity("maltego.PhoneNumber",infos["phoneNumber"])
            email.setLinkLabel("Found in "+i)
        if infos["others"]!= None:
            if "@" not in infos["others"]["FullName"]:
                email = trx.addEntity("maltego.Person",infos["others"]["FullName"])
                email.setLinkLabel("Found in "+i)
            reandom =''.join(random.choice(string.ascii_lowercase) for i in range(30))
            params = (
                ('source', 'indexpage'),
                ('url', infos["others"]["profilePicture"]),
                ('alias', reandom),
            )
            response = requests.get('https://tinyurl.com/create.php', params=params)
            web.setIconURL("https://tinyurl.com/"+reandom)
print(trx.returnOutput())
