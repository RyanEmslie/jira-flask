import pandas as pd
import json


def splitIssueKey(str):
    newString = str.rsplit('FSUPPORT-')[1]
    return newString

def all_tickets():
    # Create dataframe from csv and rename duplicate columns
    df_raw = pd.read_csv('total_resolved.csv', mangle_dupe_cols=True)
    for index, value in enumerate(df_raw['Issue key']):
        df_raw.at[index,'Key'] =splitIssueKey(value)
    df = df_raw[['Issue key','Summary','Key']]
    df['Key'] = df['Key'].astype(int)
    df.sort_values('Key', ascending=False, inplace=True)
    df['Key'] = df['Key'].astype(str)
    dff = df.to_numpy().tolist()
    return dff


def text_search(text):
    df = pd.read_csv('total_resolved.csv', mangle_dupe_cols=True)
    df['Found'] = df.apply(lambda row: row.astype(str).str.contains(text).any(), axis=1)
    # print(df)
    df_raw = df[df['Found'] == True]
    df_raw.reset_index(drop=True, inplace=True)
    # print(df_raw)
    for index, value in enumerate(df_raw['Issue key']):
        df_raw.at[index,'Key'] =splitIssueKey(value)
    dff = df_raw[['Issue key','Summary','Key','Found']]
    dff['Key'] = dff['Key'].astype(int)
    dff.sort_values('Key', ascending=False, inplace=True)
    dff['Key'] = dff['Key'].astype(str)
    dfff = dff.to_numpy().tolist()
    return dfff


def number_search(num):
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
    description = df_record.at[0, 'Description']
    
    
    if ('Custom field (Account ID)' in df_record):
        account_id = df_record.at[0, 'Custom field (Account ID)']
    else:
        account_id = 'Not Provided'
    assignee = df_record.at[0, 'Assignee']
    reporter = df_record.at[0, 'Reporter']
   
    comments = df_record.filter(regex='Comment*', axis=1)
    commentsArr = []
    for x in comments:
        commentsArr.append(comments.at[0,x])
    # results = {
    #     'reporter': reporter,
    #     'assignee': assignee,
    #     'account_id': account_id,
    #     'summary': summary,
    #     'description':description,
    #     'commentsArr':commentsArr
    # }
    results = [reporter, assignee, account_id, summary, description, commentsArr]
    return results
    # return list(reporter, assignee, account_id, summary, description, commentsArr)

