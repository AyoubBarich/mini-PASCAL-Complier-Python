from Precedure import Procedure
import sys
try:
    pro = Procedure(sys.argv[1])
    pro.ANASYNT()
    pro.GENERAT_CODE()
    pro.EXECUTE()
except:
    print("Command should be : compile.py directory-of-the file-to-complie\n Example : compile.py Exemple.pop")