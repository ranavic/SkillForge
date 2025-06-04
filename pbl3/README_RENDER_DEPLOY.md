# Deploying SkillForge Django on Render

## 1. Prepare Your Repo
- Make sure these files exist in your repo root:
  - `requirements.txt` (must include `gunicorn`, `whitenoise`, `psycopg2-binary`)
  - `Procfile` with:
    ```
    web: gunicorn skillforge.wsgi --log-file -
    ```
  - `skillforge/production_settings.py` with Render/production settings.

## 2. Push to GitHub
- Commit and push all changes to your GitHub repository.

## 3. Set Up on Render
1. Create a new **Web Service** and connect your GitHub repo.
2. Set environment variables:
    - `DJANGO_SETTINGS_MODULE=skillforge.production_settings`
    - `SECRET_KEY=your-very-secret-key`
    - `DATABASE_URL` (Render sets this if you add their PostgreSQL)
3. Build Command:
    ```
    pip install -r requirements.txt
    python manage.py collectstatic --noinput
    python manage.py migrate
    ```
4. Start Command:
    ```
    gunicorn skillforge.wsgi --log-file -
    ```
5. Add a PostgreSQL database in Render and link it to your service.

## 4. After Deploy
- Open a shell on Render and run:
    ```
    python manage.py createsuperuser --settings=skillforge.production_settings
    ```

## 5. Static Files
- WhiteNoise is configured to serve static files.
- Static files are collected to `/staticfiles`.

## 6. Custom Domain
- Add your domain in Render settings. HTTPS is automatic.

---

**You’re ready to deploy!**
