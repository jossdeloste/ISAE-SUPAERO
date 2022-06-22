import pandas as pd

base = "gcloud projects add-iam-policy-binding obd-2021-2022 --member='user:{}' --role='roles/editor'\n"

df = pd.read_csv("gmails.csv")

with open("cmd.sh", "w") as f:
    for _, r in df.iterrows():
        email = str(r.get("mails"))

        cmd = base.format(email)
        f.write(cmd)

