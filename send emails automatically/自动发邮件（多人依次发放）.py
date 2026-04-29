import smtplib
import time
import random
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
interval_min = 30
interval_max = 60
fail_send = []
receivers =["3466275913@qq.com"] 
def send_single_email(receiver):
    qqMail = None
    try:
        qqMail = smtplib.SMTP_SSL("smtp.qq.com", 465)
        mailUser = "3635229037@qq.com"
        mailPass = "yggserlpxpuucjdd"
        qqMail.ehlo()
        qqMail.login(mailUser, mailPass)
        sender = "3635229037@qq.com"
        message = MIMEMultipart()
        message["Subject"] = Header("没事")
        message["From"] = Header(sender)
        message["To"] = Header(receiver)
        textContent = "哈哈没事啦"
        mailContent = MIMEText(textContent, "plain", "utf-8")
        message.attach(mailContent)
        filePath = r"C:\Users\Lenovo\Desktop\微信图片_20251127155510_178_8.jpg"
        with open(filePath, "rb") as imageFile:
            fileContent = imageFile.read()
        attachment = MIMEImage(fileContent)
        attachment.add_header("Content-Disposition", "attachment", filename=("utf-8","","团队合照.png"))
        message.attach(attachment)
        qqMail.sendmail(sender, [receiver], message.as_string())
        print(f"成功发给：{receiver}")
        qqMail.quit()
    except Exception as e:
        error = f"失败发给：{receiver} → {str(e)}"
        print(error) 
        fail_send.append(receiver)
        if "qqMail" in locals():
            try:
                qqMail.quit()  
            except Exception as quit_e:
                print(f"关闭连接时出错：{str(quit_e)}")  
                pass 
send_rounds = 1
def batch_send_to_all():
    global interval_min, interval_max
    for round_num in range(send_rounds):
        print(f"\n开始第 {round_num + 1} 轮发送")
        for num, receiver in enumerate(receivers):
            print(f"\n第 {num + 1} 个收件人")
            send_single_email(receiver)
            if num < len(receivers) - 1:
                interval = random.uniform(interval_min, interval_max)
                print(f"等待{interval:.2f}秒发下一个...")
                time.sleep(interval)
    if fail_send:
        print(f"共{len(fail_send)}人发送失败")
        print(fail_send)
    else:
        print("全部发送成功")
if __name__ == "__main__":
      batch_send_to_all()