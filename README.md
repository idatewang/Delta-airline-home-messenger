# Makes my home-sick friend feel a little bit better.
 
Due to COVID 19, it has become very hard to fly back to China from the US. Planes are limited and cancelled but the risk of catching virus during the flight remains high. This project is created for a friend who's tracking the lastest news on delta airline's official update page, and will give him a call using **twilio**'s awesome library for Python. It reads the website with **request** library, and it uses the **lxml** library to parse the html constantly provided with xpath to the elements.

It helps my friend makes decisions on ordering, cancelling or rescheduling as soon as there is any official news regarding the flights so it maximizes his chance of getting home, and at the same time he doesn't have to be on his phone all the time. It has brought both the good news and bad so far.
