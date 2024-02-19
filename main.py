import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Kullanılacak API'ler için kapsamı belirle
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# Hizmet hesabı anahtar dosyasıyla kimlik doğrulama
creds = ServiceAccountCredentials.from_json_keyfile_name(r'C:\Users\pelin\Desktop\sublime-state-414512-10d775f75dda.json', scope)
client = gspread.authorize(creds)

def write_to_sheet(sheet_name, cell, value):
   
    spreadsheet = client.open(sheet_name)
    worksheet = spreadsheet.sheet1
    worksheet.update_acell(cell, value)
    print(f"'{value}' değeri '{sheet_name}' adlı belgenin '{cell}' hücresine yazıldı.")

def read_from_sheet(sheet_name, cell):
    
    spreadsheet = client.open(sheet_name)
    worksheet = spreadsheet.sheet1
    value = worksheet.acell(cell).value
    print(f"'{sheet_name}' adlı belgenin '{cell}' hücresinden okunan değer: {value}")
    return value

sheet_name = 'ProjectDeneme'
#cell = 'A1'

read_value = read_from_sheet(sheet_name, 'C3')
write_value = write_to_sheet(sheet_name, 'A1', 'hof')
