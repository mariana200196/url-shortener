import secrets
import string

from . import schemas

# Stores the URL and shortened URL key in memory
url_dic = {}

def lookup_key(key):
    """Searches the dictionary url_dic for the item matching the key. 

    Args:
        key (str): The unique key corresponding to the actual (target) URL

    Returns:
        target url (str) if key exists, None otherwise

    """
    if key in url_dic:
        return url_dic[key]
    return None

def add_key(url: schemas.URLTarget, key):
    """Creates a dictionary item {key: url} and adds it to url_dic for
    reference. 

    Args:
        url (schemas.URLTarget): The URL to be shortened
        key (str): The unique key generated for the URL

    """
    url_dic[key] = url.url

def create_key(length: int = 5) -> str:
    """Generates a random, 5-character-long key with letters and digits.

    Args:
        length (int): Defaults to 5

    Returns:
        str:  Random key

    """
    chars = string.ascii_letters + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))

def create_unique_key(url: schemas.URLTarget) -> str:
    """Checks that the generated random key is unique. If not unique, 
    discards the key and requests a new one. Unique keys are added to
    url_dic dictionary for reference.

    Args:
        url (schemas.URLTarget): The URL to be shortened

    Returns:
        str:  Unique key

    """
    key = create_key()
    while key in url_dic:
        key = create_key()
    add_key(url, key)
    return key