import os
import sqlite3

def cleanup_media_folder():
    db_path = 'db.sqlite3'
    media_dir = os.path.join('app', 'static', 'media', 'property')
    
    if not os.path.exists(db_path):
        print("Database not found!")
        return

    # 1. Get all unique image paths from the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    active_paths = set()
    
    # Check properties
    cursor.execute("SELECT pr_image, pr_image1 FROM app_properties")
    for row in cursor.fetchall():
        if row[0]: active_paths.add(os.path.basename(row[0]))
        if row[1]: active_paths.add(os.path.basename(row[1]))
        
    # Check products
    cursor.execute("SELECT pd_image FROM app_products")
    for row in cursor.fetchall():
        if row[0]: active_paths.add(os.path.basename(row[0]))
        
    conn.close()
    
    print(f"Active files found in DB: {active_paths}")

    # 2. Iterate through the media folder
    if not os.path.exists(media_dir):
        print(f"Media directory {media_dir} not found!")
        return

    deleted_count = 0
    kept_count = 0
    
    for filename in os.listdir(media_dir):
        file_path = os.path.join(media_dir, filename)
        
        # Only process files, not directories
        if os.path.isfile(file_path):
            if filename in active_paths:
                print(f"KEEPING: {filename}")
                kept_count += 1
            else:
                print(f"DELETING: {filename}")
                os.remove(file_path)
                deleted_count += 1
                
    print(f"\nCleanup finished!")
    print(f"Total files DELETED: {deleted_count}")
    print(f"Total files KEPT: {kept_count}")

if __name__ == "__main__":
    cleanup_media_folder()
