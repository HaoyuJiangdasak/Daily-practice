import smtplib
import time
import random
from email.mime.text import MIMEText
from email.header import Header
mail_user = "3635229037@qq.com"
mail_pass = "yggserlpxpuucjdd"  
sender = mail_user
receivers= ["3875895759@qq.com","2908372264@qq.com","1961383783@qq.com","940283567@qq.com"]
textContext = ["别往后看，有鬼","真别看，后果很严重","一只，两只，三只......","终于结束了，这场闹剧"]
sendtimes = len(textContext)
intervsal_min = 60
intervsal_max = 90
def send_simple_email(text_content):
    qq_mail = None
    try:
        qq_mail = smtplib.SMTP_SSL("smtp.qq.com", 465, timeout=20)
        qq_mail.ehlo()
        qq_mail.login(mail_user, mail_pass)
        print("登录成功")
        print(f"准备给{len(receivers)}个人发邮件")
        message = MIMEText(text_content, "plain", "utf-8")
        message["Subject"] = Header(f"{random.randint(100,999)}", "utf-8")  
        message["From"] = Header(sender)
        message["To"] = Header(",".join(receivers))
        qq_mail.sendmail(sender, receivers, message.as_string())
        print(f"邮件发送成功！本次内容：{text_content}")
    except smtplib.SMTPAuthenticationError:
        print("授权码无效！")
    except smtplib.SMTPConnectError:
        print("连接被服务器拒绝！")
    except smtplib.SMTPDataError as e:
        print(f"收件人/内容被拦截 → {e}")
    except Exception as e:
        print(f"{str(e)}")
    finally:
        if qq_mail:
            try:
                qq_mail.quit()
            except:
                qq_mail.close()
def batch_send():
    print(f"开始分批发送，共发送{sendtimes}次，间隔{intervsal_min}~{intervsal_max}秒")
    for i in range(sendtimes):
        if i < len(textContext):
            current_text = textContext[i]
        else:
            current_text = textContext[-1]  
        send_simple_email(current_text)
        if i < sendtimes - 1:
            interval = random.uniform(intervsal_min, intervsal_max)
            print(f"等待{interval:.0f}秒后发送下一封...\n")
            time.sleep(interval)
    print("所有邮件发送完成!")
if __name__ == "__main__":
    batch_send()
