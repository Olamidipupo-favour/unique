from math import floor
import inito
def getSearchResult():
    return [i.val() for i in db.child(child).get().each()]
def mwatch(d:str,d1:str,d2:str):
    d=d.strip()
    word_count=0
    for i in d.split():
        if(str(i.lower()) in str(d1.lower()) == True or str(d1.lower()).find(str(i.lower())) != -1 or str(d2.lower()).find(str(i.lower)) !=-1):
            word_count+=1
    if(word_count>0 and word_count > floor(len(d.split())/2)):
        return True
def tfidf(d):
    #g=d
    #d=[i[2] for i in g]
    #t={}
    #for i in g:
       #print(i)
       #k=d.count(i[2])
       #t.update({i[2]:k})
    #j=t.keys()
    #y=t.values()  
    #t=dict(zip(j,sorted(list(y))))
    #print(str(t))
    return d
    #will return a tfidf later in future.
def perfect_result(search):
    if(not search or search==None):
        return []
    else:
        res=[]
        #get results.
        for i in getSearchResult():
            if(mwatch(search,i[0],i[1])):
                res.append(i)
        return tfidf(res)
from flask import Flask, request,redirect, url_for, abort, render_template
app=Flask(__name__)
@app.route("/")
def rindex():
    return redirect(url_for("index"))
@app.route("/index",methods=['GET','POST'])
def index():
    if(request.method=="POST"):
        return render_template('index.html',res=perfect_result(request.form.get('q',None)),q=request.form.get('q',None))
    else:
        return render_template('index.html')
@app.errorhandler(404)
def err_404(e):
   return redirect(url_for("index"))
if __name__=='__main__':
    app.run("0.0.0.0")


