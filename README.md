![alt text](https://www.era-environmental.com/hs-fs/hubfs/ETL-era-environmetal-management.png?width=566&name=ETL-era-environmetal-management.png)



The aim of this project was to investigate whether there is a correlation between a country's Corruption Perceptions Index (CPI) and its Environment Performance Index (EPI). To do this, I loaded two datasets - epi_countries from the epi PostgreSQL database and cpi dataset from a CSV file - and created dataframes from each of them. The cpi dataframe contained information about various environmental health metrics such as air health, water health, forestries, and others for each country in the list. The epi dataframe contained each country's Corruption Perceptions Index. A higher CPI indicates that a country is better at handling corruption.

I used seaborn plots to create visualizations to see if there was any connection between the CPI and environment health categories. When making the plots on the CPI and EPI, we could infer that countries that handle corruption better have a higher EPI. However, when I made graphs on separate categories like the CPI's impact on forestry, the connection wasn't obvious. Some countries with a low CPI had a high index on forestry.

To find a more comprehensive connection between corruption and environmental health, I believe we need a more detailed dataset. I wish the dataset had some kind of corruption scores on each country's biggest industries since various industries could directly lead to deforestation or water pollution, among others. I would like to gather more information on that.



I also used Tableau to create some visualizations to confirm or refute my observations regarding the connection between the CPI and EPI. The results were similar to those obtained using seaborn plots. In general, we can infer that the higher the CPI, the higher the EPI is. It appears that there are fewer violations and less environmental damage in countries that have better control of corruption. However, as mentioned above, there are still a great number of countries with terrible CPI scores and decent levels of various environmental metrics' health. Therefore, we need more extensive data to make valid assumptions.

![screenshots1](images\countryRank.png?raw=true)
![screenshots2](images\countryscore.png?raw=true)
![screenshots3](images\histwater_h.png?raw=true)
![screenshots4](images\airrank.png?raw=true)