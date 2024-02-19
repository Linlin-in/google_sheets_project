import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Kullanılacak API'ler için kapsamı belirle
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# Hizmet hesabı anahtar dosyasıyla kimlik doğrulama
creds = ServiceAccountCredentials.from_json_keyfile_name(r'C:\Users\pelin\Desktop\sublime-state-414512-10d775f75dda.json', scope)
client = gspread.authorize(creds)

# Google Sheets belgesine erişim
sheet = client.open("ProjectDeneme").sheet1

# Bir hücredeki veriyi oku
cell_value = sheet.acell('A1').value
print(cell_value)

# Bir hücreye veri yaz
sheet.update_acell('B1', 'Hello World!')
