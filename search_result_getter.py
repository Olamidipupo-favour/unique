def getSearchResult(t:str):
    import sqlalchemy as s
    en="mysql://dipo:dipo@localhost/dipo"
    engine=s.create_engine(en)
    metadata=s.MetaData()
    essential_info=s.Table(
    "webpage_info",
    metadata,
    s.Column("name",s.String),
    s.Column("desc",s.String(10)),
    s.Column("link",s.String)
)
    metadata.create_all(engine)
    with engine.connect() as conn:
        result=conn.execute(s.select(essential_info.c.name).where(essential_info.c.name==t))
        conn.commit()
    return result
def perfect_result(search='none'):
    if(search=='none'):
        return none
    else:
        return getSearchResult(search)
from flask import Flask, request,redirect, url_for, abort, render_template
app=Flask(__name__)
@app.route("/")
def rindex():
    return redirect(url_for("index"))
@app.route("/index",methods=['GET','POST'])
def index():
    if(request.method=="POST"):
        print("**************************************************************************************************************************************")
        return render_template('index.html',search_res=perfect_result(request.form.get('search',['NO RESULTS WERE FOUND'])))
    else:
        print("zoom")
        return render_template('index.html',search_res=[])
app.run(debug=True)
import sqlalchemy as s
en="mysql://dipo:dipo@localhost/dipo"
engine=s.create_engine(en,echo=True)
metadata=s.MetaData()
essential_info=s.Table(
"webpage_info",
metadata,
s.Column("name",s.String),
s.Column("desc",s.String(10)),
s.Column("link",s.String)
)
with engine.connect() as conn:
    result=conn.execute(s.select(essential_info.c))
    for i in result:
        print(i)


