from flask import Flask, render_template, request, url_for
import os,sys,re, json
#from flask_cors import CORS
app = Flask(__name__,template_folder='.')
#cors = CORS(app, resources={r"/*": {"origins": "*"}})

# --------------------------------------------------------------------
@app.route("/")
@app.route("/pageA")
def pageA():
    return render_template('pageA.html') # rendre la page A.html

@app.route("/pageB",methods=['POST'])
def pageB():
  print(request.form)
  result = request.form
  # appliquer filtre sur result
  return render_template('pageB.html',result=result) # rendre la page B.html avec le result (qui contient le critère de client (request))


@app.route('/recherche/<critere>')
#@cross_origin()
def recherche_critere(critere):
   lignes = []
   liste = os.listdir("PAGES")
   for fichier in liste :
      fd = open("PAGES/"+fichier)
      for ligne in fd.readlines() :
        res1 = re.search("\[\[(.+?)\]\]", ligne)  # L'expression régulière est à trouver
        res2 = re.search(""+critere, ligne)         
        if res2 and res1 :
            lignes.append([fichier,ligne])  # Le nom de la page est envoyée avant la ligne dans une sous-liste
   return json.dumps(lignes)

if __name__ == '__main__':
   app.run(debug = True)


