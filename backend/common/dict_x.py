class DictX(dict):
    """
    Przeglądanei zagnieżdzonych jsonów narzędznie online http://jsonviewer.stack.hu/
    """
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as k:
            raise AttributeError(k)

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError as k:
            raise AttributeError(k)

    def __repr__(self):
        return '<DictX ' + dict.__repr__(self) + '>'


if __name__ == "__main__":
    data = DictX({
        "name": "bo"
    })

    # use dot to get
    print(data.name)
    print(data["name"])

    # use dot to set
    data.state = "NY"
    print(data.state)
    print(data["state"])

    # use dot to delete
    del data.state
    print(data)