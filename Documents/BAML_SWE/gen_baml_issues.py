import requests
from bs4 import BeautifulSoup
import yaml
import os

GITHUB_ISSUES_URL = "https://github.com/boundaryml/baml/issues"
OUTPUT_FILE = "instances/baml/instances.baml_test.yaml"
MAX_ISSUES = 10

headers = {
    "User-Agent": "Mozilla/5.0"
}

#scrape first oens
def scrape_github_issues():
    print(f"Scraping first {MAX_ISSUES} issues from {GITHUB_ISSUES_URL}")
    response = requests.get(GITHUB_ISSUES_URL, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    issue_links = soup.select('a.Link--primary.v-align-middle.no-underline.h4.js-navigation-open.markdown-title')

    issues = []

    for i, link in enumerate(issue_links[:MAX_ISSUES]):
        href = link.get("href")
        issue_url = f"https://github.com{href}"
        issue_number = href.split("/")[-1]
        print(f"Fetching issue #{issue_number}: {issue_url}")
        issue_data = fetch_single_issue(issue_url, issue_number)
        if issue_data:
            issues.append(issue_data)

    return issues

#get issue one onkly one
def fetch_single_issue(url, issue_number):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    title_tag = soup.select_one("span.js-issue-title")
    body_tag = soup.select_one("td.comment-body")

    if not title_tag or not body_tag:
        print(f"Skipping issue #{issue_number} — content missing")
        return None

    title = title_tag.text.strip()
    body = body_tag.text.strip()

    return {
        "id": f"baml_issue_{issue_number}",
        "problem_statement": f"{title}\n\n{body}",
        "env": {
            "deployment": {
                "type": "docker",
                "image": "python:3.11"
            }
        }
    }
#write to file
def write_to_yaml(issues):
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        yaml.dump(issues, f, sort_keys=False)
    print(f"\n Saved {len(issues)} issues to {OUTPUT_FILE}")

if __name__ == "__main__":
    issues = scrape_github_issues()
    write_to_yaml(issues)
