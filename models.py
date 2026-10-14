from database import get_db_connection

def create_tables():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS job_applications (
            id INT AUTO_INCREMENT PRIMARY KEY,
            company_name VARCHAR(100) NOT NULL,
            job_title VARCHAR(100) NOT NULL,
            job_description TEXT NOT NULL,
            match_score FLOAT DEFAULT 0.0,
            status VARCHAR(50) DEFAULT 'Pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    print("Table created successfully!")
    
    cursor.close()
    connection.close()

if __name__ == "__main__":
    create_tables()
