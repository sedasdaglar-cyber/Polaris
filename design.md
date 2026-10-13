# Polaris — Charte & guide du design system

Référence pour concevoir de nouvelles maquettes à la charte du forum Polaris
(polaris-rpg.forumactif.com) et pour lire le fichier Figma *Polaritz*.

- **Figma** : https://www.figma.com/design/MFIJxpGl2mxRgfUhLCITem/Polaritz (page du DS : `node-id=1-1088`)
- **Implémentation de référence** : [`boutique/boutique.html`](boutique/boutique.html) (tokens, composants et deux thèmes en CSS)
- **Maquette Claude Design** : https://claude.ai/artifact/AEACR1hUkeBX2M6oUmdYfs

> Sources : variables Figma (lues via l'API), captures des planches Buttons, Champs, Color, Typo,
> Search et Header, CSS du forum. Les points non vérifiés dans Figma sont signalés par ⚠️.

---

## 1. Ambiance

Dark mode cosmique / astral, très contrasté.

- Fonds quasi noirs, **violet électrique** comme couleur de marque, **jaune soleil** en accent.
- Illustrations **duotone jaune/noir** (personnages), **soleils rayonnants**, planètes au trait,
  étoiles à 4 branches **✦**, grilles déformées, grain sur les fonds colorés,
  texte japonais vertical décoratif (**ポラリス**).
- Un vrai **mode jour** : le violet y est remplacé par du **bleu cyan**, le jaune reste l'accent.

---

## 2. Couleurs

### 2.1 Variables Figma (source de vérité)

| Variable Figma | Hex | Usage |
|---|---|---|
| `Main/Purple` | `#591696` | Couleur principale **nuit** (boutons, liserés, bandeaux, onglet actif) |
| `Main/Blue` | `#0C9BC3` | Couleur principale **jour** |
| `Main/White` | `#F6F6F6` | Texte nuit, surfaces jour |
| `Main/Black` | `#0F0F0F` | Fond de page nuit, texte jour |
| `Secondary/Light Purple` | `#A771D9` | Accent violet clair, Tags actifs, états « clic » |
| `Secondary/Light Blue` | `#00C1EF` | Accent cyan (jour), dégradés |
| `Secondary/Gold` | `#FCC430` | Accent jaune : icônes, menu, dates, prix, badges |
| `Secondary/Gray` | `#DADADA` | Texte secondaire nuit, champs désactivés |
| `Secondary/Mid Grey` | `#646464` | Texte secondaire jour, bouton désactivé (`#666`) |
| `Secondary/Dark Gray` | `#2C2C2C` | Tags, champs en mode nuit |
| `Background/Dark` | `#1A1A1A` | Cartes / panneaux nuit |
| `Background/Light` | `#EBEFF4` | Fond de page jour |
| `From/error` | `#E73D3D` | Erreur |
| `From/Dark Red` | `#B30808` | Erreur foncée |
| `From/Active` | `#208CEF` | Focus des champs, lien actif |
| `Secondary/Soft Blue` | *(vide)* — `#D3ECF8` relevé sur le site | En-têtes de panneaux jour, fonds d'icônes jour |
| `Secondary/Dark Purple` | *(vide)* — dégradé `#3A0A63 → #56008C` sur la planche | Fonds violets profonds |

Couleurs hors variables, relevées sur le forum :

| Hex | Usage |
|---|---|
| `#141413` | Encarts internes nuit (dernier sujet, onglets inactifs) |
| `#EEEEEE` | Encarts internes jour, fond de bouton secondaire au clic |
| `#AFAFAF` | Texte discret nuit |
| `#8563FF` | Violet vif des dégradés nuit |
| `#4FC3EA` | Bleu clair des états « clic » jour |
| Pseudos de groupe | ambre `#CC8100`, violet `#AF5DD6`, cyan `#129DC9`, vert `#299F75`, rouge `#E55555` |

### 2.2 ⚠️ Piège : les étiquettes de la planche *Color* sont fausses

La planche affiche d'anciens noms et hex (une version « rose » du site). **Fiez-vous aux
variables, jamais aux étiquettes** :

| Étiquette sur la planche | Couleur réelle (variable) |
|---|---|
| Pink `#EA4D6B` | Blue `#0C9BC3` |
| Light Pink `#FF7791` | Light Blue `#00C1EF` |
| Dark Pink `#C61B3D → #E13D5C` | Soft Blue `#D3ECF8` |
| White `#F8F8F8` | `#F6F6F6` |
| Black `#0A0A0A` | `#0F0F0F` |
| Background Dark `#141414` | `#1A1A1A` |
| Background Light `#EBEBEB` | `#EBEFF4` |

Dans Figma : sélectionner l'échantillon → panneau de droite → **Fill** → survoler la variable
(ou passer en **Dev Mode**) pour lire la vraie valeur.

### 2.3 Thèmes nuit / jour

| Rôle | Nuit | Jour |
|---|---|---|
| Fond de page | `#0F0F0F` | `#EBEFF4` |
| Cartes / panneaux / sidebar | `#1A1A1A` | `#F6F6F6` |
| Encarts internes | `#141413` | `#EEEEEE` |
| En-têtes de panneaux et de catégories | `#1A1A1A` | `#D3ECF8` |
| Couleur principale (boutons, liserés, bandeau) | `#591696` | `#0C9BC3` |
| Accent vif (survol, dégradés) | `#8563FF` | `#00C1EF` |
| Menu, icônes, dates | `#FCC430` | `#0C9BC3` |
| Fond du carré d'icône | jaune 12 % `rgba(252,196,48,.12)` | `#D3ECF8` |
| Texte principal | `#F6F6F6` | `#0F0F0F` |
| Texte secondaire | `#DADADA` / `#AFAFAF` | `#3A3A3A` / `#646464` |
| Champs (Search, Select) | `#2C2C2C` | `#FFFFFF` |
| Soleil du bandeau | soleil **jaune** | soleil **noir** |
| Titres Display | blanc | noir (blanc s'ils sont posés sur une image ou un bandeau) |

Les badges SOON / NEW restent **jaune + texte noir** dans les deux thèmes.
Les pseudos gardent leur couleur de groupe dans les deux thèmes.

### 2.4 Tokens CSS prêts à l'emploi

```css
.dark  { --bg:#0F0F0F; --surface:#1A1A1A; --inner:#141413; --header:#1A1A1A;
         --primary:#591696; --primary-soft:#A771D9; --accent:#FCC430; --nav:#FCC430;
         --text:#F6F6F6; --text2:#DADADA; --muted:#AFAFAF; --field:#2C2C2C; }
.light { --bg:#EBEFF4; --surface:#F6F6F6; --inner:#EEEEEE; --header:#D3ECF8;
         --primary:#0C9BC3; --primary-soft:#4FC3EA; --accent:#FCC430; --nav:#0C9BC3;
         --text:#0F0F0F; --text2:#3A3A3A; --muted:#646464; --field:#FFFFFF; }
```

Sur le forum, le thème est piloté par Alpine (`$store.darkMode.toggle()`) et les variantes
Tailwind `dark:` (classe `dark` sur `<html>`).

---

## 3. Typographie

| Style (planche *Typo*) | Police | Notes |
|---|---|---|
| Titre H1 / H2 / H5 | **Display serif décorative** ⚠️ *Motesar* (à confirmer) | Capitales, haute, contrastée. Logo POLARIS ~300 px, titres de section ~30 px, poids 400 |
| Titre H3 | **Lato Bold**, capitales | Variante **Lato Light**, capitales |
| Titre h4 | Lato Bold | Casse normale |
| Bouton | Lato Bold (et Regular pour les petits) | 14–15 px |
| Paragraphe | **Lato Regular 14 px, interligne 1,35** | Style Figma `Main/Paragraphe` |
| Info paragraphe / Question fiche | Lato Bold, petit (~12 px) | Libellés de fiche |
| Libellés de catégories | Lato, capitales, gris, numérotés | « 001. AVANT-PROPOS », « 002. PERSONNAGE » |
| Menu latéral | Lato 14 px, capitales, interlettrage 0,7 px, jaune | |

- Lato est sur Google Fonts. **La police display n'est pas branchée** dans la boutique :
  `Bodoni Moda` sert de remplaçant (`--plr-font-title`). Récupérer le fichier `.woff2`
  de la police réelle pour l'intégrer.
- ⚠️ Tailles exactes H1 → H5 non relevées (limite d'appels Figma atteinte).

---

## 4. Forme, espacement, icônes

- **Rayons** : 6 px (boutons, champs, sélecteurs de quantité) · 12 px (cartes, panneaux) ·
  32 px / pilule (Tags, badges) · grand arrondi sur **un seul coin** pour les bandeaux
  (ex. `12px 12px 12px 72px`).
- **Liseré haut** des cartes : 6 px dans la couleur principale.
- **Grilles** : gap 16–20 px entre cartes ; padding de carte 16–18 px.
- **Cibles tactiles** : 44 px minimum (40 px toléré pour les Tags).
- **Icônes** : contour (outline), trait ~1,5 px, en jaune la nuit / bleu le jour, souvent dans un
  **carré arrondi** (fond jaune translucide la nuit, `#D3ECF8` le jour). Le forum utilise aussi
  Material Symbols. ⚠️ La planche *Iconographie* n'a pas encore été reprise dans la boutique.
- **Décor** : ✦ jaunes ou blancs, grain (bruit ~35 %), grilles blanches à 8 % d'opacité.

---

## 5. Composants

### 5.1 Boutons (planche *Buttons*, `1858:4508`)

Rectangles arrondis 6 px, Lato Bold, flèches ← / → optionnelles de chaque côté du label.

| Variante | Défaut | Survol | Clic | Désactivé |
|---|---|---|---|---|
| **Primaire** nuit | fond `#591696`, texte blanc | fond `#F2F2F2`, bordure 2 px + texte `#591696` | fond `#F2F2F2`, bordure + texte `#A771D9` | fond `#666`, texte blanc |
| **Primaire** jour | fond `#0C9BC3`, texte blanc | fond `#F2F2F2`, bordure + texte `#0C9BC3` | bordure + texte `#4FC3EA` | — |
| **Secondaire** | fond `#F5F5F5`, texte violet (nuit) / bleu (jour), sans bordure | label souligné | fond `#EEEEEE`, label souligné | — |
| **Tertiaire** | texte seul, jaune (nuit) / bleu (jour) | label souligné | quasi transparent | — |

Sur le forum on trouve aussi des CTA « C'est parti ! → » et « Lire le guide », ainsi que
des liens « Lire la fiche → » (petit texte blanc souligné + flèche).

### 5.2 Champs (planche *Champs*, `1858:4509`)

Types : Text, Select, Textfield (compteur 250), File, Search, Dropdown.

| État | Style |
|---|---|
| Default | fond `#F6F6F6`, sans bordure, placeholder **italique** |
| Active (focus) | bordure **bleue `#208CEF`** |
| Valid | bordure noire `#0F0F0F` |
| Error | bordure + label rouge `#E73D3D`, message « error » sous le champ |
| Disabled | fond `#DADADA`, texte grisé |

- Label au-dessus : **capitales, petit, gras** (« LABEL* »), aide en petit gris dessous.
- **Search** : icône loupe **à droite**, placeholder « Recherche ».
- **Select** : chevron ↓ à droite. Variante sombre `#2C2C2C` pour le mode nuit.
- Rayon 6 px.

### 5.3 Tags (frame *Search*, `2863:6946` — composant `SmallSousCate`)

Pastilles-filtres avec case à cocher.

| Prop | Valeurs |
|---|---|
| `state` | `Default` : fond `#2C2C2C`, texte `#F6F6F6`, icône carré vide · `Actif` : fond `#A771D9`, texte `#0F0F0F`, icône case cochée |
| `isIcon` | affiche ou non la case (24 px) |
| `value` | libellé (Lato Regular 14 px / 1,35) |

Padding 8 × 16 px, gap 8 px, rayon 32 px. Ce sont des **cases à cocher** : choix multiple.

### 5.4 Carte raccourci (Listing / Boutique / Annexes / Chronologie)

Fond `#1A1A1A` (nuit) ou `#F6F6F6` (jour), **liseré haut 6–8 px** violet ou bleu, rayon 12 px,
icône jaune ou bleue dans un carré arrondi sombre ou bleu pâle, titre Lato blanc ou noir,
deux sous-liens gris. Badge **SOON** : pilule jaune, texte noir, capitales.
⚠️ Composant `Card` (`2474:4886`) pas encore comparé au pixel.

### 5.5 Panneaux (Suivez l'actualité / Dernières réponses)

En-tête plus clair (`#1A1A1A` sur `#0F0F0F`, ou `#D3ECF8` le jour) avec un **titre Display**.
Lignes : icône jaune ou bleue (alerte, étiquette, calendrier), **date en couleur d'accent, gras**,
texte. Scrollbar fine grise.

### 5.6 Bloc catégorie repliable

En-tête sombre (ou bleu pâle le jour) « **00X. NOM** » en capitales grises + chevron
jaune ou bleu, corps en `#1A1A1A`.

### 5.7 Bandeau de zone / header

- Fond **violet plein** (nuit) ou **cyan** (jour) avec grain et grille, titre Display blanc.
- Illustration duotone avec **un grand arrondi sur un coin**.
- Onglets verticaux à gauche : actif en couleur principale, inactifs sombres avec texte jaune
  (nuit) ou noir (jour), en capitales.
- **Soleil** qui déborde à droite : jaune la nuit, noir le jour (voir 5.8).
- Encart « Nouvelles fiches postées » : avatar carré arrondi, pseudo coloré, sujet gris,
  lien « Lire la fiche → ».

### 5.8 Éléments animés (soleils)

Section *PA* → « Animated elements ».

| Composant | Node | Usage |
|---|---|---|
| `Night_Soleil` (4 variantes) | `947:1390` | Soleil jaune, 216 px |
| `soleil jaune 300300 1` (4 variantes) | `1167:3054` | Soleil jaune, **300 px** (préférer celui-ci) |
| `Soleil noir` (4–5 variantes) | `947:1364` | Soleil noir (mode jour), 300 px |
| `Day_Soleil` (4 variantes) | `1021:1621` | Soleil blanc pointillé (décor jour) |

Les 4 variantes sont le même soleil légèrement tourné : c'est une animation par variantes,
sans images-clés. Sur le web, on la remplace par une **rotation CSS continue** (40 s par tour)
qui s'arrête si `prefers-reduced-motion` est activé. Les PNG exportés sont dans
[`boutique/img/`](boutique/img/).

### 5.9 Badges et états (boutique)

| Élément | Style |
|---|---|
| SOON / NEW / spécial | pilule jaune `#FCC430`, texte noir, capitales, 11 px gras |
| Épuisé | pilule rouge `#E73D3D`, texte blanc, carte à 55 % d'opacité |
| Grade Commun | `#DADADA` |
| Grade Peu commun | `#299F75` |
| Grade Rare | `#208CEF` |
| Grade Épique | `#A771D9` |
| Grade Légendaire | `#FCC430` |
| Texte des badges de grade | toujours `#0F0F0F` (contraste ≥ 4,5:1 sur les 5 couleurs) |
| Prix | gras 900, jaune la nuit, `#086985` le jour |
| Monnaie | **✦** (étoile à 4 branches) |

---

## 6. Accessibilité : points de vigilance

| Combinaison | Contraste | Verdict |
|---|---|---|
| Blanc sur `#591696` | 10,6:1 | ✅ |
| Jaune `#FCC430` sur `#1A1A1A` | 10,8:1 | ✅ |
| Noir sur jaune (badges) | 11,9:1 | ✅ |
| **Blanc sur `#0C9BC3`** (bouton primaire jour) | **3,2:1** | ⚠️ échoue sous 18 px gras. Option : `#0A7FA0` (4,6:1) |
| **Jaune sur cyan** (bandeau jour) | 1,3–2:1 | ❌ ne jamais mettre de texte jaune sur cyan : utiliser le noir |
| `#AFAFAF` sur `#F6F6F6` | 2:1 | ❌ en jour, utiliser `#646464` (5,5:1) |
| Prix `#0C9BC3` sur `#F6F6F6` | 3:1 | ❌ en jour, utiliser `#086985` (5,8:1) |

Autres règles :
- Cibles ≥ 44 px.
- Libellés ≥ 11 px.
- Focus visible (bleu `#208CEF`).
- Ne jamais distinguer deux états par la teinte seule : ajouter une icône (case cochée, coche, etc.).

---

## 7. Lire le fichier Figma

### 7.1 Sections de la page DS (`node-id=1-1088`)

| Section | Node | Contenu |
|---|---|---|
| Typo | `1858:4506` | Échelle des titres et textes |
| Color | `1858:4507` | Palette (⚠️ étiquettes trompeuses, voir 2.2) |
| Buttons | `1858:4508` | Primaire / secondaire / tertiaire × états × thèmes |
| Champs | `1858:4509` | Text `1383:1169`, Select `1383:1233`, Textfield `1383:1266`, File `1383:1197`, Search `2847:6877`, Dropdown `2863:7022` |
| Search (Tags) | `2863:6946` | Pastilles-filtres `SmallSousCate` |
| Iconographie | `1858:4504` | Bibliothèque d'icônes |
| Navigation | `1858:4505` | Sidebar, menus, mobile |
| PA | `1858:4501` | Guide `854:3398`, Contexte `1051:1429`, Actu `1059:1568`, Last post `1059:1626`, **soleils animés** (5.8), Footer `1395:7043`, **Header** `2744:5848`, Card `2474:4886` |
| PA (2) | `1858:4502` | Variantes de pages d'accueil |
| Categories | `1858:4503` | Catégories et forums |
| Profils | `1858:4500` | Profils et fiches |
| Memberlist | `3054:8143` | Liste des membres |
| Sujets | `3524:14468` | Sujets et messages |
| Site annexe | `3263:9096` | Site annexe |
| Page complète | `3478:9615` | Frame 1440 × 3038 |

### 7.2 Conseils de lecture

- **Lien vers un élément précis** : clic droit sur le calque → *Copy link to selection*.
  L'URL contient `node-id=XXXX-YYYY` (le `-` vaut `:`). C'est ce lien qu'il faut donner
  à Claude pour un composant donné.
- **Dev Mode** (`Shift + D`) : affiche les vraies valeurs (variables, tailles, polices) et
  permet d'exporter les assets. Toujours préférer les **variables** aux textes posés sur les planches.
- **Composants à variantes** : les noms `Property 1=…`, `Mode=Light/Night`, `State=Default/Actif`
  indiquent les variantes. Une suite de variantes presque identiques (comme les soleils)
  signale une animation de prototype.
- **Exporter un asset** : sélectionner le calque → panneau *Export* → PNG 2× ou SVG.
  Pour une icône, préférer le SVG et remplacer la couleur par `currentColor`.
- **Limite d'appels** : sur l'offre Figma **Starter**, l'API utilisée par Claude est vite
  limitée. Viser des liens précis (un composant) plutôt qu'une section entière.

---

## 8. Recettes pour une nouvelle maquette

1. **Fond** `--bg`, contenu en cartes `--surface` au rayon 12 px, gap 20 px.
2. **Titre de page** en Display, dans un **bandeau** violet (nuit) ou cyan (jour) avec grain,
   ✦, ポラリス vertical et un soleil qui déborde.
3. **Sections** en blocs repliables « 00X. NOM ».
4. **Actions** : un seul bouton **primaire** par zone ; secondaire pour l'alternative ;
   tertiaire pour les liens d'action discrets (« Effacer », « Retirer »).
5. **Filtres** : Tags `SmallSousCate` à choix multiple. **Recherche** : champ Search, loupe à droite.
6. **Accent jaune** réservé à : icônes, dates, prix, badges. Pas de texte jaune sur fond clair ou cyan.
7. **Toujours prévoir les deux thèmes** avec les correspondances du tableau 2.3.
8. **Mobile** : cartes en lignes (vignette 64 px à gauche), actions principales collées en bas,
   panneaux secondaires en feuille qui monte du bas.

### Brief type à donner à Claude (Claude Design ou code)

> Maquette [écran] pour le forum RPG Polaris, à la charte de `design.md` (dépôt Polaris) :
> thème nuit par défaut + mode jour, tokens 2.3, boutons 5.1, champs 5.2, Tags 5.3,
> cartes à liseré 5.4, bandeau + soleil animé 5.7/5.8. Figma : [lien avec node-id].
> Contenus : [liste]. Desktop 1440 + mobile 390.

---

## 9. Reste à compléter

- [ ] Nom exact et fichier de la police display (Motesar ?) et tailles H1 → H5.
- [ ] Icônes de la planche *Iconographie* (export SVG).
- [ ] Spécifications du composant `Card` (`2474:4886`) et des panneaux.
- [ ] Valeurs des variables vides `Secondary/Soft Blue` et `Secondary/Dark Purple` dans Figma.
- [ ] Décision sur le bleu du bouton primaire jour (`#0C9BC3` du DS ou `#0A7FA0`, plus accessible).
