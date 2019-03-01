
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
VN_STATS = CLIENT.open('VN-Stats')
SHEET_ONE = VN_STATS.get_worksheet(1)
PARLIAMENT = VN_STATS.worksheet('Parliament')

@BLUEPRINT.route("/progress")
def sheet_one():
    """Display index page"""
    return jsonify(SHEET_ONE.get_all_records())


@BLUEPRINT.route("/parliament")
def parliament():
    """Display index page"""
    return jsonify({
        'labels': PARLIAMENT.row_values(1),
        'dataset': PARLIAMENT.get_all_records()
    })
