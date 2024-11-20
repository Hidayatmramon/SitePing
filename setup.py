import requests

input_file = "data.txt"
output_file = "reachable.txt"

with open(input_file, "r") as file:
    urls = [line.strip() for line in file.readlines()]

reachable_urls = []

for url in urls:
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url  
    try:
        response = requests.get(url, timeout=5)
        if response.ok:
            print(f"[SUCCESS] {url} is reachable!")
            reachable_urls.append(url)
        else:
            print(f"[ERROR] {url} returned status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[FAIL] {url}")

if reachable_urls:
    with open(output_file, "w") as file:
        file.writelines(f"{url}\n" for url in reachable_urls)
    print(f"\nReachable URLs saved to {output_file}")
else:
    print("\nNo reachable URLs found.")
