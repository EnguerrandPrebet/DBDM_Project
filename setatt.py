class SetAttr(set):
    def __repr__(self):
        s = set.__repr__(self)
        return "".join(s[len("SetAttr({"):-len("})")].split(", "))
