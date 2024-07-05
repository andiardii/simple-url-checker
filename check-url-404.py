import requests
import sys

def check_url(url):
    try:
        response = requests.head(url, allow_redirects=True)
        if response.status_code == 404:
            return False
        return True
    except requests.RequestException as e:
        print(f"Error checking URL {url}: {e}")
        return False

def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()
    return [url.strip() for url in urls]

def write_urls_to_file(urls, file_path):
    with open(file_path, 'w') as file:
        for url in urls:
            file.write(url + '\n')

def main(file_path):
    urls = read_urls_from_file(file_path)
    not_accessible_urls = []

    for url in urls:
        try:
            if not check_url(url):
                print(f"\033[91m{url} is not accessible (404).\033[0m")
                not_accessible_urls.append(url)
            else:
                print(f"{url} is accessible.")
            
            sys.stdout.flush()
        except Exception as e:
            print(f"Error processing URL {url}: {e}")
            sys.stdout.flush()

    if not_accessible_urls:
        write_urls_to_file(not_accessible_urls, 'not_accessible_urls.txt')
        print(f"Not accessible URLs saved to 'not_accessible_urls.txt'.")
        sys.stdout.flush()

if __name__ == "__main__":
    file_path = 'urls.txt'
    main(file_path)
