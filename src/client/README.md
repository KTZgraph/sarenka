<!-- FIXME - mirage dummy server podłączać przed wrzuceniem na serwer -->

# chart.js

- https://react-chartjs-2.js.org/examples/radar-chart/
- https://www.youtube.com/watch?v=6jc_GKVNkSs

# D3.js

- npm i d3
- radarchart https://stackoverflow.com/questions/72259679/chartjs-radar-chart-hover-text
- https://jsfiddle.net/qejb9ntu/
- heatmap "d3": "6.7.0", https://codesandbox.io/s/heatmap-d3-tzpnu?file=/package.json
- heatmap basic https://d3-graph-gallery.com/graph/heatmap_basic.html
- https://d3-graph-gallery.com/heatmap
- kolekcja d3.js https://github.com/holtzy/D3-graph-gallery
- google https://www.google.com/search?source=univ&tbm=isch&q=Dataviz&fir=JctDQqFfk99VCM%252CcdocXOTlxdxNvM%252C_%253B_5x0jglXDk6NCM%252CmAPSJHSOQ6Z8DM%252C_%253BrqOQTJVzMaKbPM%252CScCwGlRWX0PzzM%252C_%253BhrluR6jzBIZFiM%252Ca8sFua_1GtbaUM%252C_%253B3BeBzkr75LrymM%252CScCwGlRWX0PzzM%252C_%253B9YicN5YR2SonhM%252CyiPbApK3LAGulM%252C_%253ByLOaCTHqmmH4MM%252Cly1sgApmRIG0SM%252C_%253BzTDtsAQiwsrnaM%252CQ--ZC_KIy93isM%252C_%253BG5FhjqjosaZiUM%252CUFP9EjM8B-yYkM%252C_%253B-B-P9VtROaYUHM%252CSXW4LguSlyls4M%252C_&usg=AI4_-kRzKIHc6CCP6c5_qw74V7gA0wwPHA&sa=X&ved=2ahUKEwi5sKX7yNb6AhUSl4sKHfMXDOcQjJkEegQIOhAC
- https://geojson-maps.ash.ms/ żródło jsona do mapy dla D3.js tylko trzeba dla React zmineić nazwę z końce .json
- https://devdocs.io/d3~7/
- https://rpruim.github.io/D3/notes/d3.html
- http://using-d3js.com/
- google analytics d3js
- google grid-analytics dashboard
- https://www.google.com/imgres?imgurl=https%3A%2F%2Fanmolkoul.files.wordpress.com%2F2015%2F07%2Fgridpreview.gif&imgrefurl=https%3A%2F%2Fwww.kdnuggets.com%2F2015%2F07%2Fvisuals-interactive-dashboard-gridster-d3js.html&tbnid=JNAhN5vSm5oErM&vet=12ahUKEwiMgZ3rhNb6AhUhCBAIHdewA6gQMygBegUIARCtAQ..i&docid=52G7VWy9wqvzIM&w=1366&h=674&q=analytics%20d3js&ved=2ahUKEwiMgZ3rhNb6AhUhCBAIHdewA6gQMygBegUIARCtAQ
- https://www.kdnuggets.com/2015/07/visuals-interactive-dashboard-gridster-d3js.html

# CREATIVE COLOR SCHEMES

- https://creativecolorschemes.com/resources/free-color-schemes/romantic-color-scheme.shtml

# ikonki

- SQL
- https://www.flaticon.com/free-icon/sql-server_5815809
- https://www.flaticon.com/free-icon/files_569809
- https://www.flaticon.com/packs/file-and-folder
- https://www.flaticon.com/free-icon/operating-system_5815980
- https://www.flaticon.com/free-icon/python-file_5815719
- https://www.flaticon.com/packs/coding-and-development-2
- https://www.flaticon.com/packs/documentation-2
- https://www.flaticon.com/free-icon/programing_4824239
- https://www.flaticon.com/free-icon/programing_4824411
- https://www.flaticon.com/free-icon/heart_2724657

<!-- autorzy -->

# cat icon

author: Icon Mela
https://www.flaticon.com/authors/icon-mela
https://www.flaticon.com/free-icon/animal-shelter_7577239?term=cat&page=1&position=6&page=1&position=6&related_id=7577239&origin=style

# tools

png -> svh converter
https://convertio.co/pl/download/7217ec7d2bf7443cc23246e9fbddc64b1689f1/

# notes-service

- https://quilljs.com/docs/api/#text-change

# TODO:

- https://github.com/danilowoz/react-atomic-design
- code of conduct napisać
- tabelka w czystym HTML https://www.youtube.com/watch?v=vIxGDq1SPZQ
- https://github.com/airbnb/javascript/tree/master/react#naming (naming convention)
- https://cpe.mitre.org/specification/
- https://capec.mitre.org/
- https://devtrium.com/posts/async-functions-useeffect

# Links

- https://sass-lang.com/documentation/at-rules/mixin
- https://mui.com/material-ui/material-icons/
- https://html-css-js.com/css/generator/box-shadow/
- https://www.npmjs.com/package/react-circular-progressbar
  ```
  npm install --save react-circular-progressbar
  ```
  - client\src\components\featured\Featured.jsx
    ```js
    import { CircularProgressbar } from "react-circular-progressbar";
    import "react-circular-progressbar/dist/styles.css";
    ...
        <CircularProgressbar value={70} text={"70%"} strokeWidth={5} />
    ...
    ```
- https://recharts.org/en-US/examples/SimpleAreaChart (ten nie)
- https://recharts.org/en-US/api
  ```
  npm install recharts
  ```
  - client\src\components\chart\Chart.module.scss
    - dodać:
      ```js
      import {
      AreaChart,
      Area,
      XAxis,
      YAxis,
      CartesianGrid,
      Tooltip,
      ResponsiveContainer,
      } from "recharts";
      ...
      <ResponsiveContainer width="100%" height="100%">
          <AreaChart ...>
              ...
          </AreaChart>
      </ResponsiveContainer>
      ```

# Charts

- https://uber.github.io/react-vis/examples/showcases/axes
- https://nivo.rocks/line/
- https://recharts.org/en-US/
- https://react-chartjs-2.netlify.app/

# Tables

- https://mui.com/material-ui/react-table/#basic-table
- https://mui.com/material-ui/react-table/#data-table

### paginacja

- https://github.com/mui/mui-x/issues/1907

```
npm install @mui/x-data-grid
```

# CSS normalize

- https://github.com/csstools/normalize.css

```
npm install @csstools/normalize.css --save
```

- https://create-react-app.dev/docs/adding-css-reset/

#### client/src/index.css

```
@import-normalize; /* bring in normalize.css styles */

/* rest of app styles */
```

### libraries

```
npm install @csstools/normalize.css --save
npm install @mui/material @emotion/react @emotion/styled
npm install @mui/icons-material
npm install --save react-circular-progressbar
npm install recharts
npm install @mui/x-data-grid

```

#### SASS React

- https://www.youtube.com/watch?v=kFA-ZJ9KTqs

# Mockowanie serwera

- https://www.youtube.com/watch?v=Xw3K6Kk5Npw
- https://miragejs.com/docs/getting-started/overview/
- https://miragejs.com/docs/getting-started/overview/#shorthands
- https://miragejs.com/docs/getting-started/overview/#relationships
- https://miragejs.com/docs/advanced/graphql/ (GraphQL)

# Struktura komponentów React

## `Atomic Design Principles`

- https://atomicdesign.bradfrost.com/table-of-contents/
- https://andela.com/insights/structuring-your-react-application-atomic-design-principles/
- https://github.com/danilowoz/react-atomic-design (całe repo <3)
- https://danilowoz.com/blog/atomic-design-with-react
- https://szkolareacta.pl/atomic-design/

### Storybook

- https://storybook.js.org/docs/react/get-started/install
- https://www.youtube.com/watch?v=FUKpWgRyPlU
- https://www.youtube.com/watch?v=cx0S8JyiVxc (prop types)
- https://marketplace.visualstudio.com/items?itemName=riccardoforina.storybook-helper Storybook helper (VS Code extension)

```sh
npx sb init
npm run storybook
```

# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)

# TERNARY OPERATOR

- https://stackoverflow.com/questions/29043135/javascript-one-line-if-else-else-if-statement

```js
<span
  className={
    row.status === "Pending"
      ? `${styles.status} ${styles.Pending}`
      : `${styles.status} ${styles.Approved} `
  }
>
```

```js
<div
  className={
    params.row.status === "active"
      ? `${styles.cellWithStatus} ${styles.active}`
      : params.row.status === "passive"
      ? `${styles.cellWithStatus} ${styles.passive}`
      : `${styles.cellWithStatus} ${styles.pending}`
  }
>
  {params.row.status}
</div>
```

```js
a ? a : b ? (c ? c(b) : b) : null;
```

```
a ? a : (b ? (c ? c(b) : b) : null)

a
  ? a
  : b
      ? c
        ? c(b)
        : b
      : null
```

### client\src\components\datatable\DatatableColumns.jsx

```js
...
  //   WARNING uważać na składnie - jak sie zrobi błąd to dane sie nie wyświetlają
  renderCell: (params) => {
    return (
      <div
        className={
          params.row.status === "active"
            ? `${styles.cellWithStatus} ${styles.active}`
            : params.row.status === "passive"
            ? `${styles.cellWithStatus} ${styles.passive}`
            : `${styles.cellWithStatus} ${styles.pending}`
        }
      >
        {params.row.status}
      </div>
    );
  }
...
```

### dodawanie kolumny do tabeli client\src\components\datatable\Datatable.jsx

```js
const a = [1, 2, 3];
const b = ["a", "b"];
a.concat(b);
console.log(a); // [1, 2, 3, "a", "b"]
```

```js
...
  const actionColumn = [
    {
      field: "action",
      headerName: "Action",
      width: 200,
      renderCell: () => {
        return (
          <div className={styles.cellAction}>
            <div className={styles.viewButton}>View</div>
            <div className={styles.deleteButton}>Delete</div>
          </div>
        );
      },
    },
  ];
  ...
        <DataGrid
        rows={userRows}
        columns={userColumns.concat(actionColumn)}
        pageSize={5}
        rowsPerPageOptions={[5]}
        checkboxSelection
        className={styles.dataGrid}
      />
...
```
