class RaiseError:
    def END_OF_FILE():
       print("Error : End of file")
       exit(0)
    def OPEN_COMMENT_FIELD():
        print("Error : Bracket not closed")
        exit(1)

    def MAXINT():
        print("Surpassed max integer value")
        exit(1)