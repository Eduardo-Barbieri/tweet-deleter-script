import tweepy as tw
import os
from IPython.core.display import HTML


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acess_token, Acces_token_secret)

api = tw.API(auth)

def delete_tweets():
    
    def get_user_statusses():
        user_id = api.me().id
        user = api.get_user(user_id)
        statuses_count = user.statuses_count 
        
        return(statuses_count,user)
        
    def deleter(statuses_count, user):
        
        x = 100
        if statuses_count-x<0:
            x = statuses_count
        
        delete = True
        
        while delete == True:
            
            #Must be enabled for the jupyter bug fix
            #try:
                for status in tw.Cursor(api.user_timeline, id=user).items(x):
                    api.destroy_status(status.id)
                    statuses_count = user.statuses_count

                    if statuses_count-x<0:
                            x = statuses_count
                else: 
                    delete = False

            #This part of code resets the jupyter kernel and fixed an error that happend when, 
            #after a certain number of requests, the code crashed.
            #PS 01: only works in jupyter notebook;
            #PS 02: the error may be due to weak set up;
            #PS 03: may not be necessary;    
            
            #except tw.TweepError:  
                   #HTML("<script>Jupyter.notebook.kernel.restart()</script>")

        print('Tweets deleted')
    
    statuses_count , user = get_user_statusses()
    deleter(statuses_count,user)

delete_tweets()