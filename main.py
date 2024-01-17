import requests
import re
from jinja2 import Environment, FileSystemLoader

# Prepare Jinja template env
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("changelog.html")

commit_types = {
    "feat": "Features",
    "fix": "Bug Fixes",
    "docs": "Documentation",
    "refactor": "Code Refactoring",
    "test": "Tests",
    "build": "Build System",
    "ci": "Continuous Integration",
}

repo_owner = 'angular'
repo_name = 'angular'


def get_commits_from_github_api(repo_owner, repo_name):
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/commits'
    response = requests.get(url)
    commits = response.json()
    return commits


def group_commits_by_convention(commits):
    grouped_commits = {}
    for commit in commits:
        try:
            message = commit['commit']['message']
            commit_type = re.match(r"^(\w+)(?:\(.+\))?:", message)
            if commit_type:
                commit_type = commit_type.group(1).lower()
                section_header = commit_types.get(commit_type, "Other Changes")
                grouped_commits.setdefault(section_header, []).append(commit)
        except Exception as e:
            print(e)

    return grouped_commits


commits = get_commits_from_github_api(repo_owner, repo_name)
grouped_commits = group_commits_by_convention(commits)


# Render the template
rendered_content = template.render(
    grouped_commits=grouped_commits,
    repo_name=repo_name,
    version="2.4.0" # Version Name from Image
)

# Save the rendered HTML to a file
with open("index.html", "w") as file:
    file.write(rendered_content)