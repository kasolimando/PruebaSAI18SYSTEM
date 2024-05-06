from flask_injector import inject
from Core.Database.ICompanyDBContext import ICompanyDBContext
from Application.Mappers.CompanyMapper import *
from Application.Responses.Response import Response
from Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from Application.Exceptions.CustomException import CustomException


class ConsultCompanyHandler:

    @inject
    def __init__(self, companyDBContext: ICompanyDBContext):
        self.companyDBContext = companyDBContext

    def Handle(self):
        try:
            Companys = self.companyDBContext.getAll(Company)
            Companys = EntityToRequest(Companys)
            return Response('',HttpStatusCode['OK'],Companys,True,'')
        except CustomException as e:
            raise CustomException(e.errorMessage)  
        except Exception as e:
            raise CustomException(['Ha ocurrido un error por favor intente mas tarde handler',str(e)])
            
