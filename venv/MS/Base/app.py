from flask import Flask
from Infrastructure.Settings.Config import config
from flask_injector import FlaskInjector, singleton
from Infrastructure.Database.CompanyDBContext import CompanyDBContext
from Core.Database.ICompanyDBContext import ICompanyDBContext
from MS.Controllers import CompanyController

#Se inicializa
app = Flask(__name__)

#se colocan las configuraciones
app.config.from_object(config['development'])

app.register_blueprint(CompanyController.companies, url_prefix='/companies')

def configure(binder):
    binder.bind(ICompanyDBContext, to=CompanyDBContext(app),scope=singleton)

if __name__ == '__main__':
    FlaskInjector(app=app, modules=[configure])
    app.run()