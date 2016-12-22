 ![CANOE](https://github.com/anyakeller/JSONmohabir_MohabirJ-FichterN-FreyraJ-KelllerA/blob/master/static/img/logo.png "The original boat png credit goes to https://thenounproject.com/term/canoe/64735/ thanks!  We added the logo text.") 
by JSONMohabir
===============================================
- [About] (#about)
- [Usage] (#usage)
- [Known Bugs] (#known-bugs)

About
----------
Canoe [kæn-o-e], our project, is a website that utilizes 5 APIs to help the user find the event tickets that best suit their requirements.  The user inputs the type of event they are looking for, the price range, and the numbers of seats, and the site displays a list of the different ticket options. Other parameters can be also selected in dropdown menu to refine the search. The default sorting for the list is by relevance but the user can change that to highest price, lowest price, and date of event. The ticket options that fulfill the input criterion will be displayed in on a paginated output that include the ticket seller, event name, date / time, price and  seat number.  The results per page are are capped at 10 so if the number of results goes over that limit, there is an option to see the next page of results.  

Usage
----------
To run website from terminal:
- make sure flask is installed
- make sure python-dateutil is installed (pip install python-dateutil)
- make sure requests is installed (pip install requests)
- make sure keys.csv is in main direcotry
 - keys.csv should be formatted: name,key
- run: $python app.py
- open a browser to 27.0.0.1:5000

Known Bugs
----------
