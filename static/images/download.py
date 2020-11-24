import time
import webbrowser
import pandas as pd
import itertools


def splitIssueKey(str):
    newString = str.rsplit('FSUPPORT-')[1]
    return newString


def getAttachments():
    df_raw = pd.read_csv('total_resolved.csv', mangle_dupe_cols=True)

    df_att = df_raw.filter(regex='Attachment*')
    # df_issue = df_raw.filter(regex='Issue key')
    # df_con = pd.concat([df_att, df_issue], axis=1)

    # print(df_con)
    # print(df_att)
    # # test = []
    df_list = df_att.values.tolist()
    strArr = []
    for list in df_list:
        for item in list:
            if(isinstance(item, str)):
                strArr.append(item)

    total = []
    for item in strArr:
        total.append(item.split(';'))

    pngs = []
    for items in total:
        for item in items:
            if ('http' in item and 'png' in item and '2020' in item):
                pngs.append(item)
                # print(pngs)

    # print(pngs)
    return pngs


pics2020 = getAttachments()

print(len(pics2020))

# for x in range(0, len(pics2020)):
#     webbrowser.open_new_tab(pics2020[x])
