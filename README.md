
Web scraping using beautiful soup(bs4)
This notebook includes data scraping, which takes a website URL as an input and extracts the information listed below as an output from that webpage.

Specific HTML tags along with titles and meta description
Extract specific tags, heading tags from h1-h6 along with titles and meta description
Extracting ALT tags
For counting words inside a web page
Inspection of broken links inside a webpage
Extracting the source code of the webpage in google colab
Extracting all URLs from a website without duplication
Measuring the forntend and backend performance of website

 For scraping specific HTML tags along with titles and meta description
#------------- Main ---------------#
if __name__ == '__main__':
  titleandmetaTags()
  tags = getTags('h1')
  for tag in tags:
     print(tag) # display tags 
     print(tag.contents) # display contents of the tags



what u wanted to disply just chnge the predefine code accordingly and print terminolgy as well in program.

example 1: 
For extracting specific tags, all heading tags from h1-h6 along with titles and meta description
#------------- Main ---------------#
if __name__ == '__main__':
  titleandmetaTags()
  tags = getTags('p')
  headtags = headingTags('h1')
  for tag in tags:
     print(" Here are the tags from getTags function:", tag.contents)
        

     
