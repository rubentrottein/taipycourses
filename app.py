import os, sys
from taipy.gui import Gui, Markdown, notify

# Données du professeur
professor = {
    "name": "Jean Dupont",
    "bio": "Professeur de piano et guitare avec plus de 10 ans d'expérience. Spécialisé en classique et jazz pour débutants et intermédiaires.",
    "contact": {
        "email": "jean.dupont@example.com",
        "phone": "+33 6 12 34 56 78"
    }
}

# Variables globales
current_page = "home"  # Par défaut, on commence sur la page d'accueil
name = ""
email = ""
message = ""

# Fonction d'envoi de message
def send_message(state):
    notify(state, "success", f"Merci {state.name}, votre message a été envoyé !")
    state.name, state.email, state.message = "", "", ""

# Header unique
header = """
<header class="bg-dark text-white py-3">
  <div class="container text-center">
    <h1>Jean Dupont - Professeur de Musique</h1>
    <nav class="nav">
      <a href="/home" class="nav-link mx-2">Accueil</a>
      <a href="/contact" class="nav-link mx-2">Contact</a>
    </nav>
  </div>
</header>
"""

# Contenu de la page d'accueil
home_content = """
<div class="container mt-4">
  <div class="row">
    <div class="col-md-6 text-center">
      <h2 class="text-light mb-4">Bienvenue</h2>
      <p class="lead text-light">Cours personnalisés de piano et guitare pour tous niveaux.</p>
      <img src="JavaScript-logo.png" class="img-fluid rounded mt-4" />
    </div>
  </div>
</div>
"""

# Contenu de la page de contact
contact_content = """
<div class="container mt-4">
  <div class="row justify-content-center">
    <div class="col-md-6">
      <h2 class="text-light mb-4">Contact</h2>
      <div class="card bg-dark text-light">
        <div class="card-body">
          <p><strong>Email:</strong> {email}</p>
          <p><strong>Téléphone:</strong> {phone}</p>
          <hr class="bg-light" />
          <div class="mb-3">
            <input type="text" class="form-control bg-dark text-light" placeholder="Votre nom" bind="{{name}}" />
          </div>
          <div class="mb-3">
            <input type="email" class="form-control bg-dark text-light" placeholder="Votre email" bind="{{email}}" />
          </div>
          <div class="mb-3">
            <textarea class="form-control bg-dark text-light" rows="5" placeholder="Votre message" bind="{{message}}"></textarea>
          </div>
          <button class="btn btn-primary w-100" on:click="send_message">Envoyer</button>
        </div>
      </div>
    </div>
  </div>
</div>
""".format(email=professor['contact']['email'], phone=professor['contact']['phone'])

# Page principale
main_md = Markdown(f"""

{header}

{home_content}
""")
# Page de contact
contact_md = Markdown(f"""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" />
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>


{header}          

{contact_content}

""")

# Configuration des routes
pages = {
    "home": main_md,
    "contact": contact_md
}

#Export du site statique pour le déploiement
def export_static_site():
    # Crée un dossier pour le site statique
    os.makedirs("static_site", exist_ok=True)

    # Exporte chaque page en HTML
    gui = Gui(pages=pages)
    for page_name, page_content in pages.items():
        html_content = gui.render(page_content)
        with open(f"static_site/{page_name}.html", "w", encoding="utf-8") as f:
            f.write(html_content)

if __name__ == "__main__":
    # exportation de la version statique
    if "--export" in sys.argv:
        export_static_site()
    else:
      # Exécution de l'application avec rechargement automatique
      Gui(pages=pages).run(use_reloader=True)