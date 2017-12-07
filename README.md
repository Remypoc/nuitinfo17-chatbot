# Dépot de la nuit de l'info 2017 - Chatbot

L'équipe la plus classe du monde:
* Oussema Oulhaci
* Valentin Bouquet
* Rémy Pocquerusse

## Technologies

* Npm: Javascript package manager
* Webpack: Javascript module bundler
* Babel: Transpiling code for new languages features
* React: MVC Framework for dynamic statefull web pages

## Prérequis
* Git, gestionnaire de version - [Télécharger git](https://git-scm.com/downloads)
* Virtualbox, outil de virtualisation - [Télécharger Virtualbox](https://www.virtualbox.org/wiki/Downloads)
* Vagrant, gestionnaire de machine virtuelle - [Télécharger vagrant](https://www.vagrantup.com/downloads.html)

## Installation

```
cd ~/{$project}
vagrant up
vagrant ssh
cd /vagrant
sudo mount --bind $HOME_DIR/vagrant_node_modules $PROJECT_DIR/node_modules
npm run build
node src/server/main.js &

# Accéder au navigateur à l'URL http://localhost:8080
```

## CLI

```
# Lancer webpack avec la configuration pour produire le bundle.js (regroupement des dépendances javascript)
# Option 1
./node_modules/.bin/webpack -d --config webpack-config.js
# Option 2
npm run build
# Option 3, depuis n'importe quel dossier
npm run --prefix /vagrant build

# Lancer webpack pour automatiser la génération à chaque modification
# Attention: problème de synchronisation en dehors de la machine virtuelle

# Option 1
./node_modules/.bin/webpack -d --config webpack-config.js --watch
# Option 2
npm run watch
```