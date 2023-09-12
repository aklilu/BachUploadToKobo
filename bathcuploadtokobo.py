import requests
import uuid

from datetime import datetime
import pandas as pd

# https://kcnew.ifrc.org/api/v1/forms find the kpi asset uid for forms here 

#from settings import * #to import MYTOKEN and KPIASSETUID
##################
## RUN SETTINGS ##
##################


##https://kobonew.ifrc.org/token/?format=json
MYTOKEN = ""

#"kpi_asset_uid": 
KPIASSETUID= ""

# https://kcnew.ifrc.org/api/v1/forms find the kpi asset uid 

headers = {
    'Authorization': f'Token {MYTOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
now = datetime.now()
current_time = now.strftime("%Y-%b-%d %I:%M %p")

# Specify the path to your Excel file First Qtr 2022
file_path = 'data/ercs_base_wh_dummy.xlsx'

# Read the Excel file into a Pandas DataFrame
data_frame = pd.read_excel(file_path)

for index, row in data_frame.iterrows():
    # Access values in each column for the current row
    submission = {
        'meta': {
            'instanceID': f'uuid:{uuid.uuid4()}',            
        },
        'Supplier_Donor':row['Supplier_Donor'],
      
        'Local_or_Foreign_Receival':row['Local_or_Foreign_Receival'],
        'Packing_List_Number':row['Packing_List_Number'],
        'Certificate_of_Origin':row['Certificate_of_Origin'],
        'Donation_Certificate':row['Donation_Certificate'],
        'Waybill_Number':row['Waybill_Number'],
        'Contract_Number':row['Contract_Number'],
        'Invoice_Number':row['Invoice_Number'],
        'Purchase_Requisition_Number':row['Purchase_Requisition_Number'],
        'Department_Name':row['Department_Name'],
        'Receiver':row['Receiver'],
        'Purchase_Order':row['Purchase_Order'],
        'Date_of_Reception':row['Date_of_Reception'].date().strftime("%Y-%m-%d"),
        'Items_Inspected_approved':row['Items_Inspected_approved'],
        'Received_By':row['Received_By'],
        'Received_On':row['Received_On'].date().strftime("%Y-%m-%d"),
        'Account_Number':row['Account_Number'],
        'Project_code':row['Project_code'],
        'Items':row['Items'],
        'Remark':row['Remark'],
        'EXPIRY_DATES':row['EXPIRY_DATES'].date().strftime("%Y-%m-%d"),
        'Vender_Manufacturer_No':row['Vender_Manufacturer_No'],
        'Vender_seiral_No':row['Vender_seiral_No'],
        'Unit_of_Measure':row['Unit_of_Measure'],
        'Quantity_Intial':row['Quantity_Intial'],
        'Unit_Price':row['Unit_Price'],
        'Currency_of_Purchase':row['Currency_of_Purchase'],
    
       
    }
 
    data_request = requests.post(
        f'https://kcnew.ifrc.org/api/v1/submissions',
        json={
            "id": f"{KPIASSETUID}",
            "submission": submission
        },
        headers=headers
    )