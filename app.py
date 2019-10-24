from flask import Flask
from flask import request,render_template
import wikipedia

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if(request.method=='GET'):
        return render_template("form.html")  # return Form Page Template
    else:
       query=request.form.get('querystring')
       try:
           summary = wikipedia.summary(query)
       except wikipedia.exceptions.DisambiguationError as e:
             return render_template("result.html",message=e.options)
       except wikipedia.exceptions.PageError as p:
           return render_template("result.html",message="The page you requested was not found") 
       else:
            return render_template("result.html",message=summary)   # return final page template



if __name__ == '__main__':
   app.run()