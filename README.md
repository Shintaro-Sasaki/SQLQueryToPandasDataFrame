# SQLQueryToPandasDataFrame

Just a little Python function to execute multi-statement SQL server sql query and get array of Pandas DataFrame back based on result sets that are coming back from the query.  What I mean by multi-statement is that on the SQL side you might want to create some temp table, or branch out etc.

The query MUST divide each statement with a ';' that is how this function determines different statement without doing Syntax Analysis of the query

Not performance tested - This is for small data (like less than 100K records, as to Big Data) and not intended to be used to replace ETL

Also this is specifically for Windows machine.  You will need OLEDB SQL server driver available (which comes with newer Windows 7+)

Need Pandas and win32com.client (as you can see in the code)
