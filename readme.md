# EcoleDirecte Terminal Client

> [!IMPORTANT]
> Je ne suis en aucun cas affilié à Ecoledirecte. Si vous avez des problèmes avec leur service Web ou Mobile, merci de les contacter (et non moi !)

> Si quelque chose ne fonctionne pas, ou vous avez une suggestion, merci d'ouvrir une ISSUE

Vous avez toujours rêvé d'utiliser EcoleDirecte avec le terminal ? Probablement non, mais maintenant vous le pouvez !

## Sommaire
1. [Installation](#1-installation)
2. [Spécificités](#2-spécificités)

## 1. Installation
Vous pouvez utiliser soit le fichier python du code source ou alors utiliser le binaire trouvable dans la page [Release](https://github.com/julianoMa/ecoledirecte-terminal-client/releases/tag/v1.0.0)
N'oubliez pas d'installer les dépendances nécessaire pour utiliser le fichier python !

## 2. Spécificités
Pour voir les différentes catégories disponibles, vous devez utiliser la commande `cd -help`.

Pour voir son emploi du temps d'une semaine choisie, vous devez d'abord vous rendre dans le répertoire `edt` puis lancer la commande `ls YYYY-MM-DD` (YYYY = année, MM = mois, DD = jour . Vous pouvez mettre n'importe quel jour de la semaine désirée). Pour avoir l'EDT de la semaine en cours, tapez uniquement `ls`

Pour voir les devoirs détaillés, vous devez d'abord vous rendre dans le répertoire `agenda` puis lancer la commande `ls YYYY-MM-DD` (si dans le jour choisi il n'y a aucun devoir, alors rien ne s'affichera)

> [!TIP]
> Pour voir les différentes commandes disponibles écrivez `help`
