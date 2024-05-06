from Core.Database.ICompanyDBContext import ICompanyDBContext
from Core.Entities.Company import Company
from Application.Exceptions.CustomException import CustomException
from Application.Validators.CompanyValidator import CompanyValidator


def ValidateData(companyDBContext: ICompanyDBContext, company: Company):
    try:
        validator = CompanyValidator(data=vars(company))
        if validator.validate():
            companyValidate = companyDBContext.getByField(Company,'descripcion', company.descripcion)
            if companyValidate:
                raise CustomException([f'Ya existe la compañia {companyValidate.descripcion}'])
        else:
            raise CustomException(validator.errors.values())
    except CustomException as e:
        raise CustomException(e.errorMessage)
    except Exception as e:
        raise CustomException(['Ha ocurrido un error por favor intente más tarde',str(e)])


def ValidateCompany(companyDBContext: ICompanyDBContext, company):
    companyValidate = companyDBContext.getByField(Company,'compania', company)
    if companyValidate is None:
        raise CustomException([f'No la compañia indicada, por favor verifique he intente nuevamente'])
    return companyValidate


def ValidatePut(newCompany: Company):
    validator = CompanyValidator(data=vars(newCompany))
    if not validator.validate():
        raise CustomException(validator.errors.values())
            