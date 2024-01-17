# Release Notes Log Generator

This python repo fetches commit data from a public GitHub repository and generates a HTML change log page grouped by convention.

## Usage

1. Clone the repository or download the project.

   ```bash
   git clone git@github.com:Yashwanth70/release_notes.git
2. Go inside the repo
    ```bash
    cd release_notes
3. Create python3 environment
    ```bash
    virtualenv -p python3 env
4. Install required dependencies using pip inside the repo.
    ```bash
    pip install requests Jinja2
5. Run the script.
    ```bash
    python main.py
6. Open the generated HTML file (index.html) in a web browser to view the change log.
7. This is deployed on Vercel, here is the link:
```commandline
https://release-notes-wheat.vercel.app/
```