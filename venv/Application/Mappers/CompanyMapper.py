from Core.Entities.Company import Company
from Application.Requests.CompanyRequest import CompanyRequest
import json
from Application.Responses.CompanyResponse import CompanyResponses


def MapRequestEntity(request: CompanyRequest):
    return Company(request.descripcion, 
                   request.direccion1,
                   request.direccion2,
                   request.direccion3,
                   request.telefono1,
                   request.telefono2,
                   request.telefono3,
                   request.correo_electronico,
                   request.pagina_web)

    
def EntityToRequest(companies):
    result = []
    for company in companies:
        surveyReponse = CompanyResponses(company)
        data =  json.loads(json.dumps(surveyReponse.__dict__, ensure_ascii=False))
        result.append(data)
    return result

def EntityToNewEntity(newCompany, oldCompany):
    oldCompany.descripcion = newCompany.descripcion
    oldCompany.direccion1 = newCompany.direccion1
    oldCompany.direccion2 = newCompany.direccion2
    oldCompany.direccion3 = newCompany.direccion3
    oldCompany.telefono1 = newCompany.telefono1
    oldCompany.telefono2 = newCompany.telefono2
    oldCompany.telefono3 = newCompany.telefono3
    oldCompany.correo_electronico = newCompany.correo_electronico
    oldCompany.pagina_web = newCompany.pagina_web