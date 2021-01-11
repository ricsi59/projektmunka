import os
import os.path

from flask import Flask, redirect, render_template, send_from_directory

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/megrendeles', methods=['GET'])
def home():
    lap = open(r"C:\Users\bszim\OneDrive\Asztali gép\Ricsi suli\Projekt\Projekt\site\template.html ",
               "r", encoding="utf-8")
    web = lap.read()
    # save_path = "C:Users:bszim:OneDrive:Asztali gép:Ricsi suli:Projekt:Projekt:template.html"

    if (web.find('<table>') == -1):
        savehtml(filename="site/template.html")
    return redirect("/template.html", code=302)


@app.route('/<path:filename>')
def send_file(filename):
    return send_from_directory('site', filename)


app.run()


def savehtml(filename="defaulthtml"):
    htmldata = data2list(data)

    htmldata = htmldata.replace("<table>", f"{web}\n<table>""\n")

    with open("template.html", "w", encoding="utf-8") as filehtml:

        filehtml.write(htmldata)

        # filehtml.close()


def data2list(data):
    d = data.splitlines()[0:-1]
    d = [x.strip().split(";") for x in d]
    for row in d:
        for e in row:
            e_index = row.index(e)
            cell = "<td>" + e.strip() + "</td>"
            if e_index == 0:
                d[d.index(row)][row.index(e)] = "<tr>""\n" + cell
            elif e_index == len(row) - 1:
                d[d.index(row)][row.index(e)] = cell + "\n""</tr>""\n"
            else:
                d[d.index(row)][e_index] = cell
    d = [i for sublist in d for i in sublist]

    return "<table>" + "\n""".join(d) + "\n""</table>""\n""</body>""\n""</html>"


file = open(r"C:\Users\bszim\OneDrive\Asztali gép\Ricsi suli\Projekt\Projekt\rendeles.csv",
            "r", encoding="utf-8")
data = file.read()
lap = open(r"C:\Users\bszim\OneDrive\Asztali gép\Ricsi suli\Projekt\Projekt\site\template.html ",
           "r", encoding="utf-8")
web = lap.read()