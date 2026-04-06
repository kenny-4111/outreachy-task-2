import csv
import requests

def check_urls(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        # Skip header
        next(reader, None)

        for row in reader:
            if not row:
                continue

            url = row[0].strip()

        # Skip empty URLs
            if not url:
                continue

            try:
                response = requests.get(url, timeout=5)
                print(f"({response.status_code}) {url}")
            except requests.exceptions.RequestException:
                print(f"(ERROR) {url}")


if __name__ == "__main__":
    check_urls("Task 2 - Intern.csv")