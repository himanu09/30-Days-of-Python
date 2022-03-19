from flask import Flask, jsonify
app = Flask(__name__)
@app.route("/get/")
def getEmployeeList():
    from turtle import title
    import requests
    from bs4 import BeautifulSoup
    url="https://www.horoscope.com//us//index.aspx"
    r=requests.get(url)
    htmlcontent=r.content
    soup=BeautifulSoup(htmlcontent,"html.parser")
    title=soup.title
    print(title.text)
    aries=soup.find(id='src-hp-aries')
    for it in aries.stripped_strings:
        
        return jsonify(it)
    Gemini=soup.find(id='src-hp-gem')
    for item in Gemini.stripped_strings:
        return jsonify(item)

if __name__ == "__main__":
    app.run()

# var jsonObject = ;