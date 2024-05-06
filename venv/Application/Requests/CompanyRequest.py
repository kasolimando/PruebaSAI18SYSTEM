
class CompanyRequest():
    descripcion =str
    direccion1 = str 
    direccion2 = str 
    direccion3 = str 
    telefono1 = str
    telefono2 = str
    telefono3 = str
    correo_electronico = str 
    pagina_web = str

    def __init__(self,request):
        self.correo_electronico = request.json['correo_electronico']
        self.descripcion = request.json['descripcion']
        self.direccion1 = request.json['direccion1']
        self.direccion2 = request.json['direccion2']
        self.direccion3 = request.json['direccion3']
        self.telefono1 = request.json['telefono1']
        self.telefono2 = request.json['telefono2']
        self.telefono3 = request.json['telefono3']
        self.pagina_web = request.json['pagina_web']