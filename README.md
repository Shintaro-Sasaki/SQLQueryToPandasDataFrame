# SQLQueryToPandasDataFrame

Just a little Python function to execute multi statement SQL server sql query and get array of Pandas DataFrame back based on result sets that are coming back from the query.

Not performance tested - This is for small data (like less than 100K records, as to Big Data) and not intended to be used to replace ETL

Need Pandas and win32com.client (as you can see in the code)
