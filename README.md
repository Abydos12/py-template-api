# Deploy

if `pip` not installed

    sudo apt install pip

dependencies

    pip install -r requirements.txt

launch the app (into the project directory)

    uvicorn src.app:app --host 0.0.0.0 --port 5000

## TIP

add the aws address to list of API server in `src/app.py`

Example

    app = FastAPI(
        title="py-template-api",
        servers=[
            {"url": "http://localhost:5000", "description": "DEV"}
            {"url": "http://ip_aws:port_aws", "description": "AWS"}
        ],
    )
