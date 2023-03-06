from page import pages
import json

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


print(pages.save(
    pages.description(
        user_info["page_description"], 
        user_info["page_author"]
    ), 
    pages.titlediv(
        user_info["signature_color"], 
        user_info["name"], 
        user_info["email"], 
        user_info["URL"]
    ), 
    pages.introduction(
        user_info["about"]
    ), 
    pages.firstsection(
        langs
    ), 
    pages.secondsection(
        projects,
        user_info["URL"]["GitHub"], 
    ), 
    pages.introduction_two(
        career
    ), 
    pages.getstarted(
        user_info["email"], 
        user_info["URL"]["GitHub"],
        user_info["URL"]
    )
))