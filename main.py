import pandas as pd
import matplotlib as md

listings=pd.read_csv('listingss.csv')

#Will be doing data cleaning - there are many null columns and rows

listings=listings.drop(listings.columns[[4,17]],axis=1)#gets rid of all columns with just null values (i.e, neighbourhood count and license)

listings.dropna(inplace=True)#gets rid of all rows with null columns

# Can now start solving problems

#First Problem - find people with the most amount of listings
#Will do this via user id
def mapping_people_with_listing(listings):
    pass