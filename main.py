from flask import Flask, redirect, url_for, render_template, request, session, flash, Markup, escape
from datetime import timedelta
from search_number import number_search, all_tickets, text_search, getAttachments
import re

app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route('/attachments')
def attachments():
    attachments = getAttachments()
    name = []
    for item in attachments:
        name.append(item.split('/')[6].replace('+', ' '))
        # name.append(item.split('/')[6].split('.')[0].replace('+', ' '))

    def merge(list1, list2):
        merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
        merged_list.sort(reverse=True)
        print(len(merged_list))
        return merged_list
    merged = merge(name, attachments)
    link = '/static/images/screenshots/'
    print(merged)
    return render_template('display_attachments.html', merged=merged, link=link)


@app.route('/search', methods=['POST', 'GET'])
def search_number():
    if request.method == 'POST':
        num = request.form['key']
        return redirect(url_for('num_key', num=num))
    else:
        return render_template('search.html')


@app.route('/')
@app.route('/tickets', methods=['POST', 'GET'])
def search_text():
    if request.method == 'POST':
        text = request.form['text_string']
        tickets = text_search(text)
        num_tickets = len(tickets)
        return render_template('display_tickets.html', tickets=tickets, num_tickets=num_tickets)
    else:
        tickets = all_tickets()
        num_tickets = len(tickets)
        return render_template('display_tickets.html', tickets=tickets, num_tickets=num_tickets)


@app.route('/ticket/<num>', methods=['POST', 'GET'])
def num_key(num):
    if request.method == 'POST':
        num = request.form['key']
        search_data = number_search(num)
        assignee = search_data[0]
        reporter = search_data[1]
        account_id = search_data[2]
        summary = search_data[3]
        description = search_data[4]
        commentsArr = search_data[5]
        imageList = replaceImgText(commentsArr)

        return redirect(url_for('num_key', num=num, imageList=imageList))
    else:
        search_data = number_search(num)
        assignee = search_data[0]
        reporter = search_data[1]
        account_id = search_data[2]
        summary = search_data[3]
        description = search_data[4]
        commentsArr = search_data[5]
        imageList = replaceImgText(commentsArr)
    return render_template('display_number.html', assignee=assignee, reporter=reporter, account_id=account_id, summary=summary, description=description, commentsArr=commentsArr, num=num, imageList=imageList)


def replaceImgText(comments):
    attachments = getAttachments()
    pic_names = []
    for item in attachments:
        pic_names.append(item.split('/')[6].replace('+', ' '))

    pics_on_page = []

    for pic_name in pic_names:
        for comment in comments:
            found = comment.find(pic_name)
            if found > 1:
                pics_on_page.append(pic_name)
    return pics_on_page


if __name__ == "__main__":
    app.run(debug=True)
