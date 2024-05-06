import itertools
from flask_injector import inject
from Core.Database.ICompanyDBContext import ICompanyDBContext
from Application.Mappers.CompanyMapper import *
from Application.Responses.Response import Response
from Application.Requests.CompanyRequest import CompanyRequest
from Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from Application.Exceptions.CustomException import CustomException
from Application.Validations.CompanyValidation import ValidateData


class AddCompanyHandler:

    @inject
    def __init__(self, companyDBContext: ICompanyDBContext):
        self.companyDBContext = companyDBContext

    def Handle(self,request : CompanyRequest):
        try:
            if (request is None):
                raise CustomException(['Solicitud Inválida'])
            else:
                newCompany = MapRequestEntity(request)
                ValidateData(self.companyDBContext,newCompany)
                self.companyDBContext.save(newCompany)
                return Response('Ha sido existosa la operación',HttpStatusCode['CREATED'],'',True,'')
        except CustomException as e:
            raise CustomException(e.errorMessage)
        except Exception as e:
            raise CustomException(['Ha ocurrido un error por favor intente más tarde',str(e)])
            
