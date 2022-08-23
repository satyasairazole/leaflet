from flask import Flask, request,render_template,redirect,url_for
from flask_cors import CORS
from datetime import datetime
app = Flask(__name__,instance_relative_config=True)
app.config['SECRET_KEY'] = "\xea;\xb3\x97lqeWP\xca\x17;\x1cM\r\x80\xab\x17\xd9\xbe\\\xafC\xcb"
cors = CORS(app, resourses={"/*": {"orgins": "/*"}})


@app.route('/')
@app.route('/home')
def home():
    #return "hello world";
    return render_template('upload_article_page.html');

@app.route('/addMainCat',methods=["POST"])
def addMainCat():
    v = request.form.get('main_category')
    
    if v != None:
        print(v)
        return redirect(url_for('home'))
        #return {'status': 'success','message':'main category added'}
    else:
        return redirect(url_for('home'))
       # return {"status": "fail", "message": "main category not added"}


@app.route('/addSubCat',methods=["POST"])
def addSubCat():
    m = request.form.get('main_category')
    s = request.form.get('sub_category')
    if m != None and s != None:
        print(m)
        print(s)
        #return {'status': 'success','message':'main category added'}
        return redirect(url_for('home'))

    else:
        return redirect(url_for('home'))
        #return {"status": "fail", "message": "main category not added"}

@app.route("/uploadArticle",methods=["POST"])
def upload_article():
    title = request.form.get("title")
    pub_date = request.form.get("pubDate")
    content = request.form.get("content")
    #display_position = request.form.get("display_position")
    category =  request.form.get("category")
    author = request.form.get("author")
    author = request.form.get("tags")
    imageUrl = request.form.get('image_url')
    postUrl = request.form.get("post_url")
    # image_link = ""
    # print(post_tag,category)
    dt_obj = datetime.datetime.strptime(pub_date,
                           '%Y-%m-%dT%H:%M:%S%f')
    millisec = dt_obj.timestamp() * 1000

    data = {"title":title,"pubDate":millisec,"content":content,"display_position":display_position,"category":category,"author":author,'image_link': imageUrl,"post_link":postUrl}
    print(data)
    return {'status':'success','message':'article uploaded'}


@app.route("/uploadObiterDicta",methods=["POST"])
def upload_obiter_dicta():
    caption = request.form.get("caption")
    pub_date = request.form.get("pubDate")
    dt_obj = datetime.datetime.strptime(pub_date,
                           '%Y-%m-%dT%H:%M:%S%f')
    image = request.form.get("imageUrl")

    data = {"imageLink":image,"caption":caption, "pubDate": dt_obj}
    print(data)
    return {"status": "success",'message': 'obiter dicta uploaded'}


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")