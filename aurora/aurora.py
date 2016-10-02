import praw
import time


from praw.helpers import comment_stream


r = praw.Reddit("Simpsons Aurora Borealis")
r.login()

target_text = "Aurora Borealis"
response_text = """The aurora borealis? 

At this time of year? 

At this time of day? 

In this part of the country? 

Localized entirely within your kitchen?"""



processed = []
while True:
    for c in comment_stream(r, 'all'):   #posting to all subreddits! it is ok if a few subs end up banning me
        if target_text in c.body and c.id not in processed: #if find comment not in cache
            print('Seymour the house is on fire! :@')
            c.reply(response_text)
            processed.append(c.id)   #then push the response 
            time.sleep(10)
    

