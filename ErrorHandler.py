
class RaiseError:
    def END_OF_FILE():
       print("Error : End of file")
       
    def OPEN_COMMENT_FIELD():
        print("Error : Bracket not closed")
        exit(1)

    def MAXINT():
        print("Surpassed max integer value")
        exit(1)
    def MAX_LEN_STR_REACHED():
        print("Surpassed max string lenght")
        exit(1)
    def MAX_LEN_IDENT_REACHED():
        print("Surpassed max IDENT lenght.")
        exit(1)

    def UNILEX_NOT_FOUND():
        print("UNILEX not found")
        exit(1)
    def SYNTAX_ERR_AFF_SYMB():
        print("SYNTAX_ERR_AFF_SYMB")
    def SYNTAX_ERR_AFF_IDENT():
        print("SYNTAX_ERR_AFF_IDENT")

    def SYNTAX_ERR_AFF_SYMB():
        print("SYNTAX_ERR_AFF_SYMB")
    def SYNTAX_ERR_LECT_IDENT():
        print("SYNTAX_ERR_LECT_IDENT")
    def SYNTAX_ERR_LECT_PARENF():
        print("SYNTAX_ERR_LECT_PARENF")
    def SYNTAX_ERR_LECT_PAROUV():
        print("SYNTAX_ERR_LECT_PAROUV")
    def SYNTAX_ERR_ERR_LIRE():
        print("SYNTAX_ERR_ERR_LIRE")
    def SYNTAX_ERR_ECT_EXP():
        print("SYNTAX_ERR_ECT_EXP")
    def SYNTAX_ERR_ECR_PARENF():
        print("SYNTAX_ERR_ECR_PARENF")
    def SYNTAX_ERR_ECR_PAROUV():
        print("SYNTAX_ERR_ECR_PAROUV")
    def SYNTAX_ERR_ECR_MOTCLE():
        print("SYNTAX_ERR_ECR_MOTCLE")
    def SYNTAX_ERR_BLOC_NOT_INST():
        print("SYNTAX_ERR_BLOC_NOT_INST")
    def SYNTAX_ERR_BLOC_PTVIRG():
        print("SYNTAX_ERR_BLOC_PTVIRG")
    def SYNTAX_ERR_BLOC_DEBUT_EXPECTED():
        print("SYNTAX_ERR_BLOC_DEBUT_EXPECTED")
    def SYNTAX_ERR_PROG_OPEN():
        print("SYNTAX_ERR_PROG_OPEN")
    def SYNTAX_ERR_PROG_PTVIRG():
        print("SYNTAX_ERR_PROG_PTVIRG")
    def SYNTAX_ERR_PROG_IDENT_EXPECTED():
        print("SYNTAX_ERR_PROG_IDENT_EXPECTED")
    def SYNATX_ERR_PROG_MISSIG_KEYWORD():
        print("SYNATX_ERR_PROG_MISSIG_KEYWORD")
    def SYNTAX_ERR_CONST_TYPE():
        print("SYNTAX_ERR_CONST_TYPE")
    def SYNTAX_ERR_CONST_EG_EXPECTED():
        print("SYNTAX_ERR_CONST_EG_EXPECTED")
    def SYNTAX_ERR_CONST_IDENT_EXPECTED():
        print("SYNTAX_ERR_CONST_IDENT_EXPECTED")
    def SYNTAX_ERR_CONST_PTVIRG():
        print('SYNTAX_ERR_CONST_PTVIRG')
    def SYNTAX_ERR_VAR_IDENT_EXPECTED():
        print("SYNTAX_ERR_VAR_IDENT_EXPECTED")
    def SYNTAX_ERR_VAR_OPENFIELD():
        print("SYNTAX_ERR_VAR_OPENFIELD")
    def SYNTAX_ERR_VAR_INCORRECT():
        print("SYNTAX_ERR_VAR_INCORRECT")
    def SYNTAX_ERR_SUITE_TERME_EXP_EXPEDCTED():
        print('SYNTAX_ERR_SUITE_TERME_EXP_EXPEDCTED')
    def SYNTAX_ERR_TERME_TERME_EXPECTED():
        print("SYNTAX_ERR_TERME_TERME_EXPECTED()")
    def SYNTAX_ERR_TERME_PAROUV_EXPECTED():
        print("SYNTAX_ERR_TERME_PAROUV_EXPECTED")
    def SYNTAX_ERR_TERME_EXP_INCORRECT():
        print("SYNTAX_ERR_TERME_EXP_INCORRECT")
    def SYNTAX_ERR_TERME_INCORRECT_FORMAT():
        print("SYNTAX_ERR_TERME_INCORRECT_FORMAT")
    def SYNTAX_ERR_PROG_BLOC_EXPECTED():
        print("SYNTAX_ERR_PROG_BLOC_EXPECTED")
    def SYNTAX_ERR():
        print("SYNTAX_ERR")
    def SYNTAX_ERR_CONST_MOTCLE_EXPECTED():
        print("SYNTAX_ERR_CONST_MOTCLE_EXPECTED")
    def DEFINIR_CONSTANTE_ALREADY_DEFINED():
        print('DEFINIR_CONSTANTE_ALREADY_DEFINED')
    def DEFINIR_VAR_ALREADY_DEFINED():
        print("DEFINIR_VAR_ALREADY_DEFINED")
    def SYNTAX_ERR_AFF_VAR_NOT_DECLARED():
        print("SYNTAX_ERR_AFF_VAR_NOT_DECLARED")