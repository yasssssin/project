import script_championnat
import numpy as np

ligue1=script_championnat.Championnat()
ligue1.planifier_matches()
ligue1.jouer_matches()
cl=[]
for i in range(len(ligue1.clubs)):
     n=[]
     n.append(ligue1.clubs[i].points)
     n.append(ligue1.clubs[i].nom)

     cl.append(n)
cl.sort(reverse=True)
for i in range(len(cl)):
     cl[i].append(i+1)
     a=cl[i][0]
     b=cl[i][2]
     cl[i][2]=a
     cl[i][0]=b
print(cl)
# but marques même pour tous les joeurs


