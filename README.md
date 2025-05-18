# Application de Paie pour Fonctionnaires Congolais

Cette application permet à l'État congolais de gérer et distribuer des bulletins de paie électroniques à ses fonctionnaires.

## Structure du projet

```
paie-fonctionnaire/
├── backend/         # Backend Django REST API
│   ├── manage.py
│   ├── paie/        # Paramètres du projet Django
│   └── paie_app/    # App principale : modèles, vues, API
├── mobile/          # (À venir) Application Flutter
├── .github/         # (À venir) Actions GitHub pour build et CI/CD
└── README.md
```

## Fonctionnalités

- Création et gestion des fonctionnaires
- Enregistrement des bulletins de paie mensuels
- API REST pour intégration avec l'app mobile
- Génération de fichiers PDF de bulletins (à venir)
- Notifications email ou SMS (à venir)

## Technologies utilisées

- Backend : Python, Django, Django REST Framework
- Base de données : SQLite (dev), PostgreSQL (prod)
- API : RESTful avec JSON
- Mobile : Flutter (à venir)
- CI/CD : GitHub Actions (à venir)

## Installation (Backend)

1. Cloner le dépôt :
```bash
git clone https://github.com/votre-utilisateur/paie-fonctionnaire.git
cd paie-fonctionnaire/backend
```

2. Créer un environnement virtuel et installer les dépendances :
```bash
python -m venv env
source env/bin/activate  # ou env\Scripts\activate sur Windows
pip install django djangorestframework
```

3. Lancer le serveur :
```bash
python manage.py migrate
python manage.py runserver
```

## Auteurs

- Développé par [python], Assistant expert Python & Flutter