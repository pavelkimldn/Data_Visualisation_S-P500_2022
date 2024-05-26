# Data_Visualisation_S&P500_2022

### S&P 500 Data Visualization Report

#### Histogram of Price Distribution

The histogram visualizes the distribution of prices of the companies within the S&P 500. The y-axis represents the frequency of companies and the x-axis represents the price ranges. The tallest bar corresponds to the price range of $0-85 with a frequency slightly above 300, indicating that the majority of the companies have their stock prices within this range. The next significant bar represents the price range of $85-170 with a frequency just below 150, suggesting that a considerable number of companies also fall within this price range, though less than the previous range. The bar representing the price range of $170-250 has a frequency around 40, indicating fewer companies in this price bracket. Prices beyond $250 have negligible frequencies, showing that very few companies have stock prices in these higher ranges.

![github]([/images/icon.png](https://github.com/pavelkimldn/Data_Visualisation_S-P500_2022/blob/main/Picture%201.png))

#### Scatter Plot of Price vs. Earnings Per Share (EPS)

The scatter plot visualizes the relationship between the stock prices and the earnings per share (EPS) of companies within the S&P 500. In the plot, each point represents a company with the x-axis denoting the price per share and the y-axis representing the earnings per share. The majority of the points are concentrated in the region where the EPS ranges from -10 to 20 and the stock price ranges from $0 to $250. This dense grouping suggests that most companies have relatively modest EPS and stock prices, indicating a typical range for S&P 500 companies. There are a few points scattered further from the origin, representing companies with either significantly higher stock prices or EPS. Notably, one point is the furthest from the origin with an EPS of 40 and a stock price of $1750, highlighting a company with exceptionally high profitability and stock value. This outlier can indicate a market leader or a company with unique advantages that allow for high earnings and stock valuation.

![github]([/images/icon.png](https://github.com/pavelkimldn/Data_Visualisation_S-P500_2022/blob/main/Picture%202.png))

#### Box Plot of Dividend Yield by Sector

The box plot illustrates the distribution of dividend yields across various sectors within the S&P 500. The x-axis represents different sectors, while the y-axis shows the dividend yield percentages. The plot reveals significant variation in dividend yields among sectors, with each box indicating the interquartile range (IQR), whiskers extending to 1.5 times the IQR, and outliers marked as individual points. Several key observations can be made:
- The Telecommunication Services sector shows the highest median dividend yield, along with a wide IQR and several outliers, indicating a broad range of dividend yields within the sector.
- Utilities and Real Estate sectors also exhibit relatively high median dividend yields and larger IQRs, suggesting they are generally high-dividend sectors.
- Sectors like Health Care, Information Technology, and Industrials have lower median dividend yields and narrower IQRs, indicating more consistent but lower dividends across companies in these sectors.
- Outliers in almost every sector highlight individual companies with dividend yields significantly different from their peers.

![github]([/images/icon.png](https://github.com/pavelkimldn/Data_Visualisation_S-P500_2022/blob/main/Picture%203.png))

#### Heatmap of Correlation Matrix

The correlation matrix reveals several key relationships between financial metrics. There is a moderate positive correlation (0.59) between the stock price and earnings per share (EPS), indicating that companies with higher earnings tend to have higher stock prices. Similarly, there is a moderate positive correlation (0.41) between stock price and market capitalization, suggesting that larger companies (by market cap) tend to have higher stock prices. On the other hand, there is a weak negative correlation (-0.24) between stock price and dividend yield, which could imply that higher-priced stocks might offer lower dividend yields, possibly because they are growth stocks that reinvest earnings rather than paying them out as dividends. The Price/Earnings (PE) ratio shows no strong correlations with most other variables, suggesting that PE ratios vary independently of other financial metrics in this dataset. Additionally, there is a moderate positive correlation (0.65) between market capitalization and EBITDA, indicating that larger companies tend to have higher earnings before interest, taxes, depreciation, and amortization.

![github]([/images/icon.png](https://github.com/pavelkimldn/Data_Visualisation_S-P500_2022/blob/main/Picture%204.png))

#### Bubble Chart of Market Cap vs. Sector vs. Price

The bubble chart visualizes the relationship between stock price and market capitalization, with the size of the bubbles representing the company's EBITDA. The x-axis denotes the stock price, the y-axis represents the market capitalization, and the bubble size indicates the EBITDA. The majority of the companies cluster around lower stock prices (below $250) and lower market capitalizations, indicating that most companies in the S&P 500 have relatively modest stock prices and market caps. There are a few notable outliers with high market capitalization and high stock prices. For instance, one prominent outlier has a stock price of approximately $1750 and a market cap of around $6 trillion. Larger bubbles, representing higher EBITDA values, are dispersed among the companies, with some of the largest bubbles found at higher market caps. This suggests that companies with higher earnings before interest, taxes, depreciation, and amortization tend to have larger market capitalizations. The chart shows that while high market cap companies often have high stock prices, there are several companies with high market caps but relatively moderate stock prices, indicating diversity in how market cap is achieved.

![github]([/images/icon.png](https://github.com/pavelkimldn/Data_Visualisation_S-P500_2022/blob/main/Picture%205.png))

#### Violin Plot of Price by Sector

The violin plot visualizes the distribution of stock prices across different sectors within the S&P 500. Each violin represents a sector, and the width of the violin at different price levels indicates the density of companies with stock prices in that range. Key observations:
- **Consumer Discretionary:** This sector shows a wide range of stock prices, with some companies having very high prices up to around $2000. This indicates significant variability within the sector, possibly due to the presence of both luxury brands and more affordable consumer goods companies.
- **Information Technology:** The Information Technology sector also displays a broad range of stock prices, with a notable concentration of companies around the mid to high price range. This reflects the diversity within the tech sector, encompassing both large established firms and smaller innovative startups.
- **Health Care, Industrials, and Financials:** These sectors show a more concentrated distribution of stock prices, with most companies having prices within a narrower range. This suggests more uniformity in market valuation within these sectors.
- **Utilities and Consumer Staples:** These sectors tend to have lower stock prices, with most companies clustered in the lower price range. This could indicate that companies in these sectors are perceived as more stable and less volatile, leading to more moderate stock prices.
- **Telecommunication Services and Energy:** These sectors show relatively less variability in stock prices, indicating a more homogeneous valuation among companies within these sectors.

![github]([/images/icon.png](https://github.com/pavelkimldn/Data_Visualisation_S-P500_2022/blob/main/Picture%206.png))

#### Pairplot of Numeric Variables

The pairplot visualizes the relationships between several numeric variables in the dataset. Each subplot represents a pairwise comparison between two variables, while the diagonal shows the distribution of each variable. Key observations:
- **Price Distribution:** The histogram on the diagonal for the Price variable indicates a right-skewed distribution, with most stock prices clustered at the lower end and a few high-priced stocks creating a long tail.
- **Price vs. Earnings Per Share (EPS):** The scatter plot shows a positive correlation between Price and Earnings Per Share (EPS), with higher stock prices generally associated with higher EPS values. This suggests that companies with higher earnings tend to have higher stock prices.
- **Price vs. Price/Earnings (PE) Ratio:** There is a wide scatter of points, indicating no clear linear relationship between Price and Price/Earnings (PE) Ratio. This suggests that PE ratios vary independently of stock prices in this dataset.
- **Price vs. EBITDA:** There is a positive correlation between Price and EBITDA, with companies having higher EBITDA values tending to have higher stock prices. This implies that more profitable companies are valued higher in the market.
- **Distribution of Price/Earnings (PE) Ratio and Dividend Yield:** The histograms for Price/Earnings (PE) Ratio and Dividend Yield indicate a concentrated distribution with a few outliers. Most companies have PE ratios and dividend yields within a narrow range, but some companies significantly deviate from the mean.

![github]([/images/icon.png](https://github.com/pavelkimldn/Data_Visualisation_S-P500_2022/blob/main/Picture%207.png))

#### 3D Scatter Plot of Price, EPS, and Market Cap

The 3D scatter plot visualizes the relationship between stock price, earnings per share (EPS), and market capitalization for the companies in the dataset. The x-axis represents the stock price, the y-axis represents the EPS, and the z-axis represents the market capitalization. Key observations:
- **Clustering of Companies:** Most companies are clustered in the region where stock prices are below $500, EPS ranges from 0 to 20, and market cap is less than $1 trillion. This indicates that the majority of companies in the S&P 500 have moderate stock prices and EPS values.
- **Outliers:** There are a few outliers with higher stock prices and market caps. For example, one notable outlier has a stock price around $1750 and a market cap significantly higher than the rest, indicating a highly valued company with substantial earnings.
- **Positive Correlation:** The plot suggests a positive correlation between stock price and EPS, as well as between stock price and market capitalization. Companies with higher EPS tend to have higher stock prices and larger market caps.
- **Market Cap Distribution:** The distribution of market capitalization is wide, with some companies having much larger market caps than others. This highlights the diversity in company sizes within the S&P 500.

![github]([/images/icon.png](https://github.com/pavelkimldn/Data_Visualisation_S-P500_2022/blob/main/Picture%208.png))

