class ProviderUrl:  # todo: singleton
    def __init__(self):
        self._protonmail = 'https://api.protonmail.ch/pks/lookup?op=index&search='
        self._protonmail_pk = 'https://api.protonmail.ch/pks/lookup?op=get&search='
        self._protonmail_vpn = 'https://api.protonmail.ch/vpn/logicals'

    @property
    def protonmail(self) -> str:
        return self._protonmail

    @property
    def protonmail_pk(self) -> str:
        return self._protonmail_pk

    @property
    def protonmail_vpn(self) -> str:
        return self._protonmail_vpn
