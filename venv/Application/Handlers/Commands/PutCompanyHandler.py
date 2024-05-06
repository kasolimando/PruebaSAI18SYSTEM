import itertools
from flask_injector import inject
from Core.Database.ICompanyDBContext import ICompanyDBContext
from Application.Mappers.CompanyMapper import *
from Application.Responses.Response import Response
from Application.Requests.CompanyRequest import CompanyRequest
from Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from Application.Exceptions.CustomException import CustomException
from Application.Validations.CompanyValidation import ValidateCompany,ValidatePut


class PutCompanyHandler:

    @inject
    def __init__(self, companyDBContext: ICompanyDBContext):
        self.companyDBContext = companyDBContext

    def Handle(self,request : CompanyRequest, requestId : int):
        try:
            if (request is None or requestId is None):
                raise CustomException(['Solicitud Invalida'])
            else:
                newCompany = MapRequestEntity(request)
                oldCompany = ValidateCompany(self.companyDBContext,requestId)
                ValidatePut(newCompany)
                EntityToNewEntity(newCompany,oldCompany)
                self.companyDBContext.Commit()
                return Response('La operación ha sido exitosa',HttpStatusCode['OK'],'',True,'')
        except CustomException as e:
            raise CustomException(list(itertools.chain(*e.errorMessage)))
        except Exception as e:
            raise CustomException(['Ha ocurrido un error por favor intente más tarde',str(e)])
            
