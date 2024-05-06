from flask_injector import inject
from Core.Database.ICompanyDBContext import ICompanyDBContext
from Application.Mappers.CompanyMapper import *
from Application.Responses.Response import Response
from Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from Application.Exceptions.CustomException import CustomException
from Application.Validations.CompanyValidation import ValidateCompany


class DeleteCompanyHandler:

    @inject
    def __init__(self, companyDBContext: ICompanyDBContext):
        self.companyDBContext = companyDBContext

    def Handle(self,request : int):
        try:
            if (request is None):
                raise CustomException(['Solicitud Invalida'])
            else:
                Company = ValidateCompany(self.companyDBContext,request)
                self.companyDBContext.delete(Company)
                return Response('Ha sido exitosa la operacion',HttpStatusCode['NO CONTENT'],'',True,'')
        except CustomException as e:
            raise CustomException(e.errorMessage)
        except Exception as e:
            raise CustomException(['Ha ocurrido un error por favor intente más tarde',str(e)])
            
