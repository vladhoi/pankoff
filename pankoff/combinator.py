def combine(*validators, **kwargs):
    """
    Returns a combination of validators. E.g
    >>> name_validator = combine(Type, Sized)
    >>> name_validator(types=(str,), min_size=10)
    Of alternativelly:
    >>> name_validator = combine(Type, Sized, types=(str,), min_size=10)
    """
    def __repr__(self):
        validator_names = ", ".join(validator.__name__ for validator in type(self).__bases__)
        return f"Combination of [{validator_names}] validators"

    klass = type(
        "CombinedValidator",
        validators,
        {"__repr__": __repr__}
    )
    klass._validators = klass.__bases__
    if not kwargs:
        return klass
    return klass(**kwargs)