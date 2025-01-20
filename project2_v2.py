# -*- coding: utf-8 -*-
"""
@author: Maël DIDTSCH
"""
import math

# Définition des tâches avec leurs temps d'exécution (C) et périodes (T)
tasks = {
    'τ1': {'C': 2, 'T': 10},
    'τ2': {'C': 2, 'T': 10},
    'τ3': {'C': 2, 'T': 20},
    'τ4': {'C': 2, 'T': 20},
    'τ5': {'C': 2, 'T': 40},
    'τ6': {'C': 2, 'T': 40},
    'τ7': {'C': 3, 'T': 80}
}



# Étape 1 : Vérification de la planifiabilité via l'utilisation totale
def check_schedulability(tasks):
    U = sum(task['C'] / task['T'] for task in tasks.values())
    U_limit = len(tasks) * (2**(1 / len(tasks)) - 1)
    
    print(f"Utilisation totale U = {U:.2f}, Limite d'utilisation = {U_limit:.2f}")
    if U <= U_limit:
        print("Le système est planifiable sous RMS.")
    else:
        print("Le système n'est PAS planifiable sous RMS.")

# Étape 2 : Exécution tâche par tâche avec vérification des deadlines manquées
def execute_tasks(tasks, hyperperiod):
    timeline = []
    missed_deadlines = []
    
    # Suivi du temps d'exécution restant pour chaque tâche
    task_execution = {task: 0 for task in tasks}
    
    for time in range(hyperperiod):
        current_task = None
        for task, params in sorted(tasks.items(), key=lambda x: x[1]['T']):
            if time % params['T'] == 0:
                task_execution[task] = params['C']
            if task_execution[task] > 0:
                current_task = task
                task_execution[task] -= 1
                break
        
        timeline.append(current_task if current_task else 'Idle')
        
        # Vérifier les deadlines manquées
        for task, params in tasks.items():
            if (time + 1) % params['T'] == 0 and task_execution[task] > 0:
                missed_deadlines.append(task)
    
    print(f"Planning : {timeline}")
    if missed_deadlines:
        print(f"Deadlines manquées : {set(missed_deadlines)}")
    else:
        print("Aucune deadline manquée.")

# Calcul de l'hyperpériode
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def calculate_hyperperiod(tasks):
    periods = [task['T'] for task in tasks.values()]
    hyperperiod = periods[0]
    for period in periods[1:]:
        hyperperiod = lcm(hyperperiod, period)
    return hyperperiod

# Exécution
check_schedulability(tasks)
hyperperiod = calculate_hyperperiod(tasks)
print(f"Hyperpériode : {hyperperiod}")
execute_tasks(tasks, hyperperiod)
