from flask import Flask, Blueprint,render_template

views = Blueprint('views',__name__)

headings = ("Product", "Sites", "Price tags")
data = (
        ("Nike Air Frost One", "Ebay", "$150"),
        ("Nike", "Amazon", "$100"),
        ("Swoosh", "Nike.com", "$90"),

)


@views.route("/")

def home():
    return render_template("home.html")

   


@views.route("/table")
def table():
    return render_template("table.html",headings=headings,data=data)
