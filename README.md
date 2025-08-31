# Airbnb London Market Analysis

## Project Overview

This project provides an exploratory data analysis of the Airbnb market in London, with a focus on identifying key pricing trends. The analysis investigates how factors such as location, room type, and reviews influence a listing's price. The goal is to visualize general trends rather than build a predictive model.

##  Methodology and Analysis

### Data Collection and Cleaning

Data for this analysis was sourced from a Kaggle dataset on London Airbnb open data. The initial dataset was relatively messy, with a significant number of empty rows and columns. The `price` column also contained several erroneous entries, including a single-room listing priced at £20,000.

A custom cleaning function was implemented to address these issues. The function first drops all empty columns and then removes any remaining rows with null entries. This process resulted in a removal of approximately 16% of the data, but tens of thousands of entries remained, which was more than sufficient for the analysis.

###  Tools and Technologies

This analysis was conducted using the following Python libraries:

  * Pandas for data manipulation and cleaning.
  * Matplotlib for data visualization.

###  Exploratory Data Analysis (EDA)

The EDA process began with using `pandas.info()` to understand the column names and data types, and `pandas.describe()` to identify potential outliers that needed to be cleaned. I then proceeded with the core analysis, building bar charts and scatter plots to explore potential relationships within the data.

##  Results and Visualizations

### Price by Neighbourhood

![Price By NeighbourHood graph](images/Average%20Price%20By%20Neighbourhood.png)

Unsurprisingly, the analysis found that the three most expensive boroughs in London are the City of London, Westminster, and Kensington and Chelsea. These centrally located, wealthy areas have significantly higher average prices than all other boroughs. The price drop-off is quite sharp after these top three, with prices decreasing relatively linearly in other areas.

\<br\>

### Average Minimum Nights by Neighbourhood
![Average Minimum Nights by Neighbourhood graph](images/Average%20Minimum%20NIghts%20By%20Neighbourhood.png)
The analysis showed that average minimum nights are generally consistent across most boroughs. While a few exceptions exist, particularly in the City of London—which could be due to its high concentration of business travelers—there is no strong relationship between a neighbourhood's price and its average minimum nights.

\<br\>

### Price and Reviews per month
![Price and Reviews graph](images/Revies%20Per%20Month%20Relation%20To%20Price.png)
The relationship between a listing's price and its number of reviews is not very clear, but some trends were observed:

  * **Higher prices** tend to be associated with fewer reviews, which makes sense as new or more exclusive listings might not have accumulated many reviews yet.
  * A much clearer relationship is the inverse: a large number of reviews typically correlates with a lower price, likely reflecting high-volume, budget-friendly listings.

\<br\>

### Availability by Price
![Availability by Price graph](images/Availability%20by%20Price.png)
The analysis showed that "cheap places" have high availability throughout the year, but finding more expensive places is significantly more difficult, suggesting they may have lower overall availability.

\<br\>

### Reviews and Price by Room Type
![Reviews and Price by Room Type Graph](images/Number%20of%20Reviews%20Relation%20To%20Price.png)
The analysis on room type revealed that hotels are the most expensive, followed by private rooms and finally shared rooms, which are the cheapest.

\<br\>

### Number of Reviews vs. Reviews Per Month
![Number of Reviews vs. Reviews Per Month Graph](images/Number%20Of%20Reviews%20Relation%20to%20Reviews%20Per%20Month.png)
A slight positive correlation was found between the total number of reviews and reviews per month, but the relationship is not significant (correlation coefficient of 0.45). This lack of a strong relationship is likely due to the fact that some listings have been active for a very long time, giving them a high total review count but a low monthly rate.

##  Conclusions and Future Improvements

### Key Takeaways

The primary conclusion of this analysis is that three boroughs in London have significantly higher Airbnb prices. Additionally, a trend was observed where listings with fewer reviews can command a higher price, and hotels are consistently the most expensive room type.

### Future Enhancements

  * **More Rigorous Cleaning:** Implement a more robust data cleaning pipeline to handle outliers and missing data with greater precision.
  * **Annotate Key Statistics:** Add annotations to visualizations to highlight key statistics and insights directly on the graphs.
  * **Greater Variety of Charts:** Use a wider variety of charts, such as box plots, to better visualize the distribution of prices and other variables.
  * **Start with the README:** Focus on building a clear and comprehensive `README` from the very beginning of the project to improve documentation and reproducibility.