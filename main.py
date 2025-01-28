from dotenv import load_dotenv
from flask import Flask, request,render_template
from genresponse import AnalyseAndGenerateResponse

load_dotenv() 

app=Flask(__name__)


@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="GET":
        return render_template("index.html")
    else:
        body=request.get_json(force=True)
        sql_query=body["sql_query"]
        ob1=AnalyseAndGenerateResponse()
        return {"message":ob1.genResponse(sql_query=sql_query)}

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)