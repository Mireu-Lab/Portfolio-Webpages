from flask import Flask, render_template, request, redirect, url_for
import geoip2.database
import json

service = Flask(__name__)

userinfo = open("./DATA/info.json","r",encoding="utf-8")
user_data = json.load(userinfo)

user_name = user_data["name"]
email = user_data["email"]
github_url = user_data["github-url"]
projects = user_data['projects']
langs = user_data['langs']
career = user_data['Career']

text = """
------------------------------\n
1. User Name : {}\n
2. GitHub URL : {}\n
------------------------------
""".format(user_data["name"], user_data["github-url"])

print(text)
    
@service.route("/")
def main_pages():
    if request.method == "GET":
        return render_template("index.html", 
            email=email,
             
            github_url=github_url, 

            langs = langs,
            projects = projects,

            career=career
        )
    else:
        return "Incorrect connection method"

if __name__ == "__main__":
    service.run(host="0.0.0.0", port="12347", debug=True)
