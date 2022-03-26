# -*- coding: utf-8 -*-
"""
@Description : 
@File        : flask_app.py
@Project     : SYProject
@Time        : 2022/3/10 下午5:04
@Author      : dj
@Software    : PyCharm
"""
import json

from flask import Flask,render_template, request
import pandas as pd
from base.db_conn import DataBaseConn
import os
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "html")#html是个文件夹
path = root+'/static'

app = Flask(__name__, static_url_path=path)


@app.route('/warehouse')
def find_warehosue_task():
    db = DataBaseConn()
    conn = db.conn
    sql = '''
     SELECT * FROM warehouse_task limit 100
    '''
    df = pd.read_sql(sql=sql, con=conn)
    pd.set_option('colheader_justify', 'center')  # FOR TABLE <th>
    s = df.style.set_properties(**{'text-align': 'left'})
    s.render()
    html_string = '''
    <html>
      <head><title>HTML Pandas Dataframe with CSS</title></head>
      <link rel="stylesheet" type="text/css" href="df_style.css"/>
      <body>
        {table}
      </body>
    </html>.
    '''
    # OUTPUT AN HTML FILE
    with open('myhtml.html', 'w') as f:
        f.write(html_string.format(table=df.to_html(classes='mystyle')))
    conn.close()
    return render_template('myhtml.html')


@app.route('/get/task', methods=['get','post'])
def get_warehosue_task():
    db = DataBaseConn()
    conn = db.conn
    if request.method == 'POST':
        org_id = request.json.get('org_id')
        status = request.json.get('status')
        scene = request.json.get('scene')
    else:
        org_id = request.args.get('org_id')
        status = request.args.get('status')
        scene = request.args.get('scene')
    sql = f'SELECT * FROM warehouse_task where org_id={org_id} and status={status} and scene ={scene}'
    df = pd.read_sql(sql=sql, con=conn)
    conn.close()
    return df.to_html()


if __name__ == '__main__':
    app.run()
