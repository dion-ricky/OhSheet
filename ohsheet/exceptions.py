class OhSheetException(Exception):
    """A base class for ohsheet's exception"""

class InvalidConstraintKeySchema(OhSheetException):
    """"""

class KeyNotUnique(OhSheetException):
    """"""

class DataTypeViolation(OhSheetException):
    """"""