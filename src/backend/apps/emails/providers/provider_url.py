class ProviderUrl:  # todo: singleton
    def __init__(self):
        self._protonmail = 'https://api.protonmail.ch/pks/lookup?op=index&search='

    @property
    def protonmail(self) -> str:
        return self._protonmail
