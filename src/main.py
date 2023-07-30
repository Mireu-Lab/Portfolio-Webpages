from flask import Flask, render_template, request, redirect, url_for
import json

service = Flask(__name__)

with open("./DATA/info.json","r",encoding="utf-8") as userinfo:
    user_data = json.load(userinfo)

user_info = user_data["user_info"]
projects = user_data['projects']
langs = user_data['langs']
career = user_data['Career']

text = f"""
------------------------------\n
1. User Name : {user_info["name"]} \n
------------------------------
"""

print(text)
    
@service.route("/")
def main_pages():
    if request.method == "GET":
        return render_template("index.html", 
            user_info = user_info,
            langs = langs,
            projects = projects,
            career=career
        )
    else:
        return "Incorrect connection method"

if __name__ == "__main__":
    service.run(host="0.0.0.0", port="80", debug=True)
