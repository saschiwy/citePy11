class citepy_config:
    def __init__(self):
        self.custom_methods = {}
        self.methods_to_ignore = []
        self.header_files = []
        self.header_contents = []
        self.no_cpp_doc = True

        self.operator_map = {
            '+': '__add__',
            '-': '__sub__',
            '*': '__mul__',
            '/': '__truediv__',
            '%': '__mod__',
            '==': '__eq__',
            '<': '__lt__',
            '>': '__gt__',
            '<=': '__le__',
            '>=': '__ge__',
            '!=': '__ne__',
            '<<': '__lshift__',
            '>>': '__rshift__',
            '&': '__and__',
            '|': '__or__',
            '^': '__xor__',
            '~': '__invert__',
        }
