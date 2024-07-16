# Goal

The objective of this project is to create a transaction monitoring system that records and analyzes the status of transactions in a MySQL database, as well as sending alerts in case of anomalies.

## Data analysis

### General Comparison

The data from the two CSV files shows the number of POS sales per hour, allowing a comparison between sales from today (today), yesterday (yesterday) and the same date from the previous week (same_day_last_week), in addition to the average from the last week ( avg_last_week) and the average of the last month (avg_last_month).

#### 1. General Trends

- **Sales Peaks:** A peak in sales is observed between 10am and 3pm on both days. For example, today, the highest sale was at 10am with 55 sales on CSV 1 ![csv1](/images/image-2.png)

- and 43 in CSV 2 ![csv2](/images/image-1.png).

- **Drop in Sales:** After 3pm, sales start to decrease![alt text](/images/image-3.png),

- especially in CSV 2, where there was a zero at several times in the afternoon ![alt text](/images/image-4.png).

#### 2. Comparison between CSVs

- **CSV 1 vs CSV 2:** CSV 1 generally has higher sales numbers than CSV 2. This may indicate a difference in business activity or sales effectiveness on different days.

##### Notable Anomalies:

- **CSV 1:** The 10am time slot shows a significant increase in sales (55), contrasting with what would be expected. This suggests an anomaly, as it is well above average for most hours.

- **CSV 2:** From 3pm onwards, sales drop drastically, with zeros, which could also indicate an anomaly or an interruption in the service.

#### 3. Specific Metrics

![alt text](/images/image-5.png)

#### 4. Anomaly Analysis

##### Anomaly Identified

The most obvious anomaly is the drastic drop in sales after 3pm in CSV 2, where sales drop to zero. This may be an indication of:

- **System Outage:** The POS system may have experienced technical problems after this time.
- **Change in Customer Behavior:** A change in customer flow or opening hours may have occurred.
- **External Events:** External factors such as holidays or events in the region may have impacted sales.

#### 5. SQL Query for Analysis

To investigate further, we can run an SQL query to calculate the average sales per hour and see if any specific hour had an extreme variation:

![alt text](/images/image-6.png)

![alt text](/images/image-7.png)

![alt text](/images/image-8.png)

### Sales Chart

A graph can be generated to visualize sales over hours to identify peaks and dips. In this case, we use the code `grafico_vendas.py` to generate the graph.

![Sales Chart](grafico_vendas.png)

## Conclusion

- **Sales Peak:** The 10am time is a highlight, showing a sales volume well above the average.
- **Abnormal Drop:** From 3pm on CSV 2, sales drop drastically, which can be considered an anomaly and requires further investigation.
- **Data Comparison:** Analysis allows you to identify trends and patterns that can be used to optimize future sales strategies and understand customer behavior.
