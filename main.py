import re
import json
import csv
from bs4 import BeautifulSoup

def read_file(filepath):
    """Faylı oxuyur və məzmununu qaytarır."""
    with open(filepath, 'r') as file:
        return file.readlines()

def write_to_file(filepath, content):
    """Məlumatları fayla yazır."""
    with open(filepath, 'w') as file:
        file.write(content)

def extract_url_status(log_data):
    """Log məlumatlarından URL-ləri və status kodlarını çıxarır."""
    url_status = []
    url_count_404 = {}
    for line in log_data:
        match = re.search(r'"(GET|POST) (\S+) HTTP/1.1" (\d+)', line)
        if match:
            url = match.group(2)
            status = match.group(3)
            url_status.append((url, status))
            if status == "404":
                url_count_404[url] = url_count_404.get(url, 0) + 1
    return url_status, url_count_404

def save_url_status_report(url_status):
    """Bütün URL-ləri və status kodlarını faylda saxlayır."""
    content = "\n".join([f"URL: {url} | Status: {status}" for url, status in url_status])
    write_to_file('url_status_report.txt', content)

def save_404_urls_to_csv(url_count_404):
    """404 status kodlu URL-ləri CSV faylında saxlayır."""
    with open('malware_candidates.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["URL", "404 Count"])
        for url, count in url_count_404.items():
            writer.writerow([url, count])

def parse_blacklisted_domains(txt_file):
    """Mətn faylından qara siyahıya alınmış domenləri çıxarır."""
    with open(txt_file, 'r') as file:
        return {line.strip() for line in file.readlines()}

def save_alert_data(url_status, blacklisted_domains):
    """Qara siyahıya uyğun URL-ləri JSON faylında saxlayır."""
    matching_urls = [url for url, _ in url_status if any(domain in url for domain in blacklisted_domains)]
    alert_data = [{"url": url, "status": status} for url, status in url_status if url in matching_urls]
    with open('alert.json', 'w') as file:
        json.dump(alert_data, file, indent=4)
    return matching_urls

def save_summary_report(url_status, url_count_404, matching_urls):
    """Xülasə hesabatını JSON faylında saxlayır."""
    summary_data = {
        "all_urls_with_status": [{"url": url, "status": status} for url, status in url_status],
        "urls_404_with_counts": [{"url": url, "count": count} for url, count in url_count_404.items()],
        "blacklisted_matching_urls": [{"url": url, "status": status} for url, status in url_status if url in matching_urls]
    }
    with open('summary_report.json', 'w') as file:
        json.dump(summary_data, file, indent=4)

def transfer_and_clear_html(html_file, txt_file):
    """HTML məlumatlarını mətn faylına köçürür və HTML faylını təmizləyir."""
    with open(html_file, 'r+') as file:
        soup = BeautifulSoup(file, 'html.parser')
        blacklisted_domains = "\n".join([li.text for li in soup.find_all('li')])
        write_to_file(txt_file, blacklisted_domains)
        file.truncate(0)
    return blacklisted_domains

# Əsas proqram axını
transfer_and_clear_html('threat_feed.html', 'threat_feed.txt')

log_data = read_file('access_log.txt')
url_status, url_count_404 = extract_url_status(log_data)
save_url_status_report(url_status)
save_404_urls_to_csv(url_count_404)

blacklisted_domains = parse_blacklisted_domains('threat_feed.txt')
matching_urls = save_alert_data(url_status, blacklisted_domains)
save_summary_report(url_status, url_count_404, matching_urls)
