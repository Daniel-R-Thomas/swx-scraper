# swx-scraper

### About 
This program was written by Daniel Thomas during the Spring 2018 semester internship with SOFWERX. The intent of the program is to collect data on multiple platforms to link together relevant crime information, Local FaceBook events, and users from FaceBook. This information compiled together will ultimately give a better insight of the area around a specific location and the potential to identify events of interest based on the compiled data. It should be noted that the programming and imports used aren't the only way to accomplish this or maybe themost efficient, but it works and could easily be reused for other areas. 

### How to run 
Install pip:
`sudo apt-get install python-pip python-dev build-essential`

Install requirements (same directory):
`pip install -r req.txt`

Accounts:
Two options for storing account information. Either save account information as “username (newline no spaces) password” and modify FBGeneralCode.py -> accountFetch(infoType) -> accountFile’s directory to the new one setup. Second option is to have the function return the fbUsername and fbPassword as strings directly. This method is not recommended due to how easy it would be to accidentally upload account information.

![alt text](https://github.com/Daniel-R-Thomas/swx-scraper/blob/master/images/image5.png)

Change line 18 above to account.txt’s new directory

Or

![alt text](https://github.com/Daniel-R-Thomas/swx-scraper/blob/master/images/image9.png)

Directly return password (not recommended) 

Changing location in crime data search:
Currently the program is defaulted to Tampa, FL. To change the location, open lexis.py and copy the new URL location to the line before. Or simply edit and replace the current location on line 14.

![alt text](https://github.com/Daniel-R-Thomas/swx-scraper/blob/master/images/image3.png)

Changing location in address search:
The location in the users address search is also currently listed in the Tampa area. To change this, open the tree.py and change the remaining part of the URL to the new city and state.

![alt text](https://github.com/Daniel-R-Thomas/swx-scraper/blob/master/images/image6.png)

Line 26

Running (same directory):
`python main.py` in linux terminal


