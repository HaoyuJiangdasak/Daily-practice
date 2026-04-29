import smtplib
import time
import random
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
def send_email():
    try:
        qqMail = smtplib.SMTP_SSL("smtp.qq.com", 465)
        mailUser = "3635229037@qq.com"
        mailPass = "yggserlpxpuucjdd"
        qqMail.login(mailUser, mailPass)

        
        sender = "3635229037@qq.com"
        receiver = "2300740243@qq.com"

        
        message = MIMEMultipart()
        message["Subject"] = Header("有鬼")
        message["From"] = Header(sender)
        message["To"] = Header(receiver)

       
        textContent = "哈哈没事啦"
        mailContent = MIMEText(textContent, "plain", "utf-8")
        message.attach(mailContent)

        
        filePath = r"C:\Users\Lenovo\Desktop\微信图片_20251127155510_178_8.jpg"
        with open(filePath, "rb") as imageFile:
            fileContent = imageFile.read()
        attachment = MIMEImage(fileContent)
        attachment.add_header("Content-Disposition", "attachment", filename="团队合照.png")
        message.attach(attachment)

        
        qqMail.sendmail(sender, receiver, message.as_string())
        print("邮件发送成功")

        qqMail.quit()  
    except Exception as e:
        print(f"邮件发送失败：{str(e)}")
        if "qqMail" in locals():
            try:
                qqMail.quit()  
            except Exception as quit_e:
                print(f"关闭连接时出错：{str(quit_e)}")  
                pass  
            

while True:
    send_email()
    interval = random.uniform(10, 20)
    print(f"等待{interval:.2f}秒后发送下一封...\n")
    time.sleep(interval)