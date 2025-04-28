# https://myaccount.google.com/apppasswords 
# qriv cguj yank xqqk 
# avhy fgnt ndaw ldwl 
import smtplib, ssl
from email.message import EmailMessage
def saada_kiri():
    kellele=input("Kellele: ")
    kiri="""<!DOCTYPE html>
<head>
</head>
<body>
<h1>Sending an HTML email from Python</h1>
<p>Hello there,</p>
<a href="https://inspirezone.tech/">Here's a link to an awesome dev
community!</a>
</body>
</html>"""
    smtp_server="smtp.gmail.com"
    smtp_port=587
    kellelt="milamilana2007@gmail.com"
    parool=input("Rakendus parool") #""avhy fgnt ndaw ldwl"
    context=ssl.crate_default_context()
    msg=EmailMessage
    msg.set_content(kiri,subtype="html")
    msg['Subject']="Test"
    msg['From']=kellelt
    msg['To']=kellele
    with open("Pineapple.webp","rb") as f:
        pilt=f.read()
    msg.add_attachment(pilt,maintype="image",subtype="webp",filename="Pineapple.webp")
    try:
        server=smtplib.SMTP(smtp_server, smtp_port)
        server.starttls(context=context)
        server.login(kellelt,parool)
        server.send_message(msg)
        print("Kiri saadetud")
    except Exception as e:
        print("Viga: ",e)
    finally:
        server.quit()



def loe_failist(file:str)->list:
    f=open(file,'r', encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend

def kirjuta_failisse(fail:str,jarjend:list)->list:
    f=open(fail,'w', encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+'\n')
    f.close()

fail=loe_failist('TextFile1.txt')
print(fail)
for i in range(8,11,1):
    fail.append(input(f"{i}-i:"))
kirjuta_failisse('TextFile1.txt',fail)
fail=loe_failist('TextFile1.txt')


