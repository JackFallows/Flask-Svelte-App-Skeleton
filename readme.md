# Basic Python Flask web app with a Svelte frontend

This template has been made by:
* Partially following the tutorial here: https://cabreraalex.medium.com/svelte-js-flask-combining-svelte-with-a-simple-backend-server-d1bc46190ab9
* But using the Svelte webpack template from here: https://github.com/sveltejs/template-webpack
* And converting to TypeScript using `node scripts/setupTypeScript.js` in the `client` folder

Build the client code by running the following in the `client` folder:
```npm run build-debug```

Then, using the Flask build profile in VSCode, run `server.py`

A separate terminal window in the `client` folder is required to validate the TypeScript with the following command:
```npm run validate```

