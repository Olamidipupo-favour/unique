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
        result=conn.execute(s.select(essential_info))
        conn.commit()
    return [i for i result]
def match(d:str,d1:str):
    word_count=0
    for i in d:
        if(i.lower() in d1.lower() or d1.find(i.lower())):
            word_count+=1
    if(word_count>0 and word_count > floor(len(search)/2)):
        return True
def tfidf(d):
    return d
    #will return a tfidf later in future.
def perfect_result(search='none'):
    if(search=='none'):
        return []
    else:
        res=[]
        #get results.
        r=getSearchResult(search)
        for i in getSearchResult(search):
            if(match(search,i[0])):
                res.append(i)
        return tfidf(res)
from flask import Flask, request,redirect, url_for, abort, render_template
app=Flask(__name__)
@app.route("/<d:path>")
def error(d):
    abort(404)
@app.route("/")
def rindex():
    return redirect(url_for("index"))
@app.route("/index",methods=['GET','POST'])
def index():
    if(request.method=="POST"):
        return render_template('index.html',res=perfect_result(request.form.get('search',['NO RESULTS WERE FOUND'])),q=request.form.get('search',None))
    else:
        return render_template('index.html',res=[])
@app.errorhandler(404)
def err_404(e):
   return render_template('err404.html'),  404
app.run(debug=True)


