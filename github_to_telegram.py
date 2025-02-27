import requests
import json
from flask import Flask, request

app = Flask(__name__)

# Configuration
TELEGRAM_BOT_TOKEN = 'your-telegram-bot-token'
TELEGRAM_CHAT_ID = 'your-chat-id'
telegram_api_url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'

def send_telegram_message(message):
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    requests.post(telegram_api_url, json=payload)

@app.route('/webhook', methods=['POST'])
def github_webhook():
    payload = request.json
    event_type = request.headers.get('X-GitHub-Event')

    if event_type == 'issues':
        action = payload['action']
        issue = payload['issue']
        user = payload['sender']['login']
        assignee = issue.get('assignee', {}).get('login', 'Unassigned')

        message = (f"📌 *Issue {action} in {payload['repository']['full_name']}*\n"
                   f"👤 *By:* {user}\n"
                   f"🎯 *Assigned to:* {assignee}\n"
                   f"📝 *Title:* {issue['title']}\n"
                   f"🔍 [View Issue]({issue['html_url']})")
        send_telegram_message(message)

    elif event_type == 'merge_request' or event_type == 'pull_request':
        action = payload['action']
        pr = payload.get('pull_request', payload.get('merge_request'))
        user = payload['sender']['login']
        assignee = pr.get('assignee', {}).get('login', 'Unassigned')

        if pr['base']['ref'] == 'master':
            message = (f"🔀 *Merge Request {action} on Master in {payload['repository']['full_name']}*\n"
                       f"👤 *By:* {user}\n"
                       f"🎯 *Assigned to:* {assignee}\n"
                       f"📝 *Title:* {pr['title']}\n"
                       f"🔍 [View MR]({pr['html_url']})")
            send_telegram_message(message)

    elif event_type == 'deployment_status':
        deployment = payload['deployment_status']
        user = payload['sender']['login']

        if payload['deployment']['ref'] == 'master':
            message = (f"🚀 *Deployment Status Updated on Master*\n"
                       f"👤 *By:* {user}\n"
                       f"📊 *Status:* {deployment['state']}\n"
                       f"🔍 [View Deployment]({deployment['target_url']})")
            send_telegram_message(message)

    return 'OK', 200

if __name__ == '__main__':
    app.run(port=5000)
import requests
import json
from flask import Flask, request

app = Flask(__name__)

# Configuration
TELEGRAM_BOT_TOKEN = 'your-telegram-bot-token'
TELEGRAM_CHAT_ID = 'your-chat-id'
telegram_api_url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'

def send_telegram_message(message):
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    requests.post(telegram_api_url, json=payload)

@app.route('/webhook', methods=['POST'])
def github_webhook():
    payload = request.json
    event_type = request.headers.get('X-GitHub-Event')

    if event_type == 'issues':
        action = payload['action']
        issue = payload['issue']
        user = payload['sender']['login']
        assignee = issue.get('assignee', {}).get('login', 'Unassigned')

        message = (f"📌 *Issue {action} in {payload['repository']['full_name']}*\n"
                   f"👤 *By:* {user}\n"
                   f"🎯 *Assigned to:* {assignee}\n"
                   f"📝 *Title:* {issue['title']}\n"
                   f"🔍 [View Issue]({issue['html_url']})")
        send_telegram_message(message)

    elif event_type == 'pull_request':
        action = payload['action']
        pr = payload['pull_request']
        user = payload['sender']['login']
        assignee = pr.get('assignee', {}).get('login', 'Unassigned')

        if pr['base']['ref'] == 'master':
            message = (f"🔀 *Merge Request {action} on Master in {payload['repository']['full_name']}*\n"
                       f"👤 *By:* {user}\n"
                       f"🎯 *Assigned to:* {assignee}\n"
                       f"📝 *Title:* {pr['title']}\n"
                       f"🔍 [View MR]({pr['html_url']})")
            send_telegram_message(message)

    elif event_type == 'deployment_status':
        deployment = payload['deployment_status']
        user = payload['sender']['login']

        if payload['deployment']['ref'] == 'master':
            message = (f"🚀 *Deployment Status Updated on Master*\n"
                       f"👤 *By:* {user}\n"
                       f"📊 *Status:* {deployment['state']}\n"
                       f"🔍 [View Deployment]({deployment['target_url']})")
            send_telegram_message(message)

    return 'OK', 200

if __name__ == '__main__':
    app.run(port=5000)