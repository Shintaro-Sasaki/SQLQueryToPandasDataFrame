import pandas as pd
import win32com.client as w32c
def QueryToDataFrameList(server, database, query):
    dataframe_list = []
    conn = w32c.Dispatch(r'ADODB.Connection')
    conn.Open("Provider=SQLOLEDB; Integrated Security=SSPI; Data Source={}; Initial Catalog={};".format(server, database))
    for statement in list(q.strip() + ' ;\n' for q in query.split(';') if len(q.strip()) > 0):
        print(statement)
        recordset = conn.execute(statement)
        columns = list({
            'Name':obj.Name,
            #"Type":obj.Type #https://msdn.microsoft.com/en-us/library/ms711251%28v=vs.85%29.aspx?f=255&MSPPError=-2147217396 #TODO: Assign Correct Type to Series
        } for obj in recordset.Fields)
        if len(columns) > 0:
            rows = recordset.GetRows();
            col_index = 0
            df = pd.DataFrame()
            for series in rows:
                df[columns[col_index]['Name']] = pd.Series(data=series)
                col_index += 1
            dataframe_list += [df]
    conn.Close()
    return dataframe_list