import validators
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse

from . import schemas, keygen, config

# Instantiate the app
app = FastAPI()


def raise_bad_request(message):
    """Raises HTTPException if target URL is invalid.

    Args:
        message (str): Error message to display

    Raises:
        HTTPException: If target URL is invalid

    """
    raise HTTPException(status_code=400, detail=message)


def raise_not_found(request):
    """Raises HTTPException if client is using an invalid shortened URL 
    to navigate to a target URL or if client is requesting for an
    invalid key to be decoded.

    Args:
        request: URL

    Raises:
        HTTPException: If unique key not found in url_dic dictionary

    """
    message = f"URL '{request.url}' doesn't exist"
    raise HTTPException(status_code=404, detail=message)


@app.get("/")
def read_root():
    """Function associated with root path. All GET requests sent to root
    path are handled by this function.

    Returns:
        str: Short description of service

    """
    return """This is a URL shortener service! 
    POST to the /encode endpoint to shorten your URL. 
    Decode your shortened URL at the decode/{key} endpoint"""


@app.post("/encode", response_model=schemas.URLShort)
def create_url(url: schemas.URLTarget):
    """Function associated with /encode endpoint. Accepts URL string in
    body of POST request and converts it into a shortened URL.

    Args:
        url (schemas.URLTarget): The URL to be shortened

    Returns:
        JSON containing shortened URL

    """
    if not validators.url(url.url):
        raise_bad_request(message="Invalid URL")

    base_url = config.get_settings().base_url
    key = keygen.create_unique_key(url)
    short_url = schemas.URLShort(url=f"{base_url}/{key}")
    return short_url


@app.get("/{key}")
def forward_to_target_url(key: str, request: Request):
    """Function associated with /{key} endpoint. Forwards a GET request 
    to the shortened URL to the actual (target) URL.

    Args:
        key (str): Unique key associated with the target URL
        request (schemas.URLShort): Shortened URL

    Returns:
        Redirects to target URL or raises Error if the key is incorrect/
        doesn't exist

    """
    target_url = keygen.lookup_key(key)
    if target_url:
        return RedirectResponse(target_url)
    else:
        raise_not_found(request)


@app.get("/decode/{key}", response_model=schemas.URLTarget)
def get_target_url(key: str, request: Request):
    """Function associated with /decode endpoint. Converts a shortened 
    URL back into the original URL by checking the shortened URL's 
    unique key.

    Args:
        key (str): Unique key associated with the target URL
        request: URL

    Returns:
        JSON containing original URL or raises Error if key is incorrect/
        doesn't exist

    """
    target_url = keygen.lookup_key(key)
    if target_url:
        return schemas.URLTarget(url=target_url)
    else:
        raise_not_found(request)