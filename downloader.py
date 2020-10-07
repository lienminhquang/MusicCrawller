import wget
 
file = open("./urls_full.txt", "r")
lines = file.readlines()
file.close()

for url in lines:
    url = url.split('\n')[0]
    name = url.split('/')[-1]

    print("\nDownloading " + url)
    wget.download(url,"../playlist/"+name)
    
    #r = requests.get(url, allow_redirects=True)
    #open("../playlist/"+name, 'wb').write(r.content)
