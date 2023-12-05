import cx_Oracle


class Departamento:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def tablaDepartamentos(self):
        cursor = self.connection.cursor()
        id = []
        name = []
        loc = []

        try:
            consulta = "select * from dept"
            cursor.execute(consulta)
            for i, n, l in cursor:
                id.append(i)
                name.append(n)
                loc.append(l)
            r = {"ids": id, "names": name, "locs": loc}

        except self.connection.Error as error:
            print("Error: ", error)

        return r
    def listaDepartamentos(self):
        cursor = self.connection.cursor()

        try:
            consulta = "select * from dept"
            cursor.execute(consulta)

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

    def add(self, request):
        cursor = self.connection.cursor()
        numero = request.POST['txtNumero']
        nombre = request.POST['txtNombre'].upper()
        localidad = request.POST['txtLocalidad'].upper()
        try:
            consulta = "insert into dept DNOMBRE values (:numero, :nombre, :localidad)"
            cursor.execute(consulta, (numero, nombre, localidad))
            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)
    def delete(self, request):
        cursor = self.connection.cursor()
        numero = request.POST['txtNumero']
        try:
            consulta = "delete from dept where DEPT_NO = :numero"
            cursor.execute(consulta, (numero,))
            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

    def modify(self, request):
        cursor = self.connection.cursor()
        numero = request.POST['txtNumero']
        # nombre = request.POST['txtNombre'].upper()
        localidad = request.POST['txtLocalidad'].upper()
        try:
            consulta = "update dept set LOC = :localidad where DEPT_NO = :numero"
            cursor.execute(consulta, (localidad, numero))
            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)