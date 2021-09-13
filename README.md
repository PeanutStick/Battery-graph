# Battery-graph
it will display a graph in the terminal with the battery usage
# Install
Copy ".service" and ".timer" files in:    
/etc/systemd/system    
Execute:    
sudo systemctl enable change-csv.service    
sudo systemctl enable battery.service
    
You can create an alias like this:    
alias bat="python3 /path/to/main.py"     
# Screen
![image](https://i.imgur.com/6pS8kg1.png)
# How does it work?
The while line is the current session, The orange line is the previous one.

