# Python/Flask web app template with a Svelte frontend

This template has been made by:
* Partially following the tutorial here: https://cabreraalex.medium.com/svelte-js-flask-combining-svelte-with-a-simple-backend-server-d1bc46190ab9
* But using the Svelte webpack template from here: https://github.com/sveltejs/template-webpack
* And converting to TypeScript using `node scripts/setupTypeScript.js` in the `client` folder

Clone into a folder called `webapp` with the following command:
```
npx degit JackFallows/Flask-Svelte-App-Skeleton#playwright-component-tests webapp
```
Then:
* `cd webapp`
* (Optional) Create a Python virtual environment and activate it - see https://code.visualstudio.com/docs/python/environments
* Run `python3 -m pip install -r requirements.txt`
* Then:
* `cd client`
* `npm install`

Build the client code by running the following in the `client` folder:
```
npm run build-debug
```

Then, using the Flask build profile in VSCode, run `app.py`

The following command in the `client` folder is required to validate the TypeScript:
```
npm run validate
```

Run Playwright component tests using:
```
npm run test-ct
```
