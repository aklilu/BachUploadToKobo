import requests
import uuid

from datetime import datetime
import pandas as pd
from settings import *


# https://kcnew.ifrc.org/api/v1/forms find the kpi asset uid for forms here 


headers = {
    'Authorization': f'Token {MYTOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}


now = datetime.now()
current_time = now.strftime("%Y-%b-%d %I:%M %p")

# Specify the path to your Excel file First Qtr 2022
file_path = 'INVENTORY LIST 2022 Third  Quarter Final.xlsx'

# Read the Excel file into a Pandas DataFrame
data_frame = pd.read_excel(file_path)



for index, row in data_frame.iterrows():
    # Access values in each column for the current row
    submission = {
        'meta': {
            'instanceID': f'uuid:{uuid.uuid4()}',            
        },
        'Warehouse name': 'HQ',
        'Project Name': row['Project'],#'ECHO',
        'DESCRIPTION':row['DESCRIPTION'],#'Single bedf',
        'ITEM CODE':row['ITEMCODE'],#'code1',
        'EXPIRY DATES':row['EXPIRYDATES'].date().strftime("%Y-%b-%d"),#'2024-05-06',
        'Unit of measurement':row['UOM'],#'pcs',
        'Department':row['DEPT'],#'DMS',
        'Donor':'NLRC',
        'In or Out':'Out',
        'Total In':0,#780,
        'Total Out':row['ISSUEDQTY'],#0,
        'OPENING Balance':row['OPENINGQTY'],#500,#    'start':current_time,
        'today':now.strftime("%Y-%b-%d"),

    }

    data_request = requests.post(
        f'https://kcnew.ifrc.org/api/v1/submissions',
        json={
            "id": f"{KPIASSETUID}",
            "submission": submission
        },
        headers=headers
    )