"""Label helpers for user-entered tag names."""


def normalize(label):
    """Return the label lower-cased with outer whitespace dropped."""
    return label.strip().lower()


def is_valid(label):
    """A label is valid when it has 1 to 20 characters once normalized."""
    return 0 < len(normalize(label)) <= 20
