import requests
import sys

def get_final_url(url):
    try:
        response = requests.get(url, allow_redirects=True)
        response.raise_for_status()
        return response.url
    except requests.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None

def is_redirect_to_homepage(url):
    homepage_url = '/'.join(url.split('/')[:3])
    final_url = get_final_url(url)
    
    if final_url:
        return final_url == homepage_url
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
    redirected_urls = []

    for url in urls:
        try:
            if is_redirect_to_homepage(url):
                print(f"\033[91m{url} redirects to the homepage.\033[0m")
                redirected_urls.append(url)
            else:
                print(f"{url} opens as expected.")
            
            sys.stdout.flush()
        except Exception as e:
            print(f"Error processing URL {url}: {e}")
            sys.stdout.flush()

    if redirected_urls:
        write_urls_to_file(redirected_urls, 'redirected_urls.txt')
        print(f"Redirected URLs saved to 'redirected_urls.txt'.")
        sys.stdout.flush()

if __name__ == "__main__":
    file_path = 'urls.txt'
    main(file_path)
