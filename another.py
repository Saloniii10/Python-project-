import pikepdf 
import sys
 def protect_pdf(input_pdf, output_pdf, password) 
try:
  pdf = pikepdf.open(input_pdf) 
  pdf.save(output_pdf, encryption=pikepdf.Encryption(owner=password.
  print(f"Password-protected PDF saved as (output_pdf)")
except Exception as e 
   print(f"Error: (e)")
 
def main(): 
   if len(sys.argv) != 4:
       print("Usage: python3 script.py <input_pdf> <output_pdf> <password>")
sys.exit(1)
 
input_pdf = sys.argv[1]
output_pdf sys.argv[2]
password = sys.argv[3]

protect_pdf(input_pdf, output_pdf, password)
if__name__=="__main()__"
 main()
