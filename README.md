# PDF2Excel Scraper

This is a simple script that scrapes pdf files and return excel files using tabula and pypdf2.

> This is given that there is a table on the pdf. If there isn't checkout the proof-of-concept to see how I did it for my case.

Since it didn't work for my case (there weren't tables in the pdf), I had to use regex to order the table headers.

## Normal usage
> !pip install tabula, PyPDF2
> python scrape.py
