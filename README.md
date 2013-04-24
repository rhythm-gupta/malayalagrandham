Malayala Grandha Vivaram
========================

Sourcecode and database of malayalagrandham.com der 
Django source is licensed under AGPLv3
Gandham DB is licensed Under GPLv3


File structure
--------------

server/passenger_wsgi.py   => Server configuration required in production mode.
db/smc_bib.sql.gz 				=> DB Dump as on 6th April 2013. 
grandham/         				=> Source


TODOs
-----
06-04-2013
----------
Bump up the Django version - will change all the directory structure.
Error handling - Currently the error handling is very minimum.
Follow CURD - Search is currently POST and not GET. Look out for more.
Pagination - Search results are not paginated.
Better layout - Work on a better layout.
Optimization - Coding was done without caring much about best practises nor is it optimized. 



Credits
-------
    Centre for South Indian Studies, Thiruvanathapuram
    Beehive Digital Concepts, Cochin
    Swathanthra Malayalam Computing (SMC)
    Compilation and General Editor: K.M. Govi
    Structuring and Classifying: K.H. Hussain
    Programming: K.P.N. Unni (Kriyate)
    Systemization: Mahesh M. (Kriyate)
    Project Co-ordination: Dr. R. Raman Nair

MalayalaGrandhaVivaram Task Force on Bibliographic Data Updation
----------------------------------------------------------------
    K.M. Govi (Chairman)
    K.H. Hussain (Convenor)
    Lalitha Lenin
    Dr. R. Raman Nair
    K. Rajendran
    P.M. Abdul Kadir
    Anivar Aravind
