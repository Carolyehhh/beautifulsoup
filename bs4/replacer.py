class SoupReplacer:
    def __init__(self, og_tag=None, alt_tag=None, name_xformer=None, attrs_xformer=None, xformer=None):
        self.og_tag = og_tag
        self.alt_tag = alt_tag

        # Milestone 3
        self.name_xformer = name_xformer
        self.attrs_xformer = attrs_xformer
        self.xformer = xformer

    def maybe(self, name):
        """Return replacement tag name if matching."""
        if name == self.og_tag:
            return self.alt_tag
        return name
    
    # Milestone 3
    def apply_replacer(self, node):
        """
        Apply Milestone-3 transformers to a node (Tag OR NavigableString).
        """

        # (1) xformer — always run first (Tag or NavigableString 都要)
        if self.xformer:
            try:
                self.xformer(node)
            except Exception:
                pass

        # (2) If node is a Tag, apply tag-specific transforms
        from bs4 import Tag
        if isinstance(node, Tag):

            # Backwards name mapping
            if self.og_tag and self.alt_tag and node.name == self.og_tag:
                node.name = self.alt_tag

            # name_xformer
            if self.name_xformer:
                try:
                    new_name = self.name_xformer(node)
                    if isinstance(new_name, str) and new_name != node.name:
                        node.name = new_name
                except Exception:
                    pass

            # attrs_xformer
            if self.attrs_xformer:
                try:
                    new_attrs = self.attrs_xformer(node)
                    if isinstance(new_attrs, dict):
                        node.attrs = new_attrs
                except Exception:
                    pass

            # (3) Recursively apply to children of Tag
            for child in list(node.children):
                self.apply_replacer(child)
