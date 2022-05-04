from pydantic import BaseModel, HttpUrl


def validate_url(url: str) -> None:
    """
    Validates url string.
    :param url: url address
    :return: None
    :raises: pydantic.ValidationError if url is not a valid url address
    """

    class Model(BaseModel):
        url: HttpUrl

    Model(url=url).url
