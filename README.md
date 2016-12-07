# SQLQueryToPandasDataFrame
Just a little Python function to execute multi-statement SQL server query and get array of Pandas DataFrame back based on result sets that are coming back from the query.  What I mean by multi-statement is that on the SQL side you might want to create some temp table, or branch out etc.

Use:

- Just copy and paste the function to where you want to run.

Things to note:

- **Each statement in the query must end with a ';' (semicolon)** - That is how this function determines end of each statement in the query without doing Syntax Analysis on the query.

  ADODO.Connection.execute() does not seem to support getting multiple result sets from multi statement execution probably because of OLEDB thingy (.execute() can run multiple statements but only the result set from the first statement seems to be coming back).  So the function calls one execute() per block of sql statement that are devided by ';'.  So... if you have dynamic sql with ';' in it, that will break the statement and blow this up for sure.

- **Need Pandas and win32com.client** (as you can see in the code)

- **This is for Windows machine** - You will need OLEDB SQL server driver available (which comes with newer Windows 7+)

- **Not performance tested** - This is for small data (like less than 100K records, as to Big Data) and not intended to be used to replace ETL
