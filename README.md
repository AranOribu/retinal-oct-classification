# Contexte du projet

Vous venez de rejoindre une start-up MedTech en tant que développeur.se IA.

L'entreprise a remporté un appel d'offre du CHRU de Nancy pour la réalisation d'un POC (Proof Of Concept) d'une solution IA capable de diagnostiquer les maladies de la rétines à partir d'imagerie par OCT.

​

L’imagerie par OCT permet de détecter soit un épaississement de la rétine, soit la présence d’anomalie dans ou sous la rétine (œdème, néovaisseaux, atrophie, membrane, etc.) Cet examen permet d’analyser les conséquences de pathologies rétiniennes comme la dégénérescence maculaire liée à l’âge, la rétinopathie diabétique, les occlusions vasculaires, etc.

​

Une première version a été développée par un doctorant de l'INRIA. Il s'agit d'une API qui permet de prédire à partir d'une imagerie par OCT :

une néovascularisation choroïdienne
un Œdème maculaire diabétique
de multiples drusen
une rétine normale
Vous avez comme mission d'améliorer le modèle (en modifiant ses paramètres ou en utilisant une autre architecture) et de développer une application avec une page de prédiction (chargement d'une imagerie par OCT et affichage de la prédiction).

# Data:

Le jeu de données : https://data.mendeley.com/datasets/rscbjbr9sj/2

# Model

Une architecture VGG16 CNN est utilisée pour la calssification, pré-entraînée sur le jeu de données 'ImageNet'. Le code complet est disponible ici : https://colab.research.google.com/drive/1UzymPZ7DOG9JO2nOEA4IndMaed1kzQyK?usp=sharing


Le model entrainé : https://drive.google.com/file/d/16IakjbSdWZVAk9Y5eEiDlaJqKhCi-9EL/view?usp=share_link
à enregistrer dans le dossier model/v2

Citation: http://www.cell.com/cell/fulltext/S0092-8674(18)30154-5

![image](https://user-images.githubusercontent.com/64967048/234588397-a3ff4c79-a5f2-4f29-aa59-4c94d89b15c9.png)
