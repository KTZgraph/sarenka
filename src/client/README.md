# TODO:

- code of conduct napisać
- tabelka w czystym HTML https://www.youtube.com/watch?v=vIxGDq1SPZQ

# Links

- https://sass-lang.com/documentation/at-rules/mixin
- https://mui.com/material-ui/material-icons/
- https://html-css-js.com/css/generator/box-shadow/
- https://www.npmjs.com/package/react-circular-progressbar
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

```

#### SASS React

- https://www.youtube.com/watch?v=kFA-ZJ9KTqs

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

# __________________________________________________

```js
<span
  className={
    row.status === "Pending"
      ? `${styles.status} ${styles.Pending}`
      : `${styles.status} ${styles.Approved} `
  }
>
```
