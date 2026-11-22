"""Label helpers for user-entered tag names."""


def normalize(label):
    """Return the label lower-cased with outer whitespace dropped."""
    return label.strip().lower()


def is_valid(label, max_length=20):
    """A label is valid when it has 1 to max_length characters once normalized."""
    return 0 < len(normalize(label)) <= max_length


def first_valid(labels, max_length=20):
    """Return the first valid label of the list, normalized."""
    for label in labels:
        if is_valid(label, max_length):
            return normalize(label)
