from flask import Flask, render_template, request, redirect, url_for
import geoip2.database
import json

service = Flask(__name__)

userinfo = open("./DATA/info.json","r",encoding="utf-8")
user_data = json.load(userinfo)

user_name = user_data["name"]
email = user_data["email"]
github_url = user_data["github-url"]

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
            
            dply_lang=user_data["projects"]["dply"]["lang"], 
            dply_info=user_data["projects"]["dply"]["info_text"], 
            dply_github=user_data["projects"]["dply"]["github"],

            frontera_lang=user_data["projects"]["frontera"]["lang"], 
            frontera_info=user_data["projects"]["frontera"]["info_text"], 
            frontera_github=user_data["projects"]["frontera"]["github"],

            yuna_lang=user_data["projects"]["yuna"]["lang"], 
            yuna_info=user_data["projects"]["yuna"]["info_text"], 
            yuna_github=user_data["projects"]["yuna"]["github"],

            hana_lang=user_data["projects"]["hana"]["lang"],
            hana_info=user_data["projects"]["hana"]["info_text"],
            hana_github=user_data["projects"]["hana"]["github"],

            mina_lang=user_data["projects"]["mina"]["lang"],
            mina_info=user_data["projects"]["mina"]["info_text"],
            mina_github=user_data["projects"]["mina"]["github"],

            team_list=user_data["Career"]["team"],
        )
    else:
        return "Incorrect connection method"

if __name__ == "__main__":
    service.run(host="0.0.0.0", port="1234", debug=True)
