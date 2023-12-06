from enum import Enum



TYPE = Enum('TYPE',['ent','motcle', 'ident', 'ch', 'virg', 'ptvirg', 'point', 'deuxpts', 'parouv', 'parenf', 'inf', 'sup', 'eg', 'plus', 'moins', 'mult', 'divi', 'infe', 'supe', 'diff', 'aff' ])
TYPE_IDENT = Enum('TYPE_IDENT',['variable','constant','NotImplemented','prog'])

def get_type_from_chaine(CHAINE):
    match CHAINE:
        case "VAR":
            return TYPE_IDENT.variable
        case "CONST":
            return TYPE_IDENT.constant
        # case "PROGRAMME":
        #     return TYPE_IDENT.prog
        case _:
            return TYPE_IDENT.NotImplemented

# TYPE_IDENT_REC = Record.create_type('TYPE_IDENT_REC','name', 'TYPE_IDENT','INFO',INFO = match TYPE_IDENT )