# Simple URL Checker

This program is based on my need to handle 8k URLs, which cannot be checked individually. I have automated a script to change my permalink URLs if errors occur. Sometimes, the automation script fails to work correctly and does not successfully change the permalink URLs. Therefore, I built this program to check it.

It has two main features:
1. Checking if URLs redirect to the homepage or not, error results logged in 'not_accessible_urls.txt'.
2. Checking if URLs can be accessed or return a 404 error, error results logged in 'redirected_urls.txt'.

All error results will be logged in both notepad files and displayed in the command prompt.
Successful results will only be displayed in the command prompt."

If you need further adjustments or additional information, feel free to ask!

### Installation

**Step 1:** Clone this repository.

```bash
git clone https://github.com/andiardii/simple-url-checker.git
```

**Step 2:** Install module requests (if not have).

```bash
pip install requests
```

**Step 3:** Input all of your urls that you want to check in urls.txt file

**Step 4:** Run command

```bash
python check-url-homepage.py
```

or

```bash
python check-url-404.py
```