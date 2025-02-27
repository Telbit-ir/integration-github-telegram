# GitHub to Telegram Notifier

A Python Flask-based webhook service to send GitHub updates to a Telegram group. This script notifies about **issues**, **merge requests (on master)**, and **deployment status**.

## Features
- ✅ Notify about **issues** with assignee and action.
- ✅ Alert for **merge requests** on the `master` branch.
- ✅ Inform about **deployment status** on `master`.
- ✅ Supports Markdown formatting for better readability in Telegram.

## Prerequisites
Ensure you have the following:

- Python 3.x installed
- A Telegram bot token (via [BotFather](https://t.me/BotFather))
- Your Telegram group chat ID

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/github-telegram-notifier.git
   cd github-telegram-notifier
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install flask requests
   ```

4. Update configuration in `github_to_telegram.py`:

   ```python
   TELEGRAM_BOT_TOKEN = 'your-telegram-bot-token'
   TELEGRAM_CHAT_ID = 'your-chat-id'
   ```

## Running the Webhook

Start the Flask app:

```bash
python github_to_telegram.py
```

By default, it runs on port `5000`. Ensure the server is accessible to GitHub.

## Set Up GitHub Webhook

1. Go to your repository settings: **Settings → Webhooks → Add Webhook**
2. Payload URL: `http://your-server-ip:5000/webhook`
3. Content type: `application/json`
4. Events to trigger:
   - Issues
   - Pull requests (for merge requests)
   - Deployment statuses
5. Click **Add webhook**

## Example Notifications

### Issue Notification
```
📌 Issue opened in owner/repo
👤 By: username
🎯 Assigned to: assignee
📝 Title: Fix user authentication
🔍 View Issue
```

### Merge Request on Master
```
🔀 Merge Request opened on Master in owner/repo
👤 By: username
🎯 Assigned to: reviewer
📝 Title: Add new payment method
🔍 View MR
```

### Deployment Status
```
🚀 Deployment Status Updated on Master
👤 By: username
📊 Status: success
🔍 View Deployment
```

## Deployment
Consider using **ngrok** or a public-facing server for local testing.

1. Run the app:
   ```bash
   python github_to_telegram.py
   ```

2. Expose it via **ngrok**:
   ```bash
   ngrok http 5000
   ```

## Contributing
Feel free to submit issues or pull requests to enhance the notifier.

## License
MIT License

