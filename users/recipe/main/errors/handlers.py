from flask import Blueprint, render_template
import logging

errors = Blueprint('errors', __name__)
logger = logging.getLogger(__name__)

@errors.app_errorhandler(404)
def error_404(error):
    logger.warning(f'404 error: {error}')
    return render_template('errors/404.html'), 404

@errors.app_errorhandler(403)
def error_403(error):
    logger.warning(f'403 error: {error}')
    return render_template('errors/403.html'), 403

@errors.app_errorhandler(500)
def error_500(error):
    logger.error(f'500 server error: {error}', exc_info=True)
    return render_template('errors/500.html'), 500

@errors.app_errorhandler(Exception)
def handle_exception(error):
    logger.error(f'Unhandled Exception: {error}', exc_info=True)
    return render_template('errors/generic_error.html'), 500
