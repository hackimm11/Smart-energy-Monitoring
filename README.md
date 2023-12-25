# Smart_electrical_energy_consumption_monitoring
 
Ce projet vise à développer un dispositif de surveillance de l’énergie électrique qui permet de suivre et contrôler la consommation électrique. Pour le réaliser, nous avons utilisé un ESP32 pour récupérer les informations des différents capteurs et envoyer un rapport au consommateur via une plateforme en utilisant comme intermédiaire le Arduino IoT Cloud. Cette plateforme est développer en utilisant le Framework Flask. On a utilisé pour estimer les coûts un modèle que nous l'avons déjà entrainé sur un dataset qui représente la consommation de l'électricité pendant une année. Ce dispositif nous permettra de générer les données de la consommation en temps réel et ensuite les utiliser pour la prédiction des coûts.

# Dataset utilisé

Nous avons utlisé pour entrainer le modèle de prédiction le dataset suivant :

https://www.kaggle.com/datasets/uciml/electric-power-consumption-data-set
