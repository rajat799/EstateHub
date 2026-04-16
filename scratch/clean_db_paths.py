import sqlite3

def clean_database_paths():
    try:
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        print("Cleaning app_properties...")
        cursor.execute("UPDATE app_properties SET pr_image = REPLACE(pr_image, 'app/static/media/', '') WHERE pr_image LIKE 'app/static/media/%'")
        cursor.execute("UPDATE app_properties SET pr_image1 = REPLACE(pr_image1, 'app/static/media/', '') WHERE pr_image1 LIKE 'app/static/media/%'")
        
        print("Cleaning app_products...")
        cursor.execute("UPDATE app_products SET pd_image = REPLACE(pd_image, 'app/static/media/', '') WHERE pd_image LIKE 'app/static/media/%'")

        conn.commit()
        print(f"Success! {cursor.rowcount} records updated in the last operation.")
        conn.close()
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    clean_database_paths()
