# xbar-custom-plugins
This repo contains scripts that add functionality to xbar.


### Usage
* You have to add scripts to xbar plugin folder. If you don't find related folder, you can choose  "open plugin folder" from xbar menu
* Scripts should be executable so you can run below command 
* ```chmod +x <script>```
* Let's refresh xbar 🥳

### weather-from-google-search.py
Get city weather data from google search\
change below lines(12-15) according to your location
```
params = {
  "q": "istanbul weather",
  "hl": "tr",
}

```

<img width="187" alt="Screen Shot 2022-01-06 at 18 03 37" src="https://user-images.githubusercontent.com/45356325/148403584-018653ee-3a95-4991-b757-8c22934c2a8e.png">

### currency-usd-euro-gld-to-try.py
Get turkish lira rates 

<img width="174" alt="Screen Shot 2022-01-07 at 17 54 44" src="https://user-images.githubusercontent.com/45356325/148561807-308ee1ab-63d3-40ee-8cfb-8eb50c2400cb.png">