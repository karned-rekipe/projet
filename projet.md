# projet fil rouge

L’idée de cette application est de proposer de planifier pour les jours à venir les repas de la famille en les choisissant parmi les recettes référencées.

La vue principale sera donc un calendrier avec, pour chaque jour, les différents repas de la journée. Sur ces repas, il sera possible de choisir parmi une liste de recettes une ou plusieurs recettes et de définir le nombre de personnes présentes. Cette vue, qui pourra être rendue publique, permettra de consulter le menu d’une période donnée et d’afficher le détail de la recette sélectionnée.

La deuxième fonctionnalité sera la liste des recettes. Chaque recette aura une fiche détaillée avec la méthode pas à pas, la liste des ingrédients et la liste du matériel. Le matériel sera une simple liste d’ustensiles de cuisine. La liste des ingrédients sera plus détaillée, chaque ingrédient aura des informations telles que le groupe alimentaire, l’unité de mesure, le poids d’une portion, le poids moyen, la saisonnalité, le rayon, le ou les fournisseurs. 

La troisième fonctionnalité sera un gestionnaire d’approvisionnement. En fonction des recettes, du nombre de personnes planifiées sur chaque repas et de la période souhaitée, une liste des courses sera établie avec un cumul des quantités nécessaires et une ventilation des ingrédients par fournisseur. Il sera également possible au moment de l’achat de cocher les ingrédients achetés au fur et à mesure et de savoir pour chacun dans quelle recette et à quelle moment de la semaine il sera nécessaire de l’avoir.

Découpage en micro-services
- ingrédent
- ustensile
- recette
- planning
- fournisseur
- utilisateur

## Stack

### API
Fast API  
https://fastapi.tiangolo.com/

### ORM
SQLAlchemy  
https://docs.sqlalchemy.org/en/14/orm/tutorial.html
https://fastapi.tiangolo.com/fr/tutorial/sql-databases/

### Database
PostgreSQL  
MariaDB  

### Front
VueJS  
Angular  
React  