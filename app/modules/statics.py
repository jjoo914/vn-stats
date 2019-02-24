
"""
Gspread module
"""

from flask import Blueprint, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials


BLUEPRINT = Blueprint(
    "statics",
    __name__,
)

CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name(
    'client_secret.json',
    ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
)
CLIENT = gspread.authorize(CREDENTIALS)
SHEET_ONE = CLIENT.open('VN-Stats').get_worksheet(0)
SHEET_TWO = CLIENT.open('VN-Stats').get_worksheet(1)

@BLUEPRINT.route("/progress")
def sheet_one():
    """Display index page"""
    return jsonify(SHEET_ONE.get_all_records())


@BLUEPRINT.route("/parliament")
def sheet_two():
    """Display index page"""
    return jsonify({
        'labels': SHEET_TWO.row_values(1),
        'dataset': SHEET_TWO.get_all_records()
    })
