
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