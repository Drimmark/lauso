from flask import Blueprint, Response

from models import Survey

survey_module = Blueprint('survey', __name__, template_folder='templates')


@survey_module.route('', methods=['GET'])
def list_surveys():
    return 'list'


@survey_module.route('', methods=['POST'])
def create_survey():
    return 'create'


@survey_module.route('/<int:survey_id>', methods=['GET'])
def get_survey_by_id(survey_id):
    return str(survey_id)


@survey_module.route('/<string:survey_code>', methods=['GET'])
def get_survey_by_code(survey_code):
    survey = Survey.query.filter(Survey.code == survey_code).first()

    if survey is not None:
        return Response(response=survey,
                        status=200,
                        mimetype='application/json')
    return Response(response='',
                    status=404,
                    mimetype='application/json')
