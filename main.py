import pandas as pd
import matplotlib.pyplot as plt


def cleaning_data(listings):
    #Will be doing data cleaning - there are many null columns and rows

    listings=listings.drop(listings.columns[[4,17]],axis=1)#gets rid of all columns with just null values (i.e, neighbourhood count and license)

    return listings.dropna()#gets rid of all rows with null columns

# Can now start solving problems

#First Problem - bar chart showing relationship between neighbourhood and price
def price_by_neighbourhood(listings):
    #Calculate the average price by neighbourhood
    average_price=listings.groupby('neighbourhood')['price'].mean().sort_values(ascending=False)
    # Plot the results
    average_price.plot(kind="bar",title="Average price by neighbourhood")
    plt.ylabel("Average Price")
    plt.xlabel("London Borough")
    plt.tight_layout()
    plt.show()
    """
    Describe Findings here so I can write them in the readme

    First summary is:

    Find that City Of London, Westminister and Kensington and Chelsea are signficant outliers with prices 250+ per night
    All the others are roughly the same price, with them decreasing slowly ranging from 180 to 80 per night
    """

def plot_avg_minimum_nights_by_neighbourhood(listings):
    # Calculate the average minimum nights required per neighbourhood
    avg_min_nights = listings.groupby("neighbourhood")["minimum_nights"].mean().sort_values(ascending=False)
    # Plot the results
    avg_min_nights.plot(kind="bar", title="Average Minimum Nights by Neighbourhood")
    plt.xlabel("London Borough")
    plt.ylabel("Average Minimum Nights")
    plt.tight_layout()
    plt.show()
    """
    Greenwhich and Tower Hamlets have the highest minimum nights (8 days average)
    Sutton is the lowest (3 days average)
    The others decrease slowly
    """

def main():
    listings=pd.read_csv('listingss.csv')
    cleaned_listings=cleaning_data(listings)
    price_by_neighbourhood(cleaned_listings)
    plot_avg_minimum_nights_by_neighbourhood(cleaned_listings)

main()