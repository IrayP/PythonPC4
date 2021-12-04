import re

s = "Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 9, number of retweets: 7"
patron1 = r"User_mentions:\s*\d"
print(re.findall(patron1,s))

patron2 = r"likes:\s*\d"
print(re.findall(patron2,s))

patron3 = r"number of retweets:\s*\d"
print(re.findall(patron3,s))
