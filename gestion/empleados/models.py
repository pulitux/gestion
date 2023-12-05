import cx_Oracle


class Empleado:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def buscaporoficio(self,miOficio):
        cursor = self.connection.cursor()
        try:
            consulta = ("SELECT apellido,oficio, salario FROM emp where UPPER(oficio)=UPPER(:p1)")
            cursor.execute(consulta, (miOficio,))

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

    def buscapornombre(self,miNombre):
        cursor = self.connection.cursor()
        try:
            consulta = ("SELECT apellido,oficio, salario FROM emp where UPPER(apellido)=UPPER(:p1)")
            cursor.execute(consulta, (miNombre,))

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

    def oficios(self):
        cursor = self.connection.cursor()

        try:
            consulta = ("select oficio, count(emp_no) from emp group by oficio")
            cursor.execute(consulta)

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

    def nombres(self):
        cursor = self.connection.cursor()

        try:
            consulta = ("select apellido, count(emp_no) from emp group by apellido")
            cursor.execute(consulta)

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor
