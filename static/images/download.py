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
                print(pngs)

    print(pngs)


getAttachments()

# urls = ['https://feathr.atlassian.net/secure/attachment/19862/Screen+Shot+2020-07-13+at+3.51.46+PM.png',
#         'https://feathr.atlassian.net/secure/attachment/19867/Screen+Shot+2020-07-14+at+1.41.29+PM.png', 'https://feathr.atlassian.net/secure/attachment/19816/Screen+Shot+2020-07-07+at+4.36.27+PM.png']

# for url in urls:
#     webbrowser.open_new_tab(url)
