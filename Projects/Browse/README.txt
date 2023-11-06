•	Usage
	Initializing the Browser History
o	To start tracking a user's browsing history, you need to create an instance of the `userBrowser` class. This instance will store the browsing history for the user.
	Recording URLs
o	You can record visited URLs using the `url_records` method. This method allows you to add a URL to the user's browsing history.
o	If the URL is already in the history, it will be moved to the top of the history, ensuring that the most recently visited URL is at the beginning.
	Retrieving User History
o	You can retrieve the user's browsing history using the `user_history` method. This method returns a list of URLs in the order they were visited, with the most recent URL at the beginning of the list.
