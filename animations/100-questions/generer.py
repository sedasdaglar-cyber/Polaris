# Génère animations/100-questions/code-reponse.html : le code à coller dans une réponse Forumactif.
# Contrainte : Forumactif transforme chaque retour à la ligne en <br />.
# Tous les conteneurs qui ont des enfants sur plusieurs lignes sont donc en
# display:flex;flex-wrap:wrap;line-height:0 (les <br /> y deviennent invisibles),
# et chaque bloc enfant redéfinit son line-height. Aucun "gap" (il espacerait les <br />).
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
FLEX = "display:flex;flex-wrap:wrap;line-height:0"

def sun(color, gap, cls):
    # Soleil rayonnant en CSS : disque + anneau vide + rayons (conic-gradient).
    return (f'<div class="{cls}" style="position:absolute;top:-80px;right:-80px;width:250px;height:250px;'
            f'border-radius:50%;opacity:.9;background:radial-gradient(circle,{color} 0 27%,{gap} 27.5% 35%,transparent 35.5%),'
            f'repeating-conic-gradient({color} 0 2deg,transparent 2deg 9deg)"></div>')

def star(top, left, size, cls="text-main-white dark:text-secondary-gold"):
    return (f'<span class="{cls}" style="position:absolute;top:{top};left:{left};font-size:{size};'
            f'line-height:1;opacity:.85">✦</span>')

out = []
w = out.append

# Conteneur général
w(f'<div class="text-main-black dark:text-main-white" style="{FLEX};max-width:780px;margin:0 auto;font-family:lato,sans-serif;font-size:14px">')

# ---------- Bandeau ----------
w('<div class="bg-main-blue dark:bg-main-purple" style="position:relative;overflow:hidden;flex:1 1 100%;'
  'border-radius:12px 12px 12px 72px;padding:24px 48px 26px 24px;line-height:1.35;'
  'background-image:linear-gradient(rgba(255,255,255,.08) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.08) 1px,transparent 1px);background-size:32px 32px">'
  + sun("#0F0F0F", "#0C9BC3", "dark:hidden") + sun("#FCC430", "#591696", "hidden dark:block")
  + star("18px", "46%", "18px") + star("64%", "86%", "11px") + star("82%", "8%", "13px")
  + '<span style="position:absolute;right:16px;bottom:18px;writing-mode:vertical-rl;font-size:12px;letter-spacing:8px;color:#fff;opacity:.6;line-height:1">ポラリス</span>'
  + f'<div style="position:relative;{FLEX};align-items:center">')
# Illustration (un seul coin très arrondi)
w('<div style="flex:0 0 150px;height:190px;margin:0 22px 12px 0;border-radius:6px 6px 6px 48px;border:2px solid rgba(255,255,255,.45);'
  'background:rgba(15,15,15,.25) url(LIEN_DE_TON_IMAGE) center/cover no-repeat;display:flex;align-items:center;justify-content:center;'
  'color:#fff;font-size:30px;line-height:1">✦</div>')
# Textes
w(f'<div style="flex:1 1 250px;line-height:1.35">'
  '<span style="display:inline-block;padding:4px 12px;border-radius:32px;background:#FCC430;color:#0F0F0F;font-size:11px;font-weight:700;letter-spacing:1px;text-transform:uppercase">✦ Flood · animation</span>'
  '<div style="margin:12px 0 10px;font-family:motesar,serif;font-size:clamp(36px,7vw,54px);line-height:.95;text-transform:uppercase;color:#fff">100 questions</div>'
  '<div class="text-main-black dark:text-main-white">'
  '<div style="font-size:18px;font-weight:900;letter-spacing:1px;text-transform:uppercase">Nom du personnage</div>')
w('<div style="font-size:13px;font-weight:700;opacity:.85">âge · métier · groupe</div>')
w('<div style="margin-top:10px;font-style:italic">« Une citation de ton personnage. »</div>')
w('</div></div></div></div>')

# ---------- Carte des questions ----------
w('<div class="bg-main-white dark:bg-background-dark border-t-main-blue dark:border-t-main-purple" style="flex:1 1 100%;margin-top:16px;'
  'border-top-width:6px;border-top-style:solid;border-radius:12px;padding:6px 8px 14px 14px;line-height:1.35">'
  f'<div style="{FLEX};align-content:flex-start;max-height:560px;overflow-y:auto;scrollbar-width:thin;padding-right:6px">')

for i, (title, icon, qs) in enumerate(SECTIONS, 1):
    w(f'<div class="border-b-main-blue dark:border-b-secondary-light-purple" style="flex:1 1 100%;display:flex;align-items:center;'
      f'margin:{16 if i > 1 else 10}px 4px 6px;padding-bottom:10px;border-bottom-width:2px;border-bottom-style:solid;line-height:1">'
      f'<span class="bg-secondary-soft-blue dark:bg-secondary-gold/10 {ACCENT}" style="flex:0 0 38px;height:38px;margin-right:12px;border-radius:6px;display:flex;align-items:center;justify-content:center">'
      f'<span class="material-symbols-outlined" style="font-size:22px">{icon}</span></span>'
      f'<span style="flex:1 1 auto"><span class="{ACCENT}" style="display:block;font-size:12px;font-weight:700;letter-spacing:2px">{i:03d}</span>'
      f'<span style="display:block;margin-top:4px;font-family:motesar,serif;font-size:26px;text-transform:uppercase">{title}</span></span>'
      f'<span style="flex:0 0 auto;margin-left:12px;font-size:12px;opacity:.7">{len(qs)} questions</span></div>')
    for q in qs:
        long = isinstance(q, tuple)
        label = q[0] if long else q
        basis = "100%" if long else "200px"
        w(f'<div style="flex:1 1 {basis};margin:4px;padding:10px 12px;border-radius:6px;background:rgba(128,128,128,.12);line-height:1.35">'
          f'<b style="display:block;margin-bottom:3px;font-size:11px;letter-spacing:.6px;text-transform:uppercase;opacity:.7">{label}</b>Ta réponse</div>')

w('</div></div>')

# ---------- Pied ----------
w(f'<div style="flex:1 1 100%;margin-top:10px;padding-right:6px;text-align:right;font-size:11px;letter-spacing:1px;text-transform:uppercase;line-height:1.35;opacity:.7">'
  f'<span class="{ACCENT}">✦</span> {TOTAL} questions · Polaris</div>')
w('</div>')

sys.stdout.write("\n".join(out))
print(TOTAL, file=sys.stderr)
