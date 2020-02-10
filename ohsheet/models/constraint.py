import re
from ..exceptions import InvalidConstraintKeySchema

class Constraint:
    def __init__(self, attribute_name, primary, unique, foreign, data_type):
        try:
            self.attribute_name = attribute_name
            self.primary = self._parse_primary
            self.unique = True if unique > 0 else False
            self.foreign = foreign
            self.data_type = data_type
        except (TypeError):
            raise InvalidConstraintKeySchema("Invalid constraint key on attribute %s" % (attribute_name))

    def __repr__(self):
        return '<%s %s, data-type: %s>' % ( self.__class__.__name__,
                                            self.attribute_name,
                                            self.data_type)

    def _parse_primary(self, primary):
        if re.search("auto_increment", primary):
            self.auto_increment = AutoIncrementConstraint(primary.split(".")[1])
            return True
        else:
            return True if primary > 0 else False
    
    def validate_data_type(self, value):
        data_type = self.data_type

        if isinstance(value, str):
            if data_type is 'varchar':
                return True
        elif isinstance(value, int):
            if data_type is 'smallint':
                pass
            elif data_type is 'integer':
                pass
            elif data_type is 'bigint':
                pass
    
    def is_primary_key(self):
        return self.primary

class AutoIncrementConstraint:
    def __init__(self, last_num):
        self.last_num = last_num
    
    def get_next_key(self):
        r = self.last_num
        self.last_num += 1
        return r

    def peek_next_key(self):
        return self.last_num + 1

class ForeignConstraint:
    pass

class DataTypeConstraint:
    pass