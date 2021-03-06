# SQLQueryToPandasDataFrame
Just a little Python function to execute multi-statement SQL server query and get list of Pandas DataFrame that contain all resultsets that are coming back from the query.

ADODO.Connection.execute() does not seem to support getting multiple result sets from multi statement execution probably because of OLEDB thingy (.execute() can run multiple statements but only the result set from the first statement seems to be coming back).  So the function calls one execute() per block of sql statement that are devided by ';'.  So... if you have dynamic sql with ';' in it, that will break the statement and blow this up for sure.
  
**Usage**:

- Just copy and paste the function to where you want to run.

**Example**:

```Python
query = """
CREATE TABLE #X (ID INT) ;
INSERT INTO #X SELECT TOP 10 MyTableAId FROM dbo.MyTableA ;
INSERT INTO #X SELECT TOP 10 MyTableBId FROM dbo.MyTableB ORDER BY MyTableBId DESC ;
SELECT * FROM #X ; -- First Resultset and will be saved into list_of_DataFrames[0] as DataFrame
SELECT * FROM #X X JOIN dbo.MyTableAId A ON X.ID = A.MyTableAId ; -- Second Resultset and will be saved into list_of_DataFrames[1] as DataFrame
"""

list_of_DataFrames = QueryToDataFrameList('MyDBServer', 'MyDBName', query)
```

**Notes**:

- **Each statement in the query must end with a ';' (semicolon)** - That is how this function determines end of each statement in the query without doing Syntax Analysis on the query.



- **Need Pandas and win32com.client** (as you can see in the code)

- **This is for Windows machine** - You will need OLEDB SQL server driver available (which comes with newer Windows 7+)

- **Not performance tested** - This is for small data (like less than 100K records, as to Big Data) and not intended to be used to replace ETL

**TODO**

- Assign corret Pandas DataFrame dtype based on OLEDB column data type

- Figure out the reason for mysterious Python crash
