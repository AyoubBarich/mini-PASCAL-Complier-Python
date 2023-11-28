from enum import Enum
from pyrecord import Record

TYPE = Enum('TYPE',['ent','motcle', 'ident', 'ch', 'virg', 'ptvirg', 'point', 'deuxpts', 'parouv', 'parenf', 'inf', 'sup', 'eg', 'plus', 'moins', 'mult', 'divi', 'infe', 'supe', 'diff', 'aff' ])
TYPE_IDENT = Enum('TYPE_IDENT',['variable','constant'])

# TYPE_IDENT_REC = Record.create_type('TYPE_IDENT_REC','name', 'TYPE_IDENT','INFO',INFO = match TYPE_IDENT )