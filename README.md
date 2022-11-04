# Django-Object-Actions test

## Installation

- `git clone https://github.com/nshafer/oatest`
- `cd oatest`
- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py runserver`

## Recreating issue

- Go to http://localhost:8000/admin/
- Login with username `admin` and password `admin`
- Click on "Articles" in the sidebar
- Click on "normalkey" for the "First Article with Normal Key".
  - It renders and you can click on "Publish This"
- Click on "key_with_underscores" for the "Second Article with Underscores".
  - You get a DoesNotExist error: "Article matching query does not exist"
  - In the runserver log you can see that the article_id, as passed to `get_change_actions` is
    "key_5Fwith_5Funderscores" instead of "key_with_underscores"
  - You can "fix" it in `core/admin.py` by uncommenting the call to `unquote` on line 17.
