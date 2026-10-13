# Boutique Polaris

Page boutique autonome (`boutique.html`) pour le forum, avec des icônes placeholder en attendant les vraies images.

## Intégration Forumactif
Panneau d'admin → Modules → Pages HTML → créer une page, coller le contenu de `boutique.html`
(décocher « Utiliser le header et le footer du forum » si on veut la page plein écran, sinon garder uniquement le `<div class="plr-shop">…</div>` + `<style>` + `<script>`).

## Personnaliser
- **Couleurs / typo** : variables `--plr-*` en haut du `<style>` (tout est scopé sous `.plr-shop`).
- **Images** : dans le tableau `ITEMS`, renseigner `img: "https://…"` ; l'icône placeholder disparaît automatiquement.
- **Lien de commande** : constante `ORDER_URL` (sujet où les membres postent leurs achats).
- **Objets** : source = base Notion « Boutique ». Ajouter/modifier une ligne dans `ITEMS`.

![Aperçu](apercu.png)
