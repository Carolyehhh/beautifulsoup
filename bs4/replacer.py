class SoupReplacer:
    def __init__(self, og_tag, alt_tag):
        self.og_tag = og_tag
        self.alt_tag = alt_tag

    def maybe(self, name):
        """Return replacement tag name if matching."""
        if name == self.og_tag:
            return self.alt_tag
        return name
