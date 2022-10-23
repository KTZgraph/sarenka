/*
https://youtu.be/DGmX1FDdLZE?t=827

[patrz plik sarenka\src\frontend\client\src\config\index.js]
And the I alson want to have some relative pathing going on in here
because whener I create something like, let's say if I create a navbar which I'm going to need this file sarenka\src\frontend\client\src\jsconfig.js
whre I can set some options so things like compilerOptions
and then here I can have a baseUrl which I can set to source to sarenka\src\frontend\client\src folder
*/

{
    "compilerOptions": {
        "baseUrl": "src"
    },
    "include": ["src"]
}