# Project for Software Security course


To run on mac: python3 main.py
- when paying bill, credit card number is 1234123412341234

need to install cryptography library: pip3 install cryptography

NOTE: When viewing results, must close program completely to see each result for each date
because there is a bug that shows an empty window when trying to view a different date's result
after viewing a result.

Security use case implemented was encryption for questions file
    - I could not get decryption to work for refill.csv and payment.csv file
    - I also skipped authenticating patient for each use case as it would make working the gui 
    annoying and would be unnecessary if 2FA were implemented during the login use case
