from wtforms import Form, StringField, validators

class CompanyValidator(Form):

    descripcion = StringField('descripcion', validators=[
        validators.DataRequired(message="Debe ingresar la descripción de la compañia"),
        validators.Length(min=1,max=40, message="Debe tener una longitud de entre 0 a 40 caracteres")
    ])

    direccion1 = StringField('direccion1', validators=[
        validators.DataRequired(message="Debe ingresar la primera dirección"),
        validators.Length(min=1,max=40, message="Debe tener una longitud de entre 0 a 40 caracteres")
    ])

    direccion2 = StringField('direccion2', validators=[
        validators.DataRequired(message="Debe ingresar la segunda dirección"),
        validators.Length(min=1,max=40, message="Debe tener una longitud de entre 0 a 40 caracteres")
    ])

    direccion3 = StringField('direccion3', validators=[
        validators.DataRequired(message="Debe ingresar la tercera dirección"),
        validators.Length(min=1,max=40, message="Debe tener una longitud de entre 0 a 40 caracteres")
    ])

    telefono1 = StringField('telefono1', validators=[
        validators.DataRequired(message="Debe ingresar el primera teléfono"),
        validators.Length(min=1,max=40, message="Debe tener una longitud de entre 0 a 40 caracteres")
    ])


    telefono2 = StringField('telefono2', validators=[
        validators.DataRequired(message="Debe ingresar el segundo teléfono"),
        validators.Length(min=1,max=40, message="Debe tener una longitud de entre 0 a 40 caracteres")
    ])

    telefono3 = StringField('telefono3', validators=[
        validators.DataRequired(message="Debe ingresar el tercer teléfono"),
        validators.Length(min=1,max=40, message="Debe tener una longitud de entre 0 a 40 caracteres")
    ])

    correo_electronico = StringField('correo_electronico', validators=[
        validators.DataRequired(message="Debe ingresar el correo electrónico"),
        validators.Length(min=1,max=40, message="Debe tener una longitud de entre 0 a 40 caracteres")
    ])

    pagina_web = StringField('pagina_web', validators=[
        validators.DataRequired(message="Debe ingresar la página web"),
        validators.Length(min=1,max=40, message="Debe tener una longitud de entre 0 a 40 caracteres")
    ])