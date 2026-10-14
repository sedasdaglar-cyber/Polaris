# Génère animations/100-questions/code-reponse.html : le code à coller dans une
# réponse du Flood. Il utilise le composant du forum <x-post-admin> (comme les
# sujets d'event) : chaque <template data-value="post:…"> remplit une zone.
# Forumactif transforme les retours à la ligne en <br /> : dans post:texte,
# une ligne du code = une ligne affichée.
import sys

L = "LONG"  # question à pleine largeur
SECTIONS = [
  ("Généralités", "badge", [
    "Identité", "Date de naissance & signe astro", ("Ses origines", L), "Animaux de compagnie",
    "Adelphes", "Parents", "Lieu d’habitation", ("Ses croyances", L), "Métier", "Études"]),
  ("Physique", "accessibility_new", [
    "Taille", "Poids", "Corpulence", "Cheveux", "Yeux", "Peau", ("Style vestimentaire", L),
    "Piercings & tatouages", "Cicatrices", "Détails particuliers",
    ("Ce qu’il préfère chez lui", L), ("Ce qu’il n’aime pas chez lui", L),
    "Plutôt expressif ou inexpressif", "Type de voix", "Photogénique ou pas",
    "Est-ce qu’il chante bien", "Odeur", "Skincare & haircare"]),
  ("Psychologie", "psychology", [
    ("Ses qualités", L), ("Ses défauts", L), "Son type d’humour", ("Ses peurs", L),
    ("Sa conception du bonheur", L), ("Sa conception de la mort", L),
    ("Un meme / gif qui le décrirait", L), ("Sa philosophie", L), "Ses superstitions",
    "Croit-il en l’astrologie"]),
  ("Habitudes & goûts", "local_cafe", [
    "Droitier, gaucher, ambidextre", "Organisé ou bordélique", "Maniaque ou mimi cracra",
    ("Sa morning routine", L), ("Sa night routine", L), "Early bird ou night owl",
    "Son hygiène de vie", "Couleur préférée", "Animal fétiche", "Chiffre porte-bonheur",
    "Saison préférée", "Boisson préférée", "Plat préféré", "Dessert préféré",
    "Type de musique qu’il écoute", "L’élément qui lui correspond", "Objet fétiche",
    "Matérialiste ou minimaliste", "Sa position favorite pour dormir",
    "Team contractant ou anti-contractant", "Panthéon favori", "Constellation favorite",
    "Lait avant ou après les céréales"]),
  ("Ambitions & expériences", "explore", [
    "Son métier idéal", "Est-ce qu’il veut des enfants", "Veut-il se marier",
    ("Son enfance", L), ("Son plus gros caprice", L), ("Son plus gros sacrifice", L),
    ("Son plus grand regret", L), ("Son plus beau souvenir", L), ("Sa plus grande honte", L),
    "A-t-il déjà été gravement blessé", ("Ses amours", L), "A-t-il trahi quelqu’un",
    "A-t-il été trahi", "A-t-il menti à ses proches"]),
  ("Relationnel", "diversity_3", [
    ("Quelqu’un qui lui manque", L), "En couple ou célibataire", "Amoureux", "Orientation",
    ("Son ou ses meilleurs amis", L), "Sociable ou réservé", "Est-ce une chipie",
    "Est-il jaloux / possessif", "Tendance à rompre ou à se faire plaquer",
    ("Comment est-il quand il est amoureux", L), ("Comment est-il après une rupture", L),
    ("Comment gère-t-il les confessions", L),
    ("Lorsqu’il va mal, a-t-il tendance à s’exprimer ou à tout garder pour lui", L)]),
  ("Polaris", "auto_awesome", [
    ("Que pense-t-il des contractants", L), ("Que pense-t-il des Constellations", L),
    "Des Gardiens", "Des Traqueurs", "Des Dissidents", "Des Satellites",
    "S’intéresse-t-il à la politique", ("S’il devait élire ou réélire un membre de la Commission", L),
    "A-t-il déjà assisté à un procès de l’Héliaste", "L’endroit où il préfère aller",
    "L’endroit qu’il aime le moins", ("Garderait-il une relique pour lui, en secret", L),
    ("S’il pouvait devenir ami avec une Constellation", L),
    ("S’il devait nommer son pouvoir / ses attaques", L)]),
]
TOTAL = sum(len(s[2]) for s in SECTIONS)

ACCENT = "text-main-blue dark:text-secondary-gold"

lines = []
w = lines.append
w('<x-post-admin><template data-value="post:titre">100 questions</template>'
  '<template data-value="post:sous-titre">Nom du personnage · âge · métier · groupe</template>'
  '<template data-value="post:image"><img src="LIEN_DE_TON_IMAGE"></template>'
  f'<template data-value="post:texte"><span class="{ACCENT}">« Une citation de ton personnage. »</span>')
w('')
# Zone qui défile : le premier contenu suit la balise ouvrante pour éviter un <br /> en tête.
body = []
for i, (title, _icon, qs) in enumerate(SECTIONS, 1):
    if i > 1:
        body.append('')
    body.append(f'<span class="Title:H4 {ACCENT}">✦ {i:03d} · {title}</span>')
    for q in qs:
        label = q[0] if isinstance(q, tuple) else q
        body.append(f'<b>{label} :</b> …')
body[0] = '<div style="max-height:460px;overflow-y:auto;scrollbar-width:thin;padding-right:8px">' + body[0]
body[-1] += '</div></template>'
lines += body
lines.append('<template data-value="post:note"><div class="text-main-blue dark:text-secondary-light-purple mb-2">Crédits</div>'
             '&#10022; Avatar : …<br />&#10022; Image : …</template></x-post-admin>')
sys.stdout.write("\n".join(lines))
print(TOTAL, file=sys.stderr)


# ---------------------------------------------------------------------------
# Message d'annonce du sujet (annonce.html), qui contient le code de réponse.
# Le code est dans un <textarea> écrit sur UNE seule ligne :
# - un [code] ne marche pas : le forum transforme son texte en vrai <x-post-admin>
#   (String.f2p remplace &lt; par <) avant d'en faire un textarea ;
# - dans un <textarea>, les balises restent du texte ; les retours à la ligne sont
#   écrits &#13; (Forumactif ne les change pas en <br />, et f2p ne touche que \n).
import html as _html

reponse = "\n".join(lines)
zone = ('<textarea readonly class="bg-white dark:bg-main-black text-main-black dark:text-main-white" '
        'style="display:block;width:100%;height:240px;box-sizing:border-box;margin-top:8px;padding:12px;border:0;'
        'border-radius:4px;font:12px/1.45 ui-monospace,Menlo,Consolas,monospace;resize:vertical">'
        + _html.escape(reponse, quote=False).replace("\n", "&#13;") + '</textarea>')

annonce = "\n".join([
    '<x-post-admin><template data-value="post:titre">Animation : 100 questions</template>'
    '<template data-value="post:sous-titre">Flood, ouvert à tous</template>'
    '<template data-value="post:image"><img class="hidden dark:block" src="LIEN_IMAGE_NUIT"><img class="block dark:hidden" src="LIEN_IMAGE_JOUR"></template>'
    f'<template data-value="post:texte"><span class="{ACCENT}">Flood, animation</span>',
    '',
    'Combien de questions faut-il pour vraiment connaître quelqu’un ? Cent, peut-être.',
    '',
    f'On vous propose de passer votre personnage au crible : son physique, ses petites manies, ses souvenirs, ses amours, ce qu’il pense des Constellations… {TOTAL} questions en tout, réparties en {len(SECTIONS)} chapitres.',
    '',
    f'<span class="{ACCENT}">Comment participer</span>',
    '&#10022; Clique dans le cadre ci-dessous, sélectionne tout (Ctrl + A ou Cmd + A) et copie',
    '&#10022; Colle le code dans une réponse à ce sujet',
    '&#10022; Remplace chaque « … » par ta réponse, sur la même ligne',
    '&#10022; Ajoute ton image (600 × 190) et tes crédits, ou supprime la ligne de l’image',
    zone + '</template>',
    '<template data-value="post:note"><div class="text-main-blue dark:text-secondary-light-purple mb-2">Informations importantes</div>'
    '&#10022; Un message par personnage, les multicomptes sont les bienvenus<br />'
    '&#10022; Pas besoin de tout remplir d’un coup : édite ton message au fur et à mesure<br />'
    '&#10022; Pas d’ordre de passage<br />'
    '&#10022; [Durée de l’animation / récompense éventuelle]</template></x-post-admin>',
])
open(__file__.replace("generer.py", "annonce.html"), "w", encoding="utf-8").write(annonce)
