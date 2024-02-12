import subprocess
from collections import defaultdict

def get_commit_log():
    """
    Retrieve commit log using Git command.
    """
    command = ['git', 'log', '--pretty=format:%s']
    result = subprocess.run(command, stdout=subprocess.PIPE)
    commit_log = result.stdout.decode().split('\n')
    return commit_log

def categorize_commits(commit_log):
    """
    Categorize commits into different types (e.g., features, bug fixes).
    """
    categorized_commits = defaultdict(list)
    for commit in commit_log:
        if commit.startswith('feat:'):
            categorized_commits['Features'].append(commit)
        elif commit.startswith('fix:'):
            categorized_commits['Bug Fixes'].append(commit)
        # Add more categories as needed (e.g., docs, refactor, etc.)
        # Example: elif commit.startswith('docs:'):
        #             categorized_commits['Documentation'].append(commit)
        else:
            categorized_commits['Other'].append(commit)
    return categorized_commits

def generate_changelog(categorized_commits):
    """
    Generate a formatted changelog from categorized commits.
    """
    changelog = ""
    for category, commits in categorized_commits.items():
        changelog += f"## {category}\n"
        for commit in commits:
            changelog += f"- {commit}\n"
        changelog += "\n"
    return changelog

def main():
    commit_log = get_commit_log()
    categorized_commits = categorize_commits(commit_log)
    changelog = generate_changelog(categorized_commits)
    # Write changelog to file or print to console
    # Example: print(changelog)
    # You can also write it to a file like this:
    with open('CHANGELOG.rst', 'w') as f:
        f.write(changelog)

if __name__ == "__main__":
    main()
