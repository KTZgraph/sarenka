<p align="center">
    <img alt="sarenka-logo" src="https://raw.githubusercontent.com/pawlaczyk/sarenka/master/logo.png">
</p>

<p align="center">
    <img alt="sarenka-logo" src="https://raw.githubusercontent.com/pawlaczyk/sarenka/develop/vulns_enpoint.PNG">
</p>

# License

SARENKA is **licensed** under the **[MIT License]**.

[mit license]: https://github.com/pawlaczyk/sarenka/blob/master/LICENSE

# frontend preview
### http://sarenka-develop.pawlaczykdominika.com/

# chrome driver for selenium

https://chromedriver.chromium.org/downloads

# VS Code Extensions

#### Quokka.js (Wallaby.js)

- https://marketplace.visualstudio.com/items?itemName=WallabyJs.quokka-vscode

#### Peacock (John Papa)

- https://marketplace.visualstudio.com/items?itemName=johnpapa.vscode-peacock

#### CodeSnap (adpyke)

- https://marketplace.visualstudio.com/items?itemName=adpyke.codesnap

#### REST Client (Huachao Mao)

- https://marketplace.visualstudio.com/items?itemName=humao.rest-client

#### Thunder Client (Ranga Vadhineni)

- https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client

#### Todo Tree (Gruntfuggly)

- https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree
- https://www.youtube.com/watch?v=Zdz9UYnQHvw

```
# TODO
// TODO
# FIXME
// FIXME
# COMPLETE
// COMPLETE
// BUG

```

```
Ctrl+shift+p
Preferences: Open Settings (JSON)
```

```
  "todo-tree.highlights.defaultHighlight": {
    "icon": "alert",
    "type": "text",
    "foreground": "#FF0000",
    "background": "#ffffff",
    "opacity": 50,
    "iconColour": "#0000FF"
  },
  "todo-tree.highlights.customHighlight": {
    "TODO": {
      "icon": "check",
      "type": "line"
    },
    "FIXME": {
      "foreground": "#000000",
      "iconColour": "#FEDD00",
      "gutterIcon": true

```

#### Marquee (stateful)

- https://marketplace.visualstudio.com/items?itemName=stateful.marquee

#### Import Cost (Wix)

- https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost

#### Code Time (Software)

- https://marketplace.visualstudio.com/items?itemName=softwaredotcom.swdc-vscode

#### Live Server (Ritwick Dey)

- https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer

#### Auto Rename Tag (Jun Han)

- https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-rename-tag

#### Prettier - Code formatter (Prettier)

- https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode [alt + shift +f]

#### ES7+ React/Redux/React-Native snippets (rodrigovallades)

- https://marketplace.visualstudio.com/items?itemName=rodrigovallades.es7-react-js-snippets [rafce]

#### GitLens — Git supercharged (GitKraken)

- https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens

#### IntelliJ IDEA Keybindings (Keisuke Kato)

- https://marketplace.visualstudio.com/items?itemName=k--kato.intellij-idea-keybindings

### Tokyo Night (enkia)

- https://marketplace.visualstudio.com/items?itemName=enkia.tokyo-night

#### Prettier - Code formatter (Prettier)

- https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode
- https://www.robinwieruch.de/how-to-use-prettier-vscode/

## VS Code settings (JSON) summary

```sh
Ctrl + Shift + P
Preferences: Open Settings (JSON)
 -> copy code to json

 ctrl + shift + p
 Todo Tree: Add Tag
 COMPLETE

 -> adds not standard tag `"todo-tree.general.tags": [`
```

```
{
  "workbench.colorTheme": "Tokyo Night Storm",
...


  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 5000,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnPaste": true,
  "editor.formatOnSave": true,

  "todo-tree.highlights.defaultHighlight": {
    "icon": "clippy",
    "type": "text",
    "foreground": "#FF0000",
    "background": "#ffffff",
    "opacity": 50,
    "iconColour": "#0000FF",
    "gutterIcon": true
  },
  "todo-tree.highlights.customHighlight": {
    "TODO": {
      "icon": "calendar",
      "type": "text",
      "iconColour": "#ffee04",
      "foreground": "#FFFFFF",
      "backgourd": "00FF00",
      "gutterIcon": true
    },
    "FIXME": {
      "foreground": "#000000",
      "iconColour": "#FF0000",
      "gutterIcon": true,
      "backgourd": "00FF00"
    },
    "COMPLETE": {
      "icon": "verified",
      "type": "text",
      "foreground": "#FFFFFF",
      "gutterIcon": true,
      "iconColour": "#00FF00",
      "backgourd": "00FF00"
    }
  },
  "todo-tree.general.tags": [
    "BUG",
    "HACK",
    "FIXME",
    "TODO",
    "XXX",
    "[ ]",
    "[x]",
    "COMPLETE"
  ],
  "marquee.widgets.npm-stats.packageNames": ["client"]
}

```

## Client

```sh
cd client
npx create-react-app .
npm install sass
npm install react-router-dom
```
