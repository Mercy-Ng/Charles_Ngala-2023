#this is userBrowser class, which has an __init__ method used to initialize an empty list called history to store the browsing history.
class userBroweser:
    def __init__(self):
        self.history = []
    
    #this method is used to record URLs. It takes a URL as an argument,
    #  and if the URL is already in the history, 
    # it removes the previous occurrence of that URL 
    # and inserts it at the beginning of the history list.
    def url_records(self, url):
        if url in self.history:
            self.history.remove(url)
        self.history.insert(0, url)
    
    #This method or function simply returns the current browsing history.
    def user_history(self):
        return self.history
    
history = userBroweser()  #This is an instance of the userBrowser class

#example
#urls_visited: msn.com => google.com => facebook.com => google.com
#● history: google.com => facebook.com => msn.com
history.url_records("msn.com")
history.url_records("google.com")
history.url_records("facebook.com")
history.url_records("google.com")
history.url_records("facebook.com")
#history.url_records("msn.com")

hist = history.user_history()  #retrieve and store the browsing history

print("History: ", hist) #print out the browsing history