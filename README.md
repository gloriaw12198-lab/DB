# Movie Streaming Catalog

A Django app with two related tables:
- Director
- Movie

## Database diagram

```mermaid
erDiagram
    DIRECTOR ||--o{ MOVIE : directs
    DIRECTOR {
        int id PK
        string name
        string nationality
        int birth_year
    }
    MOVIE {
        int id PK
        string title
        string genre
        int release_year
        string streaming_service
        int director_id FK
    }
```

## Run locally

```bash
cd /home/wahome/Glo/db
. .venv/bin/activate
python manage.py runserver 0.0.0.0:8080
```

Open http://127.0.0.1:8080/catalog/
