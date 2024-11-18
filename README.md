# Projet Intégré : Etat du trafic rennais en fonction de la météo

## Technologies Utilisées

### Langage

![Python](https://img.shields.io/badge/Python-3.10.12-blue?logo=python&logoColor=white)

### Frameworks et Outils de Développement

![Docker](https://img.shields.io/badge/Docker-20.10.7-blue?logo=docker&logoColor=white)

### Cloud & Bases de Données

![Elasticsearch](https://img.shields.io/badge/Elasticsearch-8.15.0-blue?logo=elasticsearch&logoColor=white)
![Kibana](https://img.shields.io/badge/Kibana-8.15.0-orange?logo=kibana&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-5.0-green?logo=mongodb&logoColor=white)

### Bibliothèques de Données & Machine Learning

![Pandas](https://img.shields.io/badge/Pandas-1.5.2-brightgreen?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.21.0-blue?logo=numpy&logoColor=white)

### Outils de Visualisation

![Kibana](https://img.shields.io/badge/Kibana-8.15.0-orange?logo=kibana&logoColor=white)

### Conteneurisation et Déploiement

![Docker](https://img.shields.io/badge/Docker-20.10.7-blue?logo=docker&logoColor=white)

### Outils de Débogage et de Terminal

![IPython](https://img.shields.io/badge/IPython-8.0.0-blue?logo=ipython&logoColor=white)

---
Ces outils ont été utilisés pour le développement du projet sur l'état du trafic rennais, visant à ingérer, transformer, et analyser les données du trafic en temps réel pour obtenir des informations sur les habitudes des usagers et repérer les heures d'affluence ainsi qu'analyser pour savoir si le trafic est influencé par la météo ou non. Le traitement des données en temps réel est facilité par Airflow, ensuite nos données ont été intégrés dans un DataLake sous MongoDB.

## Objectif du Projet
Ce projet vise à analyser l’impact des conditions météorologiques et des niveaux de pollution sur le trafic routier afin de proposer des solutions pour améliorer la gestion de la mobilité, réduire les congestions et limiter les risques d’accidents. Ce projet nous amène donc à nous demander : 
En quoi les conditions météorologiques et les niveaux de pollution influencent-ils le trafic routier ?


## 🎭 Mes cibles

Mes cibles principales incluent :

- **Réseau de route rennais** qui souhaitent surveiller le trafic sur leurs route et repérer si il y a des jours où des routes sont plus empruntés que d'autres.

- **Métropole rennaise** qui souhaitent suivre si les routes sont plus ou moins empruntés certains jours ou non.

- **Analystes de Données et Chercheurs** qui souhaitent étudier les tendances de fréquentations des clients en fonction de circonstances extérieurs (exemple : météo et pollution de l'air)


## Architecture du Projet 

```
.
├── data
│   └── ??
├── data-ingestion-kedro ??
│   ├── conf
│   ├── data
│   ├── notebooks
│   ├── pyproject.toml
│   ├── README.md
│   ├── requirements.txt
│   ├── session_store.db
│   ├── src
│   └── tests
├── Airflow
│   ├── docker-compose.yml
│   ├── requirements.txt+
│   ├── dags
│       ├── dag.py
│   ├── script
│       ├── entrypoint.sh
├── data_collection
│   ├── getAPI.py
├── docs ??
│   └── ...
├── ELK
│   ├── docker-compose.yml
│   └── import_to_elasticsearch.py
├── ENV
│   ├── bin
│   ├── etc
│   ├── include
│   ├── lib
│   ├── lib64 -> lib
│   ├── Scripts
│       ├── creation_csv.py
│   ├── pyvenv.cfg
│   └── share
## Finir en fonction de ce qu'on rajoute
├── image-1.png
├── image-2.png
├── image-3.png
├── image-4.png
├── image.png
├── kafka
├── kedro-airflow
│   ├── dags
│   ├── docker-compose.yml
│   ├── requirements.txt
│   └── script
├── notebook
│   └── EDA.ipynb
├── README.md
├── script
│   ├── getApi_Alim.py
│   └── preprocessing.py
├── sentiment_analysis_kafka
│   ├── docker-compose.yml
│   ├── requirements.txt
│   └── sentiment_analysis.py
└── spark
    ├── kafka_to_spark.py
    └── script
```


![alt text](image.png)

### Workflow et Schéma d'Architecture

1. **Ingestion des Données de l'Etat du trafic rennais** :
   - Extraction des données sur l'Etat du trafic Rennais en temps réel via l'API "Etat du trafic en temps réel" disponible sur le site data rennes métropole puis envoi des données dans Mongo DB.

2. **Ingestion des données Météo** :
   - Extraction des données météo via l'API disponible sur Open Weather Data puis envoi des données dans Mongo DB.

3. **Ingestion des données de la pollution de l'air** :
   - Extraction des données de la pollution de l'air via l'API disponible sur Open Weather Data puis envoi des données dans Mongo DB.

4. **Traitement des Données** :
   - **Transformation des Données** : Dans un programme python, on va chercher nos données présentes dans nos collections mongoDB et on les ressort sous la forme d'un fichier CSV. Dans ce même programme, on traite nos données pour avoir toutes les variables nécessaires.

5. **Indexation et Stockage** :
   - Les données enrichies sont stockées dans Elasticsearch, indexées par ...

6. **Visualisation et Analyse** :
   - Kibana est utilisé pour créer des tableaux de bord interactifs, permettant de suivre l'usage des transports en commun en fonction de la météo et de la pollution de l'air.

## Fonctionnalités du Projet

1. **Suivi de l'état du trafic Rennais**
   - **Objectif** : Suivre l'état du trafic rennais avant de connaître les jours et heures d'affluence.
   - **Description** : Il est important de suivre l'état du trafic afin de pouvoir l'améliorer en proposant des déviations aux usagers en cas de forte affluence, ce qui permet de limiter le risque d'accidents et de sur-accidents qui ont entraînés les jours de forte affluence.

2. **Corrélation entre l'état du trafic Rennais et la météo sur une même période**
   **Objectif** : Analyser l’impact des conditions météorologiques et des niveaux de pollution sur le trafic routier afin de proposer des solutions pour améliorer la gestion de la mobilité, réduire les congestions et limiter les risques d’accidents.
   - **Description** : Les conditions météorologiques et la pollution influencent directement le trafic routier, impactant la sécurité, la fluidité et les comportements des usagers. Analyser ces interactions permettrait d’optimiser la gestion de la mobilité urbaine.


## Déroulement Technique du Projet

### **Étapes d'installation :**

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/Coline-T/Transports_meteo
   cd Transports_meteo
   ```

2. **Créer un environnement virtuel :**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Unix
   # Ou
   venv\Scripts\activate     # Windows
   ```

3. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

**Configurer les variables d'environnement :**
   Créez un fichier `.env` et renseignez les informations de connexion MongoDB , OPENAI , le topic kafka , le lien de l'api et Elasticsearch :
   ```env
MONGO_USERNAME="******"
MONGO_PASSWORD="******"
MONGO_DBNAME="*******"
MONGO_URI="*********"
API_URL=https://data.rennesmetropole.fr/api/explore/v2.1/catalog/datasets/etat-du-trafic-en-temps-reel/records
OPENAI_API_KEY="*******"
KAFKA_BROKER=localhost:9092"******"
KAFKA_TOPIC="*******"
   ```

### Sous-Projet : Ingestion et Préparation des Données

Cette partie du projet est un sous-projet spécifique à l'ingestion et à la préparation des données, inclus dans notre projet global Transports_Meteo. Deux pipelines Kedro ont été mis en place pour gérer ces données et les rendre disponibles pour l'analyse et la visualisation :

#### Pipeline ETL

Ce pipeline collecte les données brutes à partir de l'API, les transforme via des étapes de nettoyage et d'enrichissement, puis les stocke dans une base de données MongoDB. Le stockage dans MongoDB permet de centraliser les données transformées pour une utilisation ultérieure, facilitant ainsi les opérations d'analyse et de visualisation.

![alt text](image-4.png)

### **Exécuter localement :**
- **Exécuter tous les pipelines :**
   ```bash
   kedro run
   ```

### Extraction et Ingestion
   - **Données des différents API** : Extraction des données sanitaires avec Python et envoi dans MongoDB.

### Stockage et Indexation avec Elasticsearch
   - Stockage des données des transports rennais, des données météo et des données de la pollution de l'air dans Elasticsearch.

### Visualisation avec Kibana
   - Création de tableaux de bord pour :
     - ...

## Analyses et Indicateurs Attendus ---> A FAIRE

1. **...** : ...
2. **...** : ...
3. **...** : ...
4. **...** : ...

## Exemples de Cas d'Usage

- **Pour les autorités** : Prioriser les contrôles dans les zones ou établissements avec des niveaux d'hygiène et de satisfaction faible.
- **Pour les restaurateurs** : Identifier les aspects (hygiène ou service) à améliorer pour répondre aux attentes des clients.
- **Pour les analystes** : Suivre les tendances régionales en matière de conformité sanitaire et de satisfaction client.

## Déploiement

- **Docker** : Conteneurisation des services (Kafka, Spark, Elasticsearch, Kibana) pour simplifier le déploiement et le scaling.
- **Configurations** : Variables d’API et paramètres de stockage configurables via des fichiers `.env`.
- **Automatisation** : Script de déploiement pour exécuter le pipeline complet.


## Visualisation des Données avec Kibana

Les données collectées et importées dans Elasticsearch  sont visualisées dans Kibana pour une analyse approfondie. Voici un aperçu de certaines visualisations créées pour explorer les avis clients et leurs sentiments.

![alt text](image-6.png)

![alt text](image-5.png)



##  📜 Conclusion <a name="conclusion"></a>

L'application Realtime Restaurant Insights s'est avérée être un atout considérable pour les acteurs de la restauration cherchant à comprendre et à exploiter les retours clients en temps réel. Grâce à l'intégration harmonieuse d'outils tels que Kafka pour l’ingestion de données en temps réel, Apache Spark pour le traitement, et Elasticsearch et Kibana pour l’indexation et la visualisation, l'application permet une exploitation rapide et efficace des données critiques.

Cette solution offre aux restaurateurs une capacité inédite de suivre la satisfaction client, d’identifier les problématiques de manière proactive, et de mettre en œuvre des actions correctives immédiates. Les gestionnaires de chaînes peuvent obtenir une vue d’ensemble de leurs multiples établissements, facilitant une gestion centralisée tout en gardant un œil sur chaque restaurant. Cette vision consolidée améliore non seulement la qualité du service, mais permet aussi une prise de décision fondée sur des informations vérifiées et actuelles.

En utilisant l’API d’OpenAI pour analyser les sentiments des avis clients, l'application est capable de transformer de simples commentaires en indicateurs concrets, fournissant des insights sur les aspects positifs et négatifs du service et des produits. Cela aide non seulement à rehausser l'expérience client, mais permet également aux équipes marketing d’orienter leurs stratégies de manière plus personnalisée et pertinente.

Les fonctionnalités de visualisation des données, avec Kibana, apportent une dimension interactive qui permet de transformer des volumes importants de données en tableaux de bord intuitifs. Ces visualisations permettent aux utilisateurs d'explorer les tendances, de suivre la satisfaction des clients en temps réel, et de prendre des décisions éclairées.

En somme, l’application "Realtime Restaurant Insights" se positionne comme un outil essentiel pour quiconque souhaite rester compétitif dans le secteur de la restauration. Elle aide à optimiser la satisfaction client, améliorer la qualité des services, et exploiter les retours clients de manière constructive. En mettant la donnée au centre de la prise de décision, cette solution représente une avancée majeure vers une gestion proactive et axée sur les résultats pour le secteur de la restauration.



🚧 Difficultés Rencontrées

- **Quota Limité pour l'API d'OpenAI** 
Une des principales difficultés rencontrées concernait l'utilisation de l'API d'OpenAI pour l'analyse des sentiments. L'accès à l'API est limité par un quota d'utilisation, ce qui a parfois restreint le traitement de grands volumes de données en temps réel. Ce quota a nécessité des ajustements dans la fréquence des appels API et une priorisation des avis clients à analyser, surtout en période de forte activité. En conséquence, une stratégie de gestion de quota a dû être mise en place, impliquant notamment la mise en cache des résultats et l'utilisation sélective de l'API pour les avis les plus pertinents.

![alt text](image-1.png)

## Améliorations Futures

1. **Machine Learning pour la prédiction des niveaux de conformité** : Utilisation de modèles pour anticiper les besoins d'inspection.
2. **Intégration d'autres sources d'avis (réseaux sociaux)** : Agrégation d'avis de sources variées pour enrichir les données.
3. **Développement d’une API** : Fournir un accès en temps réel aux indicateurs de qualité des établissements pour des applications externes.

---

##  📊 Docs <a name="documentation"></a>
j'ai documenté plusieurs étapes critiques du projet :

**Airflow**  est utilisé pour orchestrer les pipelines de collecte de données via des DAGs. Un exemple de DAG est utilisé pour envoyer nos données de MongoDB vers Kafka. Ce script Airflow s'exécute toutes les 8 heures. Voici une images du  DAG :

![alt text](image-3.png)

## Contributeurs

- Solenn COULON (@solennCoulon17): Data engineer -**solenn.coulon@supdevinci-edu.fr**
- Coline TREILLE (@Coline-T) : Data analyst -**coline.treille@supdevinci-edu.fr**


## Licence

Ce projet est sous licence MIT. N'hésitez pas à utiliser et modifier le code pour vos propres projets.