import pandas as pd


# def createAttachments():
#     frames = df_record.filter(regex='Attachment').to_string()
#     splitString = frames.split(';')
#     newArr = []
#     for string in splitString:
#         if 'http' in string:
#             new_string = string.split('  ')[0].strip()
#             newArr.append(new_string)
#     return newArr


def splitIssueKey(str):
    newString = str.rsplit('FSUPPORT-')[1]
    return newString


def record_search(num):
    # Create dataframe from csv and rename duplicate columns
    df_raw = pd.read_csv('total_resolved.csv', mangle_dupe_cols=True)

    # add column 'Key' by splitting 'Issue key'
    for index, value in enumerate(df_raw['Issue key']):
        df_raw.at[index,'Key'] =splitIssueKey(value)
    job_number = num
    df_record_raw = df_raw.loc[df_raw['Key']==job_number]

    df_record = df_record_raw.dropna(axis='columns')
    df_record.reset_index(drop=True, inplace=True)
    summary = df_record.at[0, 'Summary']
    print(summary)
    description = df_record.at[0, 'Description']
    # print(description)
    account_id = df_record.at[0, 'Custom field (Account ID)']
    # print(account_id)
    assignee = df_record.at[0, 'Assignee']
    # print(assignee)
    reporter = df_record.at[0, 'Reporter']
    # print(reporter)
    creator = df_record.at[0, 'Creator']
    # print(creator)
    customer_account = df_record.at[0, 'Custom field (Customer Account)']
    # print(customer_account)
    # attachments = createAttachments()
    # print(attachments)
    results = {
        'reporter': reporter,
        'assignee': assignee,
        'account_id': account_id,
        'summary': summary
    }
    return results
