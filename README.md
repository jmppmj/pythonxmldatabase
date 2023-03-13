<b>A Python & XML database application for a book collection.</b>

Focus was placed on exploring various methods of parsing, manipulating, and analyzing XML data.

***

<b>Project Overview:</b>
- An XML file serves as the main data storage, with several starting book entries.
- Using the C implementation of ElementTree in Python, xml.etree.cElementTree, CRUD functionality is added. CRUD is an acronym that stands for create, read, update, and delete and encompasses the four basic functions of persistent storage.
- A user can update a book entry, delete a book entry, see all book entries, search for a book entry, and create new book entries.
- XML data is then placed into a table using Pandas Dataframes (in-memory data storage). This allows for quick data analysis and generating statistical charts and graphs on the data with the very popular and heavily used Python libraries, NumPy and MatPlotLib. 
- Four chart functions are added (bar chart of genre frequency, bar chart of publish year frequency, comparison chart of publish year frequency by genre, and comparison chart of price/values by publish year). More automatically generated chart functions can easily be added.
- A GUI was added, for a more user-friendly experience.

Please view powerpoint (<b>Databases.pptx</b> file in this GitHub) for further details on the project.

***

<table style="width:100%">
  <tr>
    <th>Python (3.8.5) Libraries Used:</th>
    <td><a href="https://www.python.org/doc/" target="_blank">Python Docs</a></td>
  </tr>
  <tr>
    <td>Pandas 1.1.1</td>
    <td><a href="https://pandas.pydata.org/pandas-docs/stable/" target="_blank">Pandas Docs</a></td>
  </tr>
  <tr>
    <td>NumPy 1.19.1</td>
    <td><a href="https://numpy.org/doc/" target="_blank">NumPy Docs</a></td>
  </tr>
  <tr>
    <td>MatPlotLib 3.3.1</td>
    <td><a href="https://matplotlib.org/" target="_blank">MatPlotLib Docs</a></td>
  </tr>
  <tr>
    <td>Seaborn 0.10.1</td>
    <td><a href="https://seaborn.pydata.org/" target="_blank">Seaborn Docs</a></td>
  </tr>
  <tr>
    <td>PySimpleGUI 4.29.0</td>
    <td><a href="https://pysimplegui.readthedocs.io/en/latest/" target="_blank">PySimpleGUI Docs</a></td>
  </tr>
</table>

***

<i>Future Work: Improve GUI</i>
