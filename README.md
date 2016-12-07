# SQLQueryToPandasDataFrame
Just a little Python function to execute multi-statement SQL server sql query and get array of Pandas DataFrame back based on result sets that are coming back from the query.  What I mean by multi-statement is that on the SQL side you might want to create some temp table, or branch out etc.

Things to note:

- Each statement in the query must end with a ';' (semicolon) - That is how this function determines end of each statement in the query without doing Syntax Analysis on the query.  ADODO.Connection.execute() does not seem to support multi statement execution probably because it's OLEDB.  So the function calls one execute() per statement.

- Not performance tested - This is for small data (like less than 100K records, as to Big Data) and not intended to be used to replace ETL

- This is for Windows machine - You will need OLEDB SQL server driver available (which comes with newer Windows 7+)

- Need Pandas and win32com.client (as you can see in the code)
