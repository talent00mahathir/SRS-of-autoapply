from database import get_db_connection

def create_tables():
    with get_db_connection() as connection:
        cursor = connection.cursor()

        # 1. Job Postings Table (Agent 1 er jonno)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS job_postings (
                id INT AUTO_INCREMENT PRIMARY KEY,
                job_title VARCHAR(150) NOT NULL,
                company_name VARCHAR(100) NOT NULL,
                raw_description TEXT NOT NULL,
                extracted_skills TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # 2. Resumes Table (Agent 2 er jonno)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS resumes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                file_name VARCHAR(255) NOT NULL,
                parsed_text TEXT NOT NULL,
                extracted_skills TEXT,
                uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # 3. Agent Results Table (Agent 3 & 4 er match score, missing skills & cover letter rakhar jonno)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS agent_results (
                id INT AUTO_INCREMENT PRIMARY KEY,
                job_id INT,
                resume_id INT,
                match_score FLOAT DEFAULT 0.0,
                missing_skills TEXT,
                tailored_bullets TEXT,
                cover_letter TEXT,
                generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (job_id) REFERENCES job_postings(id),
                FOREIGN KEY (resume_id) REFERENCES resumes(id)
            )
        """)

        # 4. Job Applications Tracker Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS job_applications (
                id INT AUTO_INCREMENT PRIMARY KEY,
                result_id INT,
                status VARCHAR(50) DEFAULT 'Pending',
                applied_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (result_id) REFERENCES agent_results(id)
            )
        """)

        connection.commit()
        cursor.close()
        print("All advanced tables created successfully!")

if __name__ == "__main__":
    create_tables()
