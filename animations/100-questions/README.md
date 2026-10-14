# Animation flood : 100 questions

Code de réponse à copier-coller dans le sujet d'animation du **Flood**, pour que chaque membre
réponde aux questions sur son personnage (liste reprise de la page Notion *100 questions* :
7 chapitres, 102 questions).

Le code utilise le composant du forum **`<x-post-admin>`**, le même que les sujets d'event
(ex. *Évent n° 2 : Attrapez les tous !*) : en-tête violet la nuit et bleu le jour, image,
bloc de texte, note (sans image dans la réponse). Le style vient du forum : rien à héberger, et le thème jour / nuit suit tout seul.

| Nuit | Jour | Mobile |
|---|---|---|
| ![](apercu-nuit.png) | ![](apercu-jour.png) | ![](apercu-mobile-nuit.png) |

## Message d'annonce (staff)

[`annonce.html`](annonce.html) : premier message du sujet, à poster tel quel après avoir remplacé
`LIEN_IMAGE_NUIT` / `LIEN_IMAGE_JOUR` (bandeau 600 × 190, une version par thème) et la ligne
`[Durée de l’animation / récompense éventuelle]`. Il explique l'animation et contient le code de
réponse dans un cadre à copier.

| Nuit | Jour |
|---|---|
| ![](annonce-nuit.png) | ![](annonce-jour.png) |

⚠️ **Ne pas mettre le code de réponse dans un `[code]`** : le script du forum (`String.f2p`)
transforme le texte du `[code]` en vrai `<x-post-admin>` avant d'en faire un cadre à copier,
et les membres copieraient le rendu au lieu du code. L'annonce utilise donc un `<textarea>` écrit
sur **une seule ligne**, avec `&#13;` pour les retours à la ligne : testé avec les scripts du
forum, le texte copié est identique à `code-reponse.html`. Si on modifie l'annonce, garder le
`<textarea>` sur une seule ligne (sinon Forumactif y ajoute des `<br />`). Penser à
**prévisualiser** avant de poster, au cas où Forumactif filtrerait le `<textarea>`.

## Mode d'emploi pour les membres

1. Copier tout le contenu de [`code-reponse.html`](code-reponse.html) et le coller dans une réponse.
2. Remplacer :
   - `Nom du personnage · âge · métier · groupe` (sous-titre) ;
   - la citation ;
   - chaque `…` après une question, par ta réponse (sur la même ligne) ;
   - les crédits en bas.
3. Une ligne du code = une ligne affichée : ne pas ajouter de retour à la ligne entre deux questions.

## Structure du code

| Zone | Contenu |
|---|---|
| `post:titre` | « 100 questions » |
| `post:sous-titre` | nom et infos du personnage |
| `post:texte` | citation, puis les 7 chapitres (`Title:H4` jaune la nuit, bleu le jour) et les questions en gras |
| `post:note` | crédits (titre violet clair la nuit, bleu le jour) |

Pour modifier les questions : éditer [`generer.py`](generer.py), puis `python3 generer.py > code-reponse.html`.
