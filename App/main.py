from flask import Flask, render_template, request, redirect, url_for
import geoip2.database
import json

service = Flask(__name__)

userinfo = open("./DATA/info.json","r",encoding="utf-8")
user_data = json.load(userinfo)

user_name = user_data["name"]
email = user_data["email"]
github_url = user_data["github-url"]
twitter_url=user_data["twitter_url"]
discord_url=user_data["discord_url"]

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
            lang="US",
            email=email,
             
            github_url=github_url, 
            twitter_url=twitter_url,
            discord_url=discord_url,
                               
            title_text=user_data["title_text"],
            see_more_text=user_data["see_more_text"],
            
            about_text_1=user_data["about_info_text"]["1"],
            about_text_2=user_data["about_info_text"]["2"],
            about_text_3=user_data["about_info_text"]["3"],

            dply_lang=user_data["projects"]["dply"]["lang"], 
            dply_info=user_data["projects"]["dply"]["info_text"], 

            frontera_lang=user_data["projects"]["frontera"]["lang"], 
            frontera_info=user_data["projects"]["frontera"]["info_text"], 
            
            yuna_lang=user_data["projects"]["yuna"]["lang"], 
            yuna_info=user_data["projects"]["yuna"]["info_text"], 

            team_list=user_data["Career"]["team"],
        )
    else:
        return "Incorrect connection method"

if __name__ == "__main__":
    service.run(host="0.0.0.0", port="1234", debug=True)
