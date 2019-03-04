import  urllib.request
import json

cid = input("Enter Youtube Channel ID:")
key = "YOUR API KEY GOES HERE"

data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&id="+cid+"&key="+key).read().decode('utf-8')

cdesc = json.loads(data)["items"][0]["snippet"]["description"]
ctitle = json.loads(data)["items"][0]["snippet"]["title"]
cviews = json.loads(data)["items"][0]["statistics"]["viewCount"]
csubs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]

print("Channel Name:",ctitle)
print("Channel Decription:",cdesc)
print("Total Views: {:,d}".format(int(cviews)))
print("Total Subscribers: {:,d}".format(int(csubs)))
