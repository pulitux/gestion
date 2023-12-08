import cx_Oracle
# import oracledb as cx_Oracle


class Departamento:
    def __init__(self):
        self.connection = cx_Oracle.connect(user="system", password="oraclepass", dsn="localhost/XE")

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
            return r

        except self.connection.Error as error:
            print("Error: ", error)

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

        numero = int(request.POST['txtNumero'])
        nombre = request.POST['txtNombre'].upper()
        localidad = request.POST['txtLocalidad'].upper()
        try:
            consulta = "insert into dept values (:numero, :nombre, :localidad)"
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

    def search(self, request):
        cursor = self.connection.cursor()
        numero = request.GET.get('dept')
        try:
            consulta = "select * from dept where DEPT_NO = :numero"
            cursor.execute(consulta, (numero,))
        except self.connection.Error as error:
            print("Error: ", error)