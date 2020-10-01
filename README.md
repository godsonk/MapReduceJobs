# À la découverte de MapReduce

Exercice d'application l'article d'introduction à MapReduce disponible sur  [mon blog](https://medium.com/@godsonkkalipe)

### Acquisition des données (IMDB)

Téléchargez et extrayez les données en utilisant les données suivantes :

```
$ wget https://datasets.imdbws.com/title.basics.tsv.gz

$ gunzip title.basics.tsv.gz
```

Pour voir le nombre de lignes du dataset 

```
$ wc -l title.ratings.tsv
```

Nous n'utilserons qu'un échantillon de 100 000 du dataset :
```
$ tail -n 100000 title.basics.tsv > moviesSubset.tsv
```
Ensuite pour exécuter le job MapReduce, il suffit d'utiliser la commande suivante :

```
python3 NombreDeFilmsParTypes.py -r hadoop --hadoop-streaming-jar /home/hdoop/hadoop-3.2.1/share//hadoop/tools/lib/hadoop-streaming-3.2.1.jar moviesSubset.tsv 
```
PS : la position de votre hadoop-streaming-jar sera différente selon votre installation. Assurez-vous que ce chemin est correct
