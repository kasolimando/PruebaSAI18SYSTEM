from flask import Blueprint, request, jsonify
from flask_injector import inject
from Application.Handlers.Commands.AddCompanyHandler import AddCompanyHandler
from Application.Handlers.Queries.ConsultCompanyHandler import ConsultCompanyHandler
from Application.Handlers.Commands.DeleteCompanyHandler import DeleteCompanyHandler
from Application.Handlers.Commands.PutCompanyHandler import PutCompanyHandler
from Application.Mappers.ResponseMapper import ModifyResponse
from Application.Exceptions.CustomException import CustomException
from Application.Responses.Response import Response
from Infrastructure.Utils.HttpStatusCode import HttpStatusCode
from Application.Requests.CompanyRequest import CompanyRequest

companies = Blueprint("Companies", __name__)

@companies.route("/", methods=['POST'])

@inject
def PostCompany(handler: AddCompanyHandler):
    try:
        response = handler.Handle(CompanyRequest(request))
        return jsonify(ModifyResponse(response)), response.status_code 
    except CustomException as e:
        response = Response('Disculpe ha ocurrido un error',HttpStatusCode['BAD REQUEST'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), HttpStatusCode['BAD REQUEST']
    

@companies.route("/", methods=['GET'])

@inject
def GetCompany(handler: ConsultCompanyHandler):
    try:
        response = handler.Handle()
        return jsonify(ModifyResponse(response)), response.status_code 
    except CustomException as e:
        response = Response('Disculpe ha ocurrido un error',HttpStatusCode['NOT FOUND'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), HttpStatusCode['NOT FOUND']
    


@companies.route("/<int:id>", methods=['DELETE'])

@inject
def DeleteCompany(handler: DeleteCompanyHandler, id):
    try:
        response = handler.Handle(id)
        return jsonify(ModifyResponse(response)), response.status_code 
    except CustomException as e:
        response = Response('Disculpe ha ocurrido un error',HttpStatusCode['NOT FOUND'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), HttpStatusCode['NOT FOUND']
    
@companies.route("/<int:id>", methods=['PUT'])

@inject
def PutCompany(handler: PutCompanyHandler, id):
    try:
        response = handler.Handle(CompanyRequest(request),id)
        return jsonify(ModifyResponse(response)), response.status_code 
    except CustomException as e:
        response = Response('Disculpe ha ocurrido un error',HttpStatusCode['CONFLICT'],'',False,e.errorMessage)
        return jsonify(ModifyResponse(response)), HttpStatusCode['CONFLICT']
