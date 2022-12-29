import os
from fastapi.testclient import TestClient
import pytest
from main import create_app, DATABASE_URL



@pytest.fixture(scope="session", autouse=True)
def create_database_and_run_migrations():
    """Run migrations for test database"""
    print("Running migrations...")
    os.system(f"yoyo apply --database {DATABASE_URL} ./migrations -b")

@pytest.fixture(scope="session")
def test_client():
    """Test client creation"""
    with TestClient(create_app()) as client:
        yield client


@pytest.fixture(scope="function", autouse=True)
def clean_tables(test_client):
    """Clean data in all tables before running test function"""
    cursor = test_client.app.state.db.cursor()
    cursor.execute("""TRUNCATE TABLE users;""")
    test_client.app.state.db.commit()
