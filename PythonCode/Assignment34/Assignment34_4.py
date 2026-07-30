import psutil
import sys
import os
import time
import schedule
import smtplib
from email.message import EmailMessage
import mimetypes

def sendemail(recipient_email,attachment_path):
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587

    SENDER_EMAIL = os.getenv("SENDER_EMAIL", "suryavanshi.s.pravin@gmail.com")
    SENDER_PASSWORD = os.getenv("SENDER_PASSWORD", "vddcjrekgwzvruel")
    msg = EmailMessage()
    msg["Subject"] = "Process email from Automation"
    msg["From"] = SENDER_EMAIL
    msg["To"] = recipient_email
    msg.set_content(f"""Jay Ganesh,
The Process Automation operation has been completed successfully.
Please find the detailed log file attached to this email.
Regards,
Marvellous Automation System
""")

    # Attach file if provided
    if attachment_path:
        if os.path.exists(attachment_path):
            mime_type, _ = mimetypes.guess_type(attachment_path)
            if mime_type:
                maintype, subtype = mime_type.split("/", 1)
            else:
                maintype, subtype = "application", "octet-stream"
            
            with open(attachment_path, "rb") as f:
                msg.add_attachment(
                    f.read(),
                    maintype=maintype,
                    subtype=subtype,
                    filename=os.path.basename(attachment_path),
                )

            print(f"Attached file: {attachment_path}")
        else:
            print(f"Attachment not found: {attachment_path}")

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            print(f"✓ Email successfully sent to {recipient_email}")
    except Exception as e:
        print(f"✗ Failed to send email: {e}")  
        
def ProcessScan():
    listprocess = []

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name","username","status"])
        info["cpu_percent"] = proc.cpu_percent(None)
        info["memory_percent"] = proc.memory_percent()
        if info["status"] == psutil.STATUS_RUNNING:
            listprocess.append(info)

    return listprocess
    
def PlatformSurvillance(FolderName,email):
    Border = "-"*50

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to proceed as directory name is existing but its nota adirectory")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for the logfile gets created succesfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)

    fobj = open(FileName,"w")

    print(f"Log file gets succesfully created with name {FileName}")

    fobj.write(Border+"\n")
    fobj.write("---- Marvellous Platform Survillence System ----\n")
    fobj.write("Log file gets created at : "+timestamp+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("---------------- System Report -----------------\n")

    # Process log
    Data = ProcessScan()

    for info in Data:
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Name : %s\n" %info.get("name"))
        fobj.write("User Name : %s\n" %info.get("username"))
        fobj.write("Status : %s\n" %info.get("status"))
        fobj.write("CPU usage : %.2f\n" %info.get("cpu_percent"))
        fobj.write("RAM usage : %.2f\n" %info.get("memory_percent"))

        fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("--------------- End of Log File ----------------\n")
    fobj.write(Border+"\n")
  
    fobj.close()
    sendemail(email,FileName)

def main():
    Border = "-"*50
    print(Border)
    print("---- Marvellous Platform Survillence System ----")
    print(Border)

    # --h & --u handling
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to perform ")
            print("1 : It fetch the information of running processess")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as : ")
            print(f"python {sys.argv[0]} Email Folder_Name")
            print("Email : ")
            print("Folder_Name : Name of folder for the log file creation")
            
        else:
            print("Unable to proceed as there is no matching argument")
            print("Please use --h or --u flag for getting more details")

    # Actual project code
    elif(len(sys.argv) == 3):

        print("Schedular started succesfully")
        print("Press Ctrl + C to abort the automation script")
        
        schedule.every(1).minutes.do(PlatformSurvillance,sys.argv[2],sys.argv[1])

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of argumenst")
        print("Unable to proceed as arguments are not matching")
        print("Please use --h or --u flag for getting more details")

    print(Border)
    print("--- Thank you for using our automation System ---")
    print(Border)

if __name__ == "__main__":
    main()