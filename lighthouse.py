import os
from datetime import datetime
from os.path import join

# set the path to this directory
path = os.path.dirname(os.path.abspath(__file__))
reports_path = join(path, "reports")

url = "https://n3xtsports.com"

# for web in ["https://ernestomartinez.dev", "https://www.n3xtsports.com/"]:
#     web_name = web.split("//")[1].split(".")[0]
#     json_filename = join(reports_path, web_name + "_" + getdate + ".report.json")
#     command = f'lighthouse {web} --disable-storage-reset="true" --chrome-flags="--headless --no-sandbox" --emulated-form-factor=desktop --output=json --output-path {json_filename}'
#     stream = os.popen(command)

# for web in ["https://www.n3xtsports.com/", "https://ernestomartinez.dev"]:
#     web_name = web.split("//")[1].split(".")[0]
#     json_filename = join(reports_path, web_name + "_" + getdate + ".report.html")
#     command = f'lighthouse {web} --disable-storage-reset="true" --chrome-flags="--headless --no-sandbox" --emulated-form-factor=desktop --output=html --output-path {json_filename}'
#     stream = os.popen(command)


def get_report(
    url_list,
    report_format="json",
    filename="report",
    device="desktop",
    getdate=datetime.now().strftime("%m-%d-%y"),
):
    for web in url_list:
        web_name = web.split("//")[1].split(".")[0]
        report_name = f"{filename}_{web_name}_{getdate}.report.{report_format}"
        json_filename = join(reports_path, report_name)
        command = f'lighthouse {web} --disable-storage-reset="true" --chrome-flags="--headless --no-sandbox" --emulated-form-factor={device} --output={report_format} --output-path {json_filename}'
        stream = os.popen(command)  # only to create the command on the terminal


get_report(["https://ernestomartinez.dev", "https://www.n3xtsports.com/"])
