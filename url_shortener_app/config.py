from pydantic import BaseSettings

class Settings(BaseSettings):
    """Subclass of BaseSettings, which defines environment variables.

    By default defines the environment name and base url for local 
    development. Edit env_name and base_url according to your 
    environment.

    Attributes:
        env_name (str): environment name
        base_url (str): domain of your app

    """
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"

def get_settings() -> Settings:
    """Initializes Settings() object.

    Returns:
        Settings() object

    """
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings