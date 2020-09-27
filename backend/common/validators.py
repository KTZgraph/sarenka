from pydantic import BaseModel, HttpUrl


class URL(BaseModel):
    """
    Validate url from user (especially from naughty user)
    """
    url: HttpUrl
