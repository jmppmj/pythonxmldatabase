from lib import *

sns.set(style="ticks", color_codes=True)
ntree = ET.parse('programmingbooks.xml')
root = ntree.getroot()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# STATISTICS/CHARTS ON DATABASE - PANDAS-MATPLOTLIB-SEABORN
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create new dataframe.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def valueofnode(node):
    return node.text if node is not None else None

def newDataFrame():
    cols = ['bookid', 'author', 'title', 'genre', 'price', 'publish_date', 'isbn10']
    xmldf = pd.DataFrame(columns=cols)

    for node in root:
        bookid = node.find('bookid')
        author = node.find('author')
        title = node.find('title')
        genre = node.find('genre')
        price = node.find('price')
        publish_date = node.find('publish_date')
        isbn10 = node.find('isbn10')

        xmldf = xmldf.append(pd.Series([valueofnode(bookid), valueofnode(author), valueofnode(title),
            valueofnode(genre), valueofnode(price), valueofnode(publish_date),
            valueofnode(isbn10)], index=cols), ignore_index=True)

    return xmldf

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Bar chart of genre frequency.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def genreBarChart():
    #bar chart
    df1 = newDataFrame()
    df1['genre'] = pd.Categorical(df1.genre)

    #uses the Seaborn Library, as well as MatPlotLib and Pandas
    sns.set(style='darkgrid')
    sns.countplot(data=df1,
                  x='genre',
                  order=df1.genre.value_counts().index,
                  palette="GnBu_d").set_title('Book Genre Frequency')
    plt.show(block=False)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Bar chart of publish year frequency.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def publishyearBarChart():
    #bar chart
    df1 = newDataFrame()
    df1['publish_date'] = pd.Categorical(df1.publish_date)

    #uses the Seaborn Library, as well as MatPlotLib and Pandas
    sns.set(style='darkgrid')
    sns.countplot(data=df1,
                  x='publish_date',
                  order=df1.publish_date.value_counts().index,
                  palette="BuGn_r").set_title('Publish Year Frequency')
    plt.show(block=False)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Comparison chart of publish year frequency by genre.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def publishdateScatter():
    #scatter plot
    df1 = newDataFrame()
    df1['publish_date'] = pd.to_numeric(df1.publish_date)
    df1['genre'] = pd.Categorical(df1.genre)

    #uses the Seaborn Library, as well as MatPlotLib and Pandas
    sns.set(style='darkgrid')
    sns.relplot(data=df1,
                x='publish_date',
                y='genre',
                sizes=(500, 500),
                alpha=.5,
                height=6,
                hue='genre',
                size='publish_date',
                legend=False)

    plt.title("Book Publish Years by Genre")
    plt.show(block=False)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Comparison chart of price/values by publish year
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def pricepublish():
    df1 = newDataFrame()
    df1['publish_date'] = pd.to_numeric(df1.publish_date)
    df1['price'] = pd.to_numeric(df1.price)

    #uses the Seaborn Library, as well as MatPlotLib and Pandas
    sns.set(style='darkgrid')
    sns.lineplot(x='price',
                 y='publish_date',
                 hue="publish_date",
                 data=df1,
                 marker="o",
                 legend=False)

    plt.title("Price/Values by Publish Year")
    plt.show(block=False)
