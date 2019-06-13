from httprunner.api import HttpRunner
import send_email
import os


if __name__ == '__main__':
    report_dir = "/Users/apple/api_test/reports"
    before_files = os.listdir(report_dir)
    before_files = os.listdir(report_dir)
    print(before_files)

    runner = HttpRunner(failfast=False, report_dir=report_dir)
    runner.run("/Users/apple/api_test/testcases")
    summary = runner.summary
    print(summary)


    after_files = os.listdir(report_dir)
    print(after_files)
    file_path =""
    for dir in before_files:
       if dir in after_files:
           after_files.remove(dir)
    if len(after_files)==1:
        file_path = report_dir + "/" + after_files[0]
        print(file_path)
        if  send_email.send_Mail(file_path, "用例执行完成") is True:
            print("发送邮件成功")
        else:
            print("发送邮件失败")





