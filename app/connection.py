from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy import text
import io


# The POST needs 4 parameters:
# inital date [str]
# end date [str]
# center_id [int]
# query numer [int]
def Connection(fini, ffin, cid, sql):
    try:
        conn = create_engine()
        file = io.open(f"sql\{sql}", 'r', encoding='utf8')
    except:
        pass

    try:
        conn = create_engine()
        file = io.open(f"sql/{sql}", 'r', encoding='utf8')

    except:
        pass

    sql = text(file.read())

    a = conn.execute(sql, InitialDate=fini, EndDate=ffin, CenterID=cid)
    a = a.fetchall()

    df = pd.DataFrame(a)
    js = df.to_json(orient='index', indent=4)

    return js