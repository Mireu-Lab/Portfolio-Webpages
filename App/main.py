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

def lang_chack(ip):
    country_reader = geoip2.database.Reader("./DATA/GeoLite2-Country.mmdb")
    country_response = country_reader.country(ip)
    print(country_response.country.iso_code)
    return str(country_response.country.iso_code)
    
@service.route("/")
def main_pages():
    if request.method == "GET":
        try:
            iso_code_data = lang_chack(request.remote_addr)
            if iso_code_data == "KR":  
                return redirect("/ko")
            elif iso_code_data == "US":
                return redirect("/en")
            elif iso_code_data == "jp":
                return redirect("/jp")
            else:
                return redirect("/en")
        except geoip2.errors.AddressNotFoundError:
            return redirect("/en")
    else:
        return "Incorrect connection method"

@service.route("/ko")
def main_pages_ko():
    if request.method == "GET":
        return render_template("index.html", 
            lang="KR",
            email=email,
             
            github_url=github_url, 
            twitter_url=twitter_url,
            discord_url=discord_url,
            
            title_text=user_data["title_text"]["ko"],
            see_more_text=user_data["see_more_text"]["ko"],

            about_text_1=user_data["about_info_text"]["ko"]["1"],
            about_text_2=user_data["about_info_text"]["ko"]["2"],
            about_text_3=user_data["about_info_text"]["ko"]["3"],

            dply_lang=user_data["projects"]["dply"]["lang"], 
            dply_info=user_data["projects"]["dply"]["info_text"]["ko"], 
            dply_url=user_data["projects"]["dply"]["url"],
            
            frontera_lang=user_data["projects"]["frontera"]["lang"], 
            frontera_info=user_data["projects"]["frontera"]["info_text"]["ko"], 
            frontera_url=user_data["projects"]["frontera"]["url"],

            yuna_lang=user_data["projects"]["yuna"]["lang"], 
            yuna_info=user_data["projects"]["yuna"]["info_text"]["ko"], 
            yuna_url=user_data["projects"]["yuna"]["url"],

            team_list=user_data["Career"]["team"]['ko'],
            certificate_list=user_data["Career"]["certificate"]['ko'],
            contest_list=user_data["Career"]["contest"]['ko'],
            thesis_list=user_data["Career"]["thesis"]['ko'],
        )
    else:
        return "Incorrect connection method"

@service.route("/en")
def main_pages_en():
    if request.method == "GET":
        return render_template("index.html", 
            lang="US",
            email=email,
             
            github_url=github_url, 
            twitter_url=twitter_url,
            discord_url=discord_url,
                               
            title_text=user_data["title_text"]["en"],
            see_more_text=user_data["see_more_text"]["en"],
            
            about_text_1=user_data["about_info_text"]["en"]["1"],
            about_text_2=user_data["about_info_text"]["en"]["2"],
            about_text_3=user_data["about_info_text"]["en"]["3"],

            dply_lang=user_data["projects"]["dply"]["lang"], 
            dply_info=user_data["projects"]["dply"]["info_text"]["en"], 
            dply_url=user_data["projects"]["dply"]["url"],

            frontera_lang=user_data["projects"]["frontera"]["lang"], 
            frontera_info=user_data["projects"]["frontera"]["info_text"]["en"], 
            frontera_url=user_data["projects"]["frontera"]["url"],

            yuna_lang=user_data["projects"]["yuna"]["lang"], 
            yuna_info=user_data["projects"]["yuna"]["info_text"]["en"], 
            yuna_url=user_data["projects"]["yuna"]["url"],

            team_list=user_data["Career"]["team"]['en'],
            certificate_list=user_data["Career"]["certificate"]['en'],
            contest_list=user_data["Career"]["contest"]['en'],
            thesis_list=user_data["Career"]["thesis"]['en'],
        )
    else:
        return "Incorrect connection method"

@service.route("/jp")
def main_pages_jp():
    if request.method == "GET":
        return render_template("index.html", 
            lang="JP",
            email=email,
             
            github_url=github_url, 
            twitter_url=twitter_url,
            discord_url=discord_url,
                               
            title_text=user_data["title_text"]["jp"],
            see_more_text=user_data["see_more_text"]["jp"],

            about_text_1=user_data["about_info_text"]["jp"]["1"],
            about_text_2=user_data["about_info_text"]["jp"]["2"],
            about_text_3=user_data["about_info_text"]["jp"]["3"],

            dply_lang=user_data["projects"]["dply"]["lang"], 
            dply_info=user_data["projects"]["dply"]["info_text"]["jp"], 
            dply_url=user_data["projects"]["dply"]["url"],
            
            frontera_lang=user_data["projects"]["frontera"]["lang"], 
            frontera_info=user_data["projects"]["frontera"]["info_text"]["jp"], 
            frontera_url=user_data["projects"]["frontera"]["url"],

            yuna_lang=user_data["projects"]["yuna"]["lang"], 
            yuna_info=user_data["projects"]["yuna"]["info_text"]["jp"], 
            yuna_url=user_data["projects"]["yuna"]["url"],

            team_list=user_data["Career"]["team"]['jp'],
            certificate_list=user_data["Career"]["certificate"]['jp'],
            contest_list=user_data["Career"]["contest"]['jp'],
            thesis_list=user_data["Career"]["thesis"]['jp'],
        )
    else:
        return "Incorrect connection method"

if __name__ == "__main__":
    service.run(host="0.0.0.0", port="1234", debug=True)
