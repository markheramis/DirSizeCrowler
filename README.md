# DIR Size Crowler

This is a small tool that I wrote to figure out which one in the directory is taking so much space by passing a group of paths to scan for

## How to use

### Scanning one path

```bash
python dir-crowler.py ~/my-projects
```

The command above will scan and get the directory and file sizes inside the `~/my-projects` directory.

### Scanning Multiple Paths

```bash
python dir-crowler.py ~/my-projects ~/my-backup-projects
```

The command above will scan the two directory paths for file/folder sizes.

*Note: You can input as many filepath as needed, the program will just loop through the following paths*