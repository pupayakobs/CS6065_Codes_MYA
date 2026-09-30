import os
import socket
import re
from collections import Counter

def process_text_files():
    data_dir = "/home/data"
    output_dir = os.path.join(data_dir, "output")
    
    file1_path = os.path.join(data_dir, "IF.txt")
    file2_path = os.path.join(data_dir, "AlwaysRememberUsThisWay.txt")
    result_path = os.path.join(output_dir, "result.txt")
    
    # --- Objective 4.a: Count total words in IF.txt ---
    with open(file1_path, 'r', encoding='utf-8') as f:
        file1_text = f.read()
    # Regular word match (treating words with standard splitting)
    file1_words = re.findall(r"\b\w+\b", file1_text.lower())
    file1_count = len(file1_words)
    
    # --- Objective 4.a & 4.d: Count words and handle contractions for AlwaysRememberUsThisWay.txt ---
    with open(file2_path, 'r', encoding='utf-8') as f:
        file2_text = f.read()
    
    # Standardize apostrophes first (handles smart quotes vs regular quotes)
    cleaned_text2 = file2_text.replace("’", "'").lower()
    
    # Replace the apostrophe with a space to split contractions (e.g., "don't" becomes "don t")
    split_contraction_text2 = re.sub(r"'", " ", cleaned_text2)
    
    # Extract all individual words
    file2_words = re.findall(r"\b\w+\b", split_contraction_text2)
    file2_count = len(file2_words)
    
    # --- Objective 4.b: Calculate Grand Total ---
    grand_total = file1_count + file2_count
    
    # --- Objective 4.c: Top 3 most frequent words in IF.txt ---
    file1_top3 = Counter(file1_words).most_common(3)
    
    # --- Objective 4.d: Top 3 most frequent words in AlwaysRememberUsThisWay.txt ---
    file2_top3 = Counter(file2_words).most_common(3)
    
    # --- Objective 4.e: Determine Container IP Address ---
    ip_address = socket.gethostbyname(socket.gethostname())
    
    # Format the final output lines exactly as expected
    output_lines = [
        f"Total words in IF.txt: {file1_count}",
        f"Total words in AlwaysRememberUsThisWay.txt (contractions split): {file2_count}",
        f"Grand total of words across both files: {grand_total}",
        f"Top 3 most frequent words in IF.txt: {file1_top3}",
        f"Top 3 most frequent words in AlwaysRememberUsThisWay.txt: {file2_top3}",
        f"Container IP Address: {ip_address}"
    ]
    
    final_output = "\n".join(output_lines)
    
    # --- Objective 4.f: Write to result.txt ---
    os.makedirs(output_dir, exist_ok=True)
    with open(result_path, 'w', encoding='utf-8') as out_f:
        out_f.write(final_output)
        
    # --- Objective 4.f: Print contents of result.txt to console before exiting ---
    print(final_output)

if __name__ == "__main__":
    process_text_files()
