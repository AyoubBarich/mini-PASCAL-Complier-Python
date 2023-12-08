from Precedure import Procedure
TestPathComments = "./CommentsTest.txt"
TestPathNumberTest = "./NumberTest.txt"
TestPathProgram = "./ExampleProg.txt"
TestPathExample = "./Exemple.pop"
TestPathExample2 = "./Exemple2.pop"

pro =Procedure(TestPathProgram)
pro.ANASYNT()
pro.GENERAT_CODE()
pro.EXECUTE()