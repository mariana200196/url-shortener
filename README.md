# URL Shortener App

This is a url shortening service implemented in Python with the [FastAPI](https://fastapi.tiangolo.com/) framework. It runs locally with supprt from [Uvicorn](https://www.uvicorn.org/) to act as a web server.

The app is a simplified version of the one implemented by Philipp Acsany in his [tutorial](https://realpython.com/build-a-python-url-shortener-with-fastapi/), most notably because it does not use a database.

## Dependencies

To run the app, please install `fastapi`, `uvicorn`, and `validators`.

This project was developed in a conda environment. If you are also using conda, install the packages by running

```
conda install -c conda-forge fastapi
conda install -c conda-forge uvicorn
conda install -c conda-forge validators
```

If you are not using conda, run
```
pip install fastapi
pip install uvicorn
pip install validators
```

## Starting the Web Server

To use the app, start the Uvicorn server by navigating to the `url-shortener-project` directory via the command line. In `url-shortener-project` run

```
uvicorn url_shortener_app.main:app --reload
```

If the start-up was successful, you should see `Application startup complete` printed in the command line. You can check that Uvicorn is running by entering http://localhost:8000/ into your browser. 

## Using the URL Shortener App

You can use the app via the command line, an API like Postman, or your web browser by navigating to http://localhost:8000/docs.

### Encoding a URL
#### With http://localhost:8000/docs:
1. Click on the /encode dropdown
2. Select `Try it out`
3. Replace `"string"` in the `Request body` with your desired URL
4. Click `Execute`

In the `Responses` section below, you will see the generated shortened URL. Paste the shortened URL in the address bar of your web browser to navigate to the target URL.

#### With Postman:
1. Create a new `POST` request
2. Enter the request URL: http://localhost:8000/encode
3. In the `Body` tab of the `Request` section, select the `raw` radio button and then `JSON` instead of `Text` from the dropdown menu
4. Enter a URL to be shortened in the `Body` in JSON format, e.g.
```
{
    "url": "https://www.devtopics.com/best-programming-jokes/"
}
```
5. Click `Send`

In the `Response` section below, under the `Body` tab, you will see the shortened URL. Paste the shortened URL in your web browser to navigate to the target URL.

Note: If the URL you are trying to shorten is invalid (e.g. malformed), you will see an error message.

### Decoding a Shortened URL
#### With a Web Browser
The easiest way is to copy the `key` from the shortened URL
```
http://localhost:8000/{key}
```
and enter the following into your browser's address bar:
```
http://localhost:8000/decode/{key}
```
The target URL will appear in the browser window.

#### With Postman:
1. Create a new `GET` request
2. Copy the `key` from the shortened URL (http://localhost:8000/{key})
3. Enter the request URL: http://localhost:8000/decode/{key}
4. Click `Send`

In the `Response` section below, under the `Body` tab, you will see the original URL. 

Note: If the key doesn't exist (e.g. typo) or has expired because the Uvicorn server was restarted, you will see an error message.

## Running Unit Tests
To run endpoint unit tests, navigate to the `url-shortener-project` directory via the command line. In `url-shortener-project` run
```
python test_endpoints.py
``` 