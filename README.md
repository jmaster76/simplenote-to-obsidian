In detail this tool does the following:

- **Converts Simplenote File Formats:** Takes your Simplenote files and converts them to `.md` for Obsidian.

- **Backdates macOS System Timestamps:** Overrides macOS kernel locks to force the actual file creation and modification dates to match your true Simplenote history.

- **Protects Metadata:** Writes permanent, text-based YAML metadata (`created:`, `updated:`) inside the note so your timeline never corrupts when syncing to an iPhone.

- **Fixes Tags and Formatting:** Formats Simplenote tags into native Obsidian frontmatter and strips out illegal characters (like forward slashes) from filenames without losing data.

Prerequisites
You must have Xcode Command Line Tools installed to let the script modify system creation dates. Check your status in Terminal:

```bash
xcode-select -p
```

*If it returns an error, install them using:* `xcode-select --install`
Step-by-Step Guide
1\. Setup

1. Export your notes from Simplenote and gather your `notes.json` file (this will be in a folder inside the zip file, along with all the individual `.txt` files).

2. Create a folder on your Desktop named `Simplenote to Obsidian`.

3. Put your `notes.json` and `convert_notes.py` into that folder.

2\. Run
Open Terminal and run these commands:

```bash
cd "/Users/YOUR_MAC_USERNAME/Desktop/Simplenote to Obsidian"python3 convert_notes.py notes.json
```

3\. Deploy

1. Drag the new `Obsidian_Import` folder into your Obsidian vault.

2. In the Obsidian sidebar, click the **Sort** icon and choose **Modified time (new to old)**.
