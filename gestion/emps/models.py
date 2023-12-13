import cx_Oracle


class Empleado:
    def __init__(self):
        self.connection = cx_Oracle.connect(user="system", password="pythonoracle", dsn="localhost/XE")

    def tablaEmpleados(self):
        cursor = self.connection.cursor()
        id = []
        name = []
        oficio = []
        sup = []
        alta = []
        salario = []
        comision = []
        dept = []

        try:
            consulta = "select * from emp"
            cursor.execute(consulta)
            for i, n, o, su, a, sa, c, d in cursor:
                id.append(i)
                name.append(n)
                oficio.append(o)
                sup.append(su)
                alta.append(a)
                salario.append(sa)
                comision.append(c)
                dept.append(d)
            r = {"ids": id,
                 "names": name,
                 "ofis": oficio,
                 "sups": sup,
                 "altas": alta,
                 "salarios": salario,
                 "coms": comision,
                 "depts": dept}
            return r
        except self.connection.Error as error:
            print("Error: ", error)

    def listaEmpleados(self):
        cursor = self.connection.cursor()

        try:
            consulta = "select * from emp order by emp_NO"
            cursor.execute(consulta)

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

    def add(self, request):
        cursor = self.connection.cursor()

        numero = int(request.POST['txtNumero'])
        nombre = request.POST['txtNombre'].upper()
        oficio = request.POST['txtOficio'].upper()
        sup = int(request.POST['txtSup'])
        alta = request.POST['txtAlta']
        salario = int(request.POST['txtSalario'])
        comision = int(request.POST['txtComision'])
        dept = int(request.POST['txtDepartamento'])
        try:
            consulta = "insert into emp values (:numero, :nombre, :oficio, :sup, to_date(:alta,'yyyy-mm-dd'), :salario, :comision, :dept)"
            cursor.execute(consulta, (numero, nombre, oficio, sup, alta, salario, comision, dept))
            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)
    def delete(self, request):
        cursor = self.connection.cursor()
        numero = int(request.POST['txtNumero'])
        try:
            consulta = "delete from emp where emp_NO = :numero"
            cursor.execute(consulta, (numero,))
            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

    def modify(self, request):
        cursor = self.connection.cursor()
        numero = int(request.POST['txtNumero'])
        salario = int(request.POST['txtSalario'])
        try:
            consulta = "update emp set SALARIO = :salario where emp_NO = :numero"
            cursor.execute(consulta, (salario, numero))
            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)