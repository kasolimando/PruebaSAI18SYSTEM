class CompanyResponses:
    compania = int 
    descripcion =str
    direccion1 = str 
    direccion2 = str 
    direccion3 = str 
    telefono1 = str
    telefono2 = str
    telefono3 = str
    correo_electronico = str 
    pagina_web = str


    def __init__(self, response):
        self.compania = response.compania
        self.descripcion = response.descripcion
        self.direccion1 = response.direccion1
        self.direccion2 = response.direccion2
        self.direccion3 = response.direccion3
        self.telefono1 = response.telefono1
        self.telefono2 = response.telefono2
        self.telefono3 = response.telefono3
        self.correo_electronico = response.correo_electronico
        self.pagina_web = response.pagina_web

