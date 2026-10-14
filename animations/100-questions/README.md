# Animation flood : 100 questions

Code de réponse à coller dans le sujet d'animation du **Flood**, pour que chaque membre
réponde aux questions sur son personnage (liste reprise de la page Notion *100 questions* :
7 chapitres, 102 questions).

Le code reprend la charte de [`design.md`](../../design.md) : bandeau violet la nuit et cyan le jour,
grille à 8 %, soleil rayonnant (jaune la nuit, noir le jour), ✦, ポラリス vertical, titres en
*motesar*, carte avec liseré haut de 6 px, sections numérotées « 001 », icônes dans un carré arrondi.

| Nuit | Jour | Mobile |
|---|---|---|
| ![](apercu-nuit.png) | ![](apercu-jour.png) | ![](apercu-mobile-nuit.png) |

## Mode d'emploi pour les membres

1. Copier tout le contenu de [`code-reponse.html`](code-reponse.html).
2. Le coller dans une réponse du sujet (éditeur en mode source / BBCode, HTML activé).
3. Remplacer :
   - `LIEN_DE_TON_IMAGE` : lien de ton image, format portrait (200 × 250 px conseillé) ;
   - `Nom du personnage`, `âge · métier · groupe`, `« Une citation de ton personnage. »` ;
   - chaque `Ta réponse` par ta réponse. Les retours à la ligne dans une réponse sont gardés.
4. Ne touche pas au reste : les questions s'adaptent toutes seules au mode jour / nuit et au mobile.

Les questions sont dans une zone qui défile (560 px de haut) pour ne pas allonger le Flood.

## Notes techniques (Forumactif)

- **Pas de `<style>` ni de `<script>`** : tout est en styles en ligne, plus quelques classes
  Tailwind déjà compilées dans `main.css` du forum pour suivre le thème
  (`bg-main-blue dark:bg-main-purple`, `text-main-blue dark:text-secondary-gold`,
  `hidden dark:block`…). Le thème du forum passe par `[data-theme=dark]`.
- **Retours à la ligne** : Forumactif transforme chaque saut de ligne en `<br />`. Les conteneurs
  sont en `display:flex; flex-wrap:wrap; line-height:0` : les `<br />` y prennent 0 px.
  Chaque bloc redéfinit son `line-height`. Pas de `gap` (il espacerait les `<br />`).
- Polices : *motesar* et *Lato* sont déjà chargées par le forum ; icônes Material Symbols aussi.
- Code de ~39 000 caractères, sous la limite d'un message.
- Pour modifier les questions ou le style : éditer [`generer.py`](generer.py), puis
  `python3 generer.py > code-reponse.html`.
