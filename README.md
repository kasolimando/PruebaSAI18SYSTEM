**Prueba SAI18 System**

Se desarrollo una API en python con FLASK para realizar el CRUD de la entidad COMPAÑIA.

**ENDPOINTS para ser ejecutado de manera local en DEV**

1. ADD COMPANY
   POST http://127.0.0.1:5000/companies

   JSON de Request
   {
   "descripcion": "coca cola",
   "direccion1": "la trinidad",
   "direccion2": "la boyera",
   "direccion3": "los ruices ",
   "telefono1": "1259986",
   "telefono2": "45641",
   "telefono3": "45644541",
   "correo_electronico": "ejemplo@ejemplo.com",
   "pagina_web": "ejemploejemplo.com"
}

3. PUT COMPANY

    PUT http://127.0.0.1:5000/companies/id

   JSON de Request
   {
   "descripcion": "coca cola 2",
   "direccion1": "la trinidad 1",
   "direccion2": "la boyera 1",
   "direccion3": "los ruices 1",
   "telefono1": "1259986",
   "telefono2": "45641",
   "telefono3": "45644541",
   "correo_electronico": "ejemplo@ejemplo.com",
   "pagina_web": "ejemploejemplo.com"
}
5. DELETE COMPANY

    DELETE http://127.0.0.1:5000/companies/id
  
7. SELECT COMPANIES

    GET http://127.0.0.1:5000/companies
