import pymysql
import _mssql

def test():
    # with pymysql.connect("192.168.0.2", "sa", "Welcome1!", "YunGongChang_184") as pyconn:
    #     cursor = pyconn.cursor();
    #     cursor.execute("""
    #     If OBJECT_ID('', 'U') IS NULL
    #     begin
    #         CREATE TABLE  (
                
    #         )
    #     end    

    #     """);

    with _mssql.connect(server="192.168.0.2", user="sa", password="Welcome1!", database="YunGongChang_Saas") as _conn:
        _conn.execute_query("select top 2 * from dbo.abpusers");
        for r in _conn:
            print "Id=%d, Name=%s" % (r['Id'], r['Name']);
# entry
test();
