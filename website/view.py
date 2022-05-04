from flask import Flask, Blueprint,render_template

views = Blueprint('views',__name__)

headings = ("Product", "Sites", "Price tags")
data = (
        ("Nike Air Frost One", "Ebay", "$150"),
        ("Nike", "Amazon", "$100"),
        ("Swoosh", "Nike.com", "$90"),
        ("alphalxlz","footlocker.com","$140")

)



   
@views.route("/")
def table():
    return render_template("table.html",headings=headings,data=data)
