# GOAT Debate Analysis: Instagram Comments on Messi vs. Ronaldo

Author: David Li

Date: 2024-03-01

**Project Overview**

This project aims to analyze Instagram comments from posts related to two of the most followed sports personalities: Lionel Messi and Cristiano Ronaldo. The analysis is focused on exploring the sentiment of the comments, particularly regarding the popular “GOAT” (Greatest of All Time) debate, and extracting insights from the usage of emojis and mentions of each other in the comments.

**Data Collection**

The data consists of comments scraped directly from Instagram posts of Messi and Ronaldo. Due to the dynamic nature of Instagram and its strong protections against scraping, the data collection process was quite challenging. The raw data is quite messy, requiring extensive cleaning and preprocessing before analysis.

**Data Preparation**

	Data Cleaning:
	•	The raw CSV files were cleaned using custom functions to remove irrelevant rows and extract meaningful information like usernames, comments, and the number of likes.
	•	The cleaning process was unique to each set of comments due to the variability in the data structure.
	Data Reshaping:
	•	Comments were reshaped to align usernames with their respective comments and likes. Missing values were handled, and the final dataset was prepared for analysis.
	Language Detection:
	•	Comments were categorized by language to ensure appropriate analysis, especially for sentiment analysis.
	Final Data:
	•	The cleaned and reshaped data were saved in an RData file for further analysis.

**Analysis**

1. GOAT Comments Analysis

	•	The frequency and percentage of comments containing the term “GOAT” were calculated for both Messi and Ronaldo.
	
 •	Findings: A significantly larger proportion of Messi’s comments mentioned the word “GOAT” compared to Ronaldo’s, suggesting a stronger association with the title among Messi’s fanbase.

2. Cross Mentions in Comments

•	The frequency of mentions of Ronaldo in Messi’s comments and vice versa was analyzed.
	
 •	Findings: Ronaldo was mentioned more frequently in Messi’s comments than Messi was in Ronaldo’s comments, indicating a potential psychological impact or rivalry between the fanbases.

3. Emoji Sentiment Analysis

•	An emoji-based sentiment analysis was conducted using a pre-existing emoji sentiment dataset.
	
 •	Findings: Ronaldo’s comments had a slightly higher average sentiment score compared to Messi’s, suggesting more positive emoji usage among Ronaldo’s fans.

4. SIUU Comments Analysis

•	The frequency of the phrase “SIUU,” Ronaldo’s signature celebration shout, was analyzed in both Ronaldo’s and Messi’s comments.
	
 •	Findings: The phrase appeared in a notable percentage of Ronaldo’s comments and even a smaller percentage in Messi’s comments, showcasing its widespread recognition.

**Visualization**

Interactive visualizations of emoji usage and sentiment scores were created using Plotly, allowing for an intuitive understanding of the data.

**Files in This Repository**

data_prep.Rmd: RMarkdown file used for data cleaning, reshaping, and preparation.
ig_comments_data.Rdata: Saved R data file containing the cleaned and prepared data for analysis.
analysis_and_writeup.Rmd: RMarkdown file containing the analysis and visualizations.
emoji_sentiment.csv: CSV file containing sentiment data for various emojis.
