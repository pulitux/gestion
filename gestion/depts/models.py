import cx_Oracle
# import oracledb as cx_Oracle


class Departamento:
    def __init__(self):
        self.connection = cx_Oracle.connect(user="system", password="pythonoracle", dsn="localhost/XE")

    def table(self):
        cursor = self.connection.cursor()
        id = []
        name = []
        loc = []

        try:
            consulta = "select * from DEPT order by DEPT_NO"
            cursor.execute(consulta)
            for i, n, l in cursor:
                id.append(i)
                name.append(n)
                loc.append(l)
            r = {"ids": id, "names": name, "locs": loc}
            return r

        except self.connection.Error as error:
            print("Error: ", error)

    def list(self):
        cursor = self.connection.cursor()

        try:
            consulta = "select * from DEPT order by DEPT_NO"
            cursor.execute(consulta)

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

    def add(self, request):
        cursor = self.connection.cursor()

        numero = int(request.POST['txtNumero'])
        nombre = request.POST['txtNombre'].upper()
        localidad = request.POST['txtLocalidad'].upper()
        try:
            consulta = "insert into DEPT values (:numero, :nombre, :localidad)"
            cursor.execute(consulta, (numero, nombre, localidad))
            self.connection.commit()
            return cursor.rowcount
        except self.connection.Error as error:
            print("Error: ", error)
    def delete(self, request):
        cursor = self.connection.cursor()
        numero = request.POST['txtNumero']
        try:
            consulta = "delete from DEPT where DEPT_NO = :numero"
            cursor.execute(consulta, (numero,))
            self.connection.commit()
            return cursor.rowcount
        except self.connection.Error as error:
            print("Error: ", error)

    def update(self, request):
        cursor = self.connection.cursor()
        numero = request.POST['txtNumero']
        # nombre = request.POST['txtNombre'].upper()
        localidad = request.POST['txtLocalidad'].upper()
        try:
            consulta = "update DEPT set LOC = :localidad where DEPT_NO = :numero"
            cursor.execute(consulta, (localidad, numero))
            self.connection.commit()
            return cursor.rowcount
        except self.connection.Error as error:
            print("Error: ", error)

    def search(self, request):
        cursor = self.connection.cursor()
        numero = request.GET.get('dept')
        try:
            consulta = "select * from DEPT where DEPT_NO = :numero"
            cursor.execute(consulta, (numero,))
        except self.connection.Error as error:
            print("Error: ", error)