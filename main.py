import pandas as pd
import matplotlib.pyplot as plt

"""
Need to deal with:

The report (i.e the README)
Make plots much more readable
Adjust the labels, especially for the later ones
"""

def cleaning_data(listings):
    #Will be doing data cleaning - there are many null columns and rows

    listings=listings.drop(listings.columns[[4,17]],axis=1)#gets rid of all columns with just null values (i.e, neighbourhood count and license)
    listings=listings[listings["price"] < 1500]
    listings=listings[listings["minimum_nights"] < 50]
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
    Summary Statistics
    Greenwhich and Tower Hamlets have the highest minimum nights (8 days average)
    Sutton is the lowest (3 days average)
    The others decrease slowly
    """

def price_by_reviews_per_month_scatter(listings):#will be a scatter chart
    # Calculate the average minimum nights required per neighbourhood
    # Plot the results
    listings.plot(kind="scatter", title="Reviews Per Month Relation To Price",x="reviews_per_month",y="price")
    plt.xlabel("Reviews Per Month")
    plt.ylabel("Price (£)")
    plt.tight_layout()
    plt.show()
    """
    Summary Statistics
    Shows there is no relation between price and the number of reviews per month
    """

def price_by_reviews_per_month_bar(listings):#will be a bar chart
    # Calculate the average minimum nights required per neighbourhood
    # Plot the results
    reviews_per_month_avg_price=listings.groupby("reviews_per_month")["price"].mean().sort_values(ascending=False)
    reviews_per_month_avg_price.plot(kind="bar", title="Reviews Per Month Relation To Price")
    plt.xlabel("Reviews Per Month")
    plt.ylabel("Price (£)")
    plt.tight_layout()
    plt.show()
    """
    Summary Statistics
    Shows there is no relation between price and the amount of reviews per month
    """

def price_by_reviews_scatter(listings):#will be a scatter chart
    # Plot the results
    listings.plot(kind="scatter", title="Number of Reviews Relation To Price Scatter Plot",x="number_of_reviews",y="price")
    plt.xlabel("Number Of Reviews")
    plt.ylabel("Price (£)")
    plt.tight_layout()
    plt.show()
    """
    Summary Statistics
    Shows there is no relation between price and the amount of reviews, can be calculated using correlation
    """

def price_by_reviews_bar(listings):#will be a bar chart
    # Calculate the average minimum nights required per neighbourhood
    # Plot the results
    reviews_avg_price=listings.groupby("reviews_per_month")["price"].mean().sort_values(ascending=False)
    reviews_avg_price.plot(kind="bar", title="Reviews Per Month Relation To Price")
    plt.xlabel("Number Of Reviews")
    plt.ylabel("Price (£)")
    plt.tight_layout()
    plt.show()
    """
    Summary Statistics
    Shows low price means high price and many reviews means low price, but this price is very close to a review count significantly lower.
    """

def number_of_reviews_by_reviews_per_month_scatter(listings):#will be a scatter chart
    # Plot the results
    listings.plot(kind="scatter", title="Number of Reviews Relation To Reviews Per Month Scatter Plot",x="number_of_reviews",y="reviews_per_month")
    plt.xlabel("Number Of Reviews")
    plt.ylabel("Reviews Per Month")
    plt.tight_layout()
    plt.show()
    """
    Summary Statistics
    Very Slight Correlation but not significant -correlation is 0.45
    """

def price_by_min_nights(listings):
    #Calculate the average price by neighbourhood
    average_price=listings.groupby('minimum_nights')['price'].mean().sort_values(ascending=False)
    # Plot the results
    average_price.plot(kind="bar",title="Average price by minimum nights")
    plt.ylabel("Average Price")
    plt.xlabel("Minimum Nights")
    plt.tight_layout()
    plt.show()

def price_by_availability_bar(listings):
    #Calculate the average price by neighbourhood
    average_price=listings.groupby('availability_365')['price'].mean().sort_values(ascending=False)
    # Plot the results
    average_price.plot(kind="bar",title="Average price by availability")
    plt.ylabel("Average Price")
    plt.xlabel("Availability")
    plt.tight_layout()
    plt.show()

def availability_by_minimum_nights_scatter(listings):
    #Calculate the average price by neighbourhood
    # Plot the results
    listings.plot(kind="scatter",title="Availability by minimum nights",x="availability_365",y="minimum_nights")
    plt.ylabel("Minimum Nights")
    plt.xlabel("Availability")
    plt.tight_layout()
    plt.show()

def price_by_availability_scatter(listings):
    #Calculate the average price by neighbourhood
    listings.plot(kind="scatter",title="Availability by price",x="availability_365",y="price")
    # Plot the results
    plt.ylabel("Average Price")
    plt.xlabel("Availability")
    plt.tight_layout()
    plt.show()

def price_by_room_type(listings):
    #Calculate the average price by neighbourhood
    average_price=listings.groupby('room_type')['price'].mean().sort_values(ascending=False)
    # Plot the results
    average_price.plot(kind="bar",title="Average Price by Room Type")
    plt.ylabel("Average Price")
    plt.xlabel("Room Type")
    plt.tight_layout()
    plt.show()
    """
    Unsurprising statistics - a shared room is less expensive than a hotel room
    """

def ppl_w_highest_avg_price(listings):
    #Calculate the average price by neighbourhood
    average_price=listings.groupby('host_id')['price'].mean().sort_values(ascending=False)
    average_price=average_price.head(10)

    # Plot the results
    average_price.plot(kind="bar",title="Average Price by Host")
    plt.ylabel("Average Price")
    plt.xlabel("Host ID")
    plt.tight_layout()
    plt.show()
    """
    Bugged Pricing Column
    """

def most_amount_of_listings_vs_highest_avg_price(listings):
    #Calculate the average price by neighbourhood
    average_price=listings.groupby('calculated_host_listings_count')['price'].mean().sort_values(ascending=False)
    highest_average_price=average_price.head(10)
    lowest_average_price=average_price.tail(10)

    # Plot the results
    highest_average_price.plot(kind="bar",title="Average Price by Host")
    plt.ylabel("Average Price")
    plt.xlabel("Listings amount")
    plt.tight_layout()
    plt.show()

    lowest_average_price.plot(kind="bar",title="Average Price by Host")
    plt.ylabel("Average Price")
    plt.xlabel("Listings amount")
    plt.tight_layout()
    plt.show()
    """
    Bugged Pricing Column
    """

def main():
    listings=pd.read_csv('listingss.csv')
    cleaned_listings=cleaning_data(listings)
    
    price_by_neighbourhood(cleaned_listings)
    plot_avg_minimum_nights_by_neighbourhood(cleaned_listings)
    price_by_reviews_per_month_bar(cleaned_listings)
    price_by_reviews_per_month_scatter(cleaned_listings)
    price_by_reviews_scatter(cleaned_listings)
    price_by_reviews_bar(cleaned_listings)
    number_of_reviews_by_reviews_per_month_scatter(cleaned_listings)
    price_by_min_nights(cleaned_listings)
    availability_by_minimum_nights_scatter(cleaned_listings)
    price_by_availability_scatter(cleaned_listings)
    ppl_w_highest_avg_price(cleaned_listings)
    most_amount_of_listings_vs_highest_avg_price(cleaned_listings)


main()