# FreeRTOS-Scheduler

# README

Ce projet contient deux sous-projets principaux :

1. **FreeRTOS**  
2. **Scheduler en Python**

---

## 1. FreeRTOS

### Description
FreeRTOS est un micro-noyau open-source (RTOS : Real-Time Operating System) largement utilisé pour les systèmes embarqués. Il permet de gérer efficacement les ressources d'un microcontrôleur en planifiant et en exécutant plusieurs tâches de manière coordonnée. Cela le rend essentiel pour des applications temps réel où les temps de réponse sont critiques.

### Fonctionnalités mises en œuvre
Dans ce projet FreeRTOS, nous avons :
- Créé plusieurs tâches périodiques et apériodiques.
- Géré des queues pour la communication entre les tâches.
- Implémenté un système simulant des calculs réguliers, des conversions de données et des opérations comme la recherche binaire.

### Instructions de lancement
1. **Compilation** : Assurez-vous que FreeRTOS est configuré correctement.
   ```bash
   make
   ```
2. **Exécution** : Lancez l'exécutable généré.
   ```bash
   ./build/posix_demo
   ```
3. **Observation** : Le comportement des tâches s'affichera dans le terminal.

---

## 2. Scheduler en Python

### Description
Un **scheduler** (ordonnanceur) est un composant essentiel d'un système d'exploitation temps réel. Il décide de l'ordre d'exécution des tâches pour respecter leurs contraintes temporelles. Ce projet Python implémente un scheduler pour vérifier la faisabilité de tâches avec des périodes, des durées d'exécution, et des délais limites (deadlines).

### Fonctionnalités mises en œuvre
- Vérification de la planifiabilité d'un ensemble de tâches.
- Calcul des délais d'attente et maximisation du temps processeur disponible.
- Implémentation en Python avec des algorithmes simples et efficaces.

### Instructions de lancement
1. **Exécution du script Python** :
   ```bash
   python project2_v2.py
   ```
---


