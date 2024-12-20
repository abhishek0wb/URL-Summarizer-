import validators

def validate_url(url):
    """Validate if the provided string is a valid URL."""
    return validators.url(url)
