import script_championnat
import numpy as np

ligue1=script_championnat.Championnat()
ligue1.planifier_matches()
ligue1.jouer_matches()
A=np.zeros((len(ligue1.clubs),3))
for i in range(len(ligue1.clubs)):
    A[0]=i+1
    A[1]=ligue1.clubs.nom
    A[2]=ligue1.clubs.points
print(A)


