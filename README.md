# rtx-crawler
This script constantly checks the price of those jucy rtx-3080Ti. I asume you have linux, bash, and python3. You will also need the python libraries `bs4`, `urllib3`, and `requests`

| Function | command |
| ------------- |-------------|
| For a one-time run | ```python3 crawler.py``` |
| To redirect the output in a computer-readable manner | `python3 crawler.py > output.log` | 
| Keep it running, peek and log stats in `rtx3080ti.log` every 30 minutes | `./runner.sh` |

## To Do
- Wouldn't it be nice to plot this stuff?
