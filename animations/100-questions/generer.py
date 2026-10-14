# Génère animations/100-questions/code-reponse.html (le code à coller dans une
# réponse du Flood) et annonce.html (le premier message du sujet).
#
# Réponse : thème « carte du ciel », style perso dans un <style> en fin de code.
# Contraintes Forumactif :
# - chaque retour à la ligne devient <br /> : le <style> tient sur UNE ligne
#   (sinon des <br /> cassent le CSS) et le CSS masque les <br /> placés entre
#   les blocs ; une ligne du code = une question ;
# - le script du forum (String.f2p) remplace [b] [i] [u] [s] [tw] : le CSS n'en contient pas ;
# - tout est préfixé .q100 ; le mode nuit suit [data-theme=dark] du forum.
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

CSS = """
.q100{--bg:#F6F6F6;--band:#0C9BC3;--sun:#0F0F0F;--ink:#0F0F0F;--muted:#646464;--accent:#086985;--star:#0C9BC3;--line:rgba(12,155,195,.45);--dot:rgba(12,155,195,.22);--onband:#0F0F0F;position:relative;max-width:720px;margin:0 auto;overflow:hidden;border-radius:12px;background:var(--bg);color:var(--ink);font-family:lato,sans-serif;font-size:14px;line-height:1.4;counter-reset:q100q q100c}
[data-theme=dark] .q100{--bg:#1A1A1A;--band:#591696;--sun:#FCC430;--ink:#F6F6F6;--muted:#AFAFAF;--accent:#FCC430;--star:#FCC430;--line:rgba(167,113,217,.55);--dot:rgba(246,246,246,.16);--onband:#F6F6F6}
.q100 br{display:none}
.q100-ch p br{display:inline}
.q100-head{position:relative;overflow:hidden;padding:36px 64px 32px 32px;border-radius:0 0 0 72px;background-color:var(--band);background-image:linear-gradient(rgba(255,255,255,.08) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.08) 1px,transparent 1px);background-size:32px 32px;color:var(--onband)}
.q100-sun{position:absolute;top:-96px;right:-96px;width:290px;height:290px;border-radius:50%;background:radial-gradient(circle,var(--sun) 0 26%,var(--band) 26.5% 34%,transparent 34.5%),repeating-conic-gradient(var(--sun) 0 2deg,transparent 2deg 9deg);animation:q100-spin 40s linear infinite}
@keyframes q100-spin{to{transform:rotate(1turn)}}
@media (prefers-reduced-motion:reduce){.q100-sun{animation:none}}
.q100-jp{position:absolute;right:20px;bottom:22px;writing-mode:vertical-rl;font-size:12px;letter-spacing:8px;color:#fff;opacity:.6}
.q100-head p{position:relative;margin:0}
.q100-kicker{display:inline-block;padding:4px 12px;border-radius:32px;background:#FCC430;color:#0F0F0F;font-size:11px;font-weight:700;letter-spacing:1px;text-transform:uppercase}
.q100-head .q100-title{margin-top:16px;font-family:motesar,serif;font-size:clamp(44px,10vw,76px);line-height:.88;text-transform:uppercase;color:#fff}
.q100-head .q100-name{margin-top:18px;font-size:20px;font-weight:900;letter-spacing:1px;text-transform:uppercase}
.q100-head .q100-info{margin-top:2px;font-size:13px;font-weight:700;opacity:.85}
.q100-head .q100-quote{max-width:420px;margin-top:16px;font-style:italic}
.q100-body{padding:4px 32px 28px;background-image:radial-gradient(var(--dot) 1px,transparent 1.6px),radial-gradient(var(--dot) 1px,transparent 1.6px);background-size:47px 47px,71px 71px;background-position:0 0,23px 31px}
.q100-ch{padding-top:40px;counter-increment:q100c}
.q100-qs{columns:2 240px;column-gap:36px}
.q100-h{position:relative;margin:0 0 22px;padding-bottom:10px;border-bottom:2px solid var(--line);font-family:motesar,serif;font-size:30px;line-height:1;text-transform:uppercase}
.q100-h:before{content:"Chapitre " counter(q100c,upper-roman) "  ✦";display:block;margin-bottom:8px;font-family:lato,sans-serif;font-size:12px;font-weight:700;letter-spacing:2px;color:var(--accent)}
.q100-h:after{content:counter(q100c,upper-roman);position:absolute;right:0;bottom:-4px;font-size:92px;line-height:.8;color:transparent;-webkit-text-stroke:1px var(--line);pointer-events:none}
.q100-ch p{position:relative;margin:0 0 0 6px;padding:0 0 18px 20px;border-left:1px dashed var(--line);break-inside:avoid;counter-increment:q100q}
.q100-ch p:before{content:"✦";position:absolute;left:-7px;top:-1px;font-size:13px;line-height:1;color:var(--star);background:var(--bg)}
.q100-ch p b{display:block;margin-bottom:3px;font-size:11px;font-weight:700;letter-spacing:.8px;text-transform:uppercase;color:var(--muted)}
.q100-ch p b:before{content:counter(q100q,q100-pad) "  ";color:var(--accent);letter-spacing:1px}
@counter-style q100-pad{system:extends decimal;pad:3 "0"}
.q100-foot{display:flex;flex-wrap:wrap;justify-content:space-between;gap:6px 16px;padding:14px 32px 20px;border-top:1px solid var(--line);font-size:11px;letter-spacing:1px;text-transform:uppercase;color:var(--muted)}
@media (max-width:600px){.q100-head{padding:28px 48px 26px 20px;border-radius:0 0 0 48px}.q100-sun{top:-70px;right:-70px;width:180px;height:180px}.q100-body{padding:0 20px 24px}.q100-foot{padding:12px 20px 18px}}
"""
css = "".join(l.strip() for l in CSS.strip().splitlines())
for bad in ("[b]", "[i]", "[u]", "[s]", "[tw]", "\n"):
    assert bad not in css.lower(), bad

lines = []
w = lines.append
w('<div class="q100"><div class="q100-head"><div class="q100-sun"></div><span class="q100-jp">ポラリス</span>'
  '<p class="q100-kicker">✦ Flood · 100 questions</p><p class="q100-title">Carte du ciel</p>'
  '<p class="q100-name">Nom du personnage</p><p class="q100-info">âge · métier · groupe</p>'
  '<p class="q100-quote">« Une citation de ton personnage. »</p></div><div class="q100-body">')
for title, _icon, qs in SECTIONS:
    w(f'<div class="q100-ch"><div class="q100-h">{title}</div><div class="q100-qs">')
    for q in qs:
        label = q[0] if isinstance(q, tuple) else q
        w(f'<p><b>{label}</b>…</p>')
    w('</div></div>')
w('</div><div class="q100-foot"><span>✦ Fin de la transmission</span><span>Avatar : …</span></div></div>')
w(f'<style>{css}</style>')
sys.stdout.write("\n".join(lines))
print(TOTAL, file=sys.stderr)


# ---------------------------------------------------------------------------
# Message d'annonce du sujet (annonce.html), qui contient le code de réponse.
# Le code est dans un <textarea> écrit sur UNE seule ligne :
# - un [code] ne marche pas : le script du forum (String.f2p remplace &lt; par <)
#   transforme son texte en vrai HTML avant d'en faire un textarea ;
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
    '&#10022; Complète le nom, les infos, la citation et l’avatar en bas',
    zone + '</template>',
    '<template data-value="post:note"><div class="text-main-blue dark:text-secondary-light-purple mb-2">Informations importantes</div>'
    '&#10022; Un message par personnage, les multicomptes sont les bienvenus<br />'
    '&#10022; Pas besoin de tout remplir d’un coup : édite ton message au fur et à mesure<br />'
    '&#10022; Pas d’ordre de passage<br />'
    '&#10022; [Durée de l’animation / récompense éventuelle]</template></x-post-admin>',
])
open(__file__.replace("generer.py", "annonce.html"), "w", encoding="utf-8").write(annonce)
