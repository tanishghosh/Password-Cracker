from datetime import date, timedelta
from PyPDF2 import PdfFileReader, PdfFileWriter

def decrypt_pdf(input_path, output_path, password):
  with open(input_path, 'rb') as input_file, \
    open(output_path, 'wb') as output_file:
    reader = PdfFileReader(input_file)
    
    r = reader.decrypt(password)
    print(password)
    if r==1:
      '''writer = PdfFileWriter()
      for i in range(reader.getNumPages()):
        writer.addPage(reader.getPage(i))
        writer.write(output_file)'''
      print("password:"+password)
      exit()
    

fi = open("dates.txt",mode='w')
d1 = date(1980, 1, 1)  
d2 = date(2005, 12, 31)  
delta = d2 - d1         
for i in range(delta.days + 1):
    dates = d1 + timedelta(i)
    st = dates.strftime('%d%m%Y')
    st = st.replace('"','')
    decrypt_pdf('C:\\Users\\Tanish Ghosh\\Desktop\\challenge-zero.pdf', 'C:\\Users\\Tanish Ghosh\\Desktop\\output.pdf', st)
    fi.write(st+"\n")
