<h2 align="center">DIGITAL ALPHA'S SEC FILING ANALYZER FOR SAAS COMPANIES</h2>
<h4 align="left">SEC Filings have always been a huge source of information for investors. We are trying to automate and analyze filings and generate insights in context of SAAS companies</h4>

**A React-Django Based ML Web App**  

-------
# Features


The performance of SaaS companies is directly correlated to their customer base. Publicly listed companies are mandated to disclose any information through filings with the SEC. These filings are textual and inconsistent, making it difficult to analyze systematically. We propose an ML-based solution that goes through filings looking for relevant information and also fills any missing data from external sources. We also perform sentiment analysis and highlight any positive/negative sentences in the filing. Any potential investor looking for green/red flags in the filings can quickly do so using this feature. Further, we perform summarization of each section using finbert. Since filings can be more than 130 pages long this is an essential time-saving feature for all investors.

### Approach

We used the open source toolkit, EDGAR CRAWLER, that was published by the authors of the paper: “EDGAR-CORPUS: Billions of Tokens Make The World Go Round” to download 10K, 10Q and 8K filings in HTML format. A crawler is used because SEC Edgar site has limited the number of requests to its page to 10 requests per second and added many other such limitations to avoid systematic download of data using normal data scraping. The reason we selected this toolkit out of various other open source projects was its actively maintained GitHub repository, its ease of use and its ability to parse the filings accurately. The different sections and items from each filing were extracted for performing sentiment, summarization and polarity analysis. Limiting our analysis to the previous three years (ie, the financial years 2021, 2020, and 2019), we found that only 191 of the 290 companies provided in the list in the problem statement were active. 

 

After a detailed analysis of different SEC filings, we realized that most of the information about a company's financials is provided in a tabular format inside the filings. Hence, we used Selenium to automate the process of extraction of tables from the filings using SEC's classical website. The data was downloaded in an excel workbook in multiple sheets. Most of the data required for the computation of the key SaaS metrics was present in these tables.   Furthermore, we also extracted information pertaining to the company, date of filing and other metadata from these tables. The main challenge in retrieving information from these tables was that the data we were looking for was provided in different sheets and under different names. The sheet names were also different for different companies. Hence, it was difficult to automate the process of extraction of information. To this end, we tried using Table QNA models to query information from the table. However, the results were not very good. The results from exploratory data analysis revealed that the key metrics data (revenue, operating costs, sales and marketing costs, customer acquisition cost) were contained in consolidated balance sheets and tables in the MDNA  section. For the cases where this information was not available, the information was procured from external open sourced resources, as mentioned in the problem statement.

To make sure we do not miss any important number or metric, we searched for metrics in the text of 10-K and 10-Q files as well. Since the text of these files varies from filing to filing, there was no particular metric that could be found in all the filings, but wherever found, we have made use of it. 

8-K filings are made when a company makes an important financial decision. These filings do not have a lot of numbers in them and investors are mostly concerned about the sentiment that these filings convey. So, we have performed sentiment analysis on 8-K filings, so that the sentiment can easily be identified without reading the entire document.   

### Key metrics

**Customer Acquisition Cost (CAC)**

Customer acquisition cost (CAC) is the money a business spends to secure a new customer. CAC is important because it is a signifier of profitability and customer revenue. If CAC is low and the revenue you make from a customer is high, profitability will be high, and vice versa.

Formula used - Total Marketing and Sales Expenses / No of new customers acquired

**Gross Margin Percent (GM)**

Gross margin, also known as gross profit margin, is an essential metric for SaaS businesses. Simply, this metric looks at gross profit as a percent of total revenue. It is the amount available to pay operating expenses and reinvest back into the business. Gross margin serves as a good indicator of scalability for SaaS businesses and is an important metric investors consider to determine valuation.Gross margin is an indicator of a SaaS company’s financial health and growth prospects. As gross margin increases, more money (i.e., gross profit) is available for reinvestment into a company’s operating expenses. A company with strong unit economics may choose to invest more cash into sales and marketing.

Formula used - ((Total Revenue - Cost of revenue ) / Total revenue ) \* 100 %


**Annual Recurring Revenue and Monthly Recurring Revenue (ARR and MRR)**

ARR is defined as the value of the contracted recurring revenue components of your term subscriptions normalized to a one-year period. ARR is the less frequently used alternative normalization method than MRR which is for 1-month period. It is used to evaluate the really crucial aspects of the revenue status of the company.

Formula used - MRR = ARR /12 

**Annual Revenue Per User (ARPU)**

Average Revenue Per User (ARPU) measures the revenue your company receives per one user (or unit) over a specific period, which is typically one month. In general, ARPU is one of the most important and useful SaaS metrics as it can help to effectively analyze and model the business’ growth. ARPU can help determine where the business stands financially and whetherit should adjust its product pricing to increase its financial growth.

Formula used - Average Revenue (MRR) / Active Users ( no. of customers)

**Active Users (Number of Customers)**

Number of Active users is a term that refers to the number of unique customers who interacted with a product or service of a company. It is a key performance indicator (KPI) that measures online user engagement. A high number of active users indicate that people are frequently interacting with a product. Therefore, a high number of users is an indication that a product enjoys good customer engagement and retention over a period of time.

- How it's calculated and how we approximate it

**Product Qualified Leads (# Qualified Leads)**

Qualified leads refers to the share of the possible customer market that a SAAS company is able to profit from. A Product Qualified Lead is showing buying intent by being willing to try out your product. This means that there are more chances to improve the conversion rate if PQL is high. The buying intent is usually based on the usage, the interest in the product and whether each lead fits in your set PQL criteria

Formula used  = Total Revenue for the company / Market Size for SAAS companies


  


**Percent Penetration Rate (% Penetration Rate)**

Market penetration is a measure of how much a product or service is being used by customers compared to the total estimated market for that product or service. This is important to judge how a SAAS company is performing in comparison to its competitors. It reflects on the state of marketing and branding of the company and how well it engages and reached more and more customers.

Formula used  = Active Users / Total possible Customers for SAAS companies

**CAC payback period (CAC payback period)**

Customer Acquisition Cost (CAC) payback is the number of months it will take to recover the cost of acquiring a customer (break-even point). CAC payback is an essential metric for any SaaS business. It helps to determine the period of time it will take for your business to regain the expenses incurred by customer acquisition. It helps evaluate the effectiveness of the current business model.

Formula used - CAC / GM \* (ARPU/12) 



**Customer Churn Rate (churn)**

SaaS churn measures the number of SaaS customers who cancel their subscription. Since recurring revenue is the lifeblood of a SaaS business, churn is a metric of critical importance to a SaaS company’s long-term viability.


Formula used - No. of lost customers / Initial number of customers


**Customer Lifetime Value (LTV)**

Customer lifetime value is a key SaaS metric that tells us how much revenue a typical customer will bring in during their relationship with the company. It provides a reliable business viability measure, clarity on customer acquisition spending, enables more efficient marketing and helps achieve steady growth.

Formula used - ARPU \* GM / churn

  
  


**MRR expansion rate**

It is the rate of increase of MRR. It shows the level of improvement in profitability of a SAAS company.

Formula used - (new MRR - old MRR) / old MRR 

**Average Selling Price**

Its the average amount of money generated by one unit of the product (in the case of SAAS, it can be one subscription’s average cost). Its important to judge the business model of a SAAS company.

Formula used - new revenue /new customers added

**LTV : CAC ratio**

This is the ratio of the value a customer provides to the cost of acquiring the customer. The LTV/CAC Ratio is a simple way to evaluate the future prospects of a SaaS company. A higher LTV/CAC Ratio means you have the potential to grow faster and require less capital to do so. This is often attractive to equity investors and can mean a higher valuation for the business. Conversely a lower LTV/CAC Ratio can mean the company is  spending more on acquiring new customers than they are worth to its bottom line.

Formula used - LTV / CAC



**Metrics from Balance Sheet and Income Statements**


These metrics include Total Revenue, Total Assets, Total Liabilities, Debt ratio, total Equity, Total Debt, Total Capitalization, Common Stock Equity, Shareholder Equity, Private Shareholding and Public Shareholding. These metrics are not SAAS specific metrics but nonetheless are important while assessing the health of any company including SAAS companies.
These values are directly taken from SEC filings (item 8 from 10-K filing)



### The most important metric - Number of customers

The number of customers(both active and churned)  is the single most important metric for saas companies. To calculate most of the other metrics like CAC, Churn rate, LTV, ACV, and so on, we require knowledge of the number of customers. After Identifying this fact we tried various methods to extract this knowledge from filings. 

We went through a few filings to find if there is any pattern as to how companies report their no of active customers and churned customers. We found that the ways companies report about the number of customers vary extremely from one company to another.

Examples->

![](https://lh4.googleusercontent.com/XlEOjpDkPKcbhpSBWhZopJhj_3hJ-90srCcI-W2H6oHXtrl6hr_xO5ix0eAsDvSXHqFacdkxR3HVeNOInN-2grO_VHY_jFZolT3aCbkQGJyP9kmmMQ5WbOnLDqMjLDooqMWlDl7SI6hn9-DTym-EWQ)

![](https://lh3.googleusercontent.com/iFfL-YkuURw_3NlDxOMdnAW08fHsA_Zejf06qA4JhR8of6DeNUbCnN1zUkCI1INrqEftYe6F9GNZKDzx2a-JhMagg94DydPgKQPaRhk4kFoHGK-Y8q2sQlE6u8JlFX1meTir5efmqXYuK9vQdRrYrw)

![](https://lh6.googleusercontent.com/f0m6GDoBi5XWzt75vmsfJArr0RFjGoNbpF56tUV2qF0LrczlUxJ55BI_N3_8_I4ySsQvBNkJXVFtpXQXoHiwb_QW9xXEz4RqvKlfjEMRg9VAbe85ShDEYuv-tZPCWtwLFlpu7C0ulDuE2-wAiochLg)

As we can see in the above examples only a few companies quote the number of customers in their filing. Most of the times they only give percentage or verbal indicator about change in number of customers.

The above examples were where the company has talked about the number of customers in some form, but as we explored more filings we found that most of the companies did not even talk about this as this is not a mandatory GAAP measure that they have to report in their filings.

As discussed above, we did not find any general pattern which we could use to extract these numbers so we turned to NLP Transformer models as they are much more flexible and can understand the context in human writing.

### QA models

 After researching various ways of using NLP techniques like NER(named entity recognition) , summarization and QnA. we settled on extractive Question Answering transformer models as our best bet. 

Extractive Question Answering models that we are using are deep learning models that take a context and question in as input and output the answer as string extracted from the context. So if we can provide context from filing and ask the questions like what is the number of customers in 2021? , we would solve our problem!

 

We used hugging face’s implementation of Question Answering models as these are state-of-the-art models which have been trained on a large corpus of text. There are various models available on hugging face. We experimented with various models and chose the one with the best result in our experimentation.

Examples ->

The model used->

distilbert-base-cased-distilled-squad

![](https://lh4.googleusercontent.com/NlKph_wFB-SiTs69RMRwyHI69hVH_PZ9kxQ094hmQN8mkf2QqEmjgZxYeS3M1BZ6HYBJQAjI6itkqdblsMCemN0SGfSGaSN2cqYHKN4G1fT9Zyi_JzSAWKfDkBQiDgBQSr2rbS0pLo6KHMNLfRifGw)

The model used->

deepset/roberta-large-squad2 

![](https://lh5.googleusercontent.com/Xn_sL5pl0-CWxUtv-51iWVscvcqgAkImzU9bRT-vppAKCm-O-A6fslKC4O8pHay8zWkcdcvJhz3_J3NXwQ8HAFHDPa6-wYNdGw_tbSIaQsJq_vu2MRLlV_8aVOBQcGGfRxuZnUaZQTWC2BDHwM_qrA)

And we tried other models also, roberta large model performed the best  as it is able to infer the context well.

After selecting the model the challenge is what will be the context for the question. One can think of passing the whole text of the filling as the context but these fillings are voluminous(130+ pages)  and it gets considerably difficult for QA models to extract answers from such a large string of text. 

Now we took 2 approaches to shorten the context ->

The first approach is Question dependent like if the question is “what is the number of customers in 2021?” Now since we know this info will be located in paragraphs where the word customers or its synonyms like users, clients, etc are mentioned along with numerical figures being present in this paragraph. So we can apply a regex search to narrow down such paragraphs and join these paragraphs to form a context. This reduces the context size considerably and improves the accuracy of the results a lot. But the main shortcoming of this method is that we have to think about ways of shortening the context for each question/metric and hence this approach is not that scalable.

In the second approach, we tried to form a context that can serve as a general context for all the questions. Here we use the fact that most of the important information in filings are present in Item 7 and 7A which is the Management Discussion and Analysis section. Now again Item 7 and 7A is quite big of a context for the QA model to work with. So to reduce context we can use summarization models which are also the state of the art transformer models from hugging face. Now to reduce the size of item 7 we first divide it into n parts and summarize it part individually and then join these summarized parts to form the context for our questions. In practice, we found that n = 25 performed well enough while not making the context too big. So now we can ask questions like what is the churn rate, what is the customer retention, and so on from this generalized context. 

**Scraping customers using google query->**

As discussed above most of the companies have not mentioned anything regarding their number of customers at all since it is not a compulsory GAAP measure. In this case where we are not able to extract customers using the QA model, we  will have to make use of 3rd party sources. We have used google queries to know the latest number of active customers of a company and approximated for rest of the years on the basis of change of revenue. We have also provided link of the website on the dashboard so that if a user wants to check the authenticity of the data then he/she can. In cases where we were not able to extract data from google we have made relevant approximations based on companies revenue and and size and scale of the whole SAAS market.

  


### NLP

**Summarization:**

The technique, where a computer program shortens longer texts and generates summaries to pass the intended message, is defined as Automatic Text Summarization and is a common problem in machine learning and natural language processing (NLP). SEC filings which are generally more than 130+ pages long require a lot of reading to extract and understand information. Thus, to simplify this process, we tried to summarize the different sections present in the form. First, we applied some basic text cleaning techniques. We have used the hugging face transformers pipeline for this task. We have tried various transformer models like T-5 base T-5 large, and based on our observations, we have stuck with Bart-large-CNN. It is a transformer encoder-encoder (seq2seq) model with a bidirectional (BERT-like) encoder and an autoregressive (GPT-like) decoder by Facebook. It was fine-tuned for CNN Daily Mail, an extensive collection of text-summary pairs.

Example of Facebook Bart-large-CNN:

![](https://lh6.googleusercontent.com/hlwQOud0wftTo3dMWitlG7ta9dLZBzWnoSB56l3qk8tlA1E3CgCj8SSJEjBeRByeNyr0PdKrbuQGBKZyqLk_Gh-tBoiQQ1HO6Sh3bz-tZ4O1aB8n2bgYqFdotN7ion1cID0wurwEOnXnYz4wIBnesw)

![](https://lh4.googleusercontent.com/wbB51qTsILvZAIpX22BFHqQpvW5JJznLw7dVF-p9e4ptjFlxkyaxJHd48UQnNGOBY0CuZbm2DMPT5A5Y8OYVjRCalphcxMD_QGI1_Ap5JPvRHmQLCdv1FgnJfMPm9HKvkKoYo0N2KMxL3GgmLzKIHQ)

After performing summarization, we applied sentiment analysis on each section, which is discussed in the sentiment analysis section below.

**Sentiment Analysis:**

Sentiment analysis is the process of detecting positive or negative sentiment in text. Businesses often use it to detect sentiment in social data, gauge brand reputation, and understand customers. On the summarized text, we then performed sentiment analysis. We have tried several models under Hugging Face transformers pipelines like Bert, Roberta, Roberta Large, and many more, and based on our observation, we have stuck with the FinBERT model. FinBERT is a pre-trained NLP model to analyze the sentiment of the financial text. It is built by training the BERT language model in the finance domain, using a large financial corpus, and fine-tuning it for financial sentiment classification. [Financial PhraseBank](https://www.researchgate.net/publication/251231107_Good_Debt_or_Bad_Debt_Detecting_Semantic_Orientations_in_Economic_Texts) by Malo et al. (2014) is used to fine-tune the model.

Example of FinBERT:

![](https://lh4.googleusercontent.com/XPVvHt7tZ_MfzyH3oE9al4PLyMSzgL-dium0nl5mLMhQl7RGcNs6Lx8tl0LARsYLv6KQlUEpgbU1qufT364QHRUw6usf474CGAfYLS5KkkKOOyyThzsTqxJkRpE9wmC43ycsyqi0GKohOf3S6z1SKQ)![](https://lh5.googleusercontent.com/Wun34Il-i_pqGEHVmZXmyFGDYVbt1pWDgajfyaK88Wm0ZLwyhp32WPMNobZ0fxIkq1n5NckL_cEW_EABke7Gxbw_W-QzS7lxjstPfl4oFFlUHpELCAjOpbocnnfYgyPep1HIV22-qiwTof9T97dkaQ "Example of FinBERT")

Then we used the Textblob library for finding the polarity of each section. TextBlob is a Python library that offers a simple API to access its methods to perform various NLP tasks. TextBlob actively used Natural Language ToolKit (NLTK) to achieve its tasks. Polarity is of float type and lies in the range of -1 to 1, where 1 means a high positive sentiment, and -1 means a high negative sentiment. 

We decided to highlight key impactful sentences in the form of this obtained polarity. This will ease the reader's work to focus on positive and negative sentences. To make it more attractive and visually appealing, we have added a gradient shade between green and red so that the sentence's tone isn't limited to only three labels and can vary between -1 to 1. We also added a Gauge Chart to visualize this polarity to give investors an easy idea about the polarity. Then we integrated all this to the hosted site so that investors could access all this in one place.

Example:

![](https://lh3.googleusercontent.com/un_TjCyR5MqmmhutaV-TCmvXmQ6Q4RF_LgmG7H-6JVSiFrR9Nul5uqUhogzEYMyrRaRljFj8ooeCHZxfPX_fQ0V01k5EH1oiVvzfrDhQ1kncxQ3MIrRiJvvcpmjgSxvW_ysm7EV_K55jMR9BwIZy2A)

![](https://lh3.googleusercontent.com/7GVUppusLgREUAWPtOVLuZupTO8xVaGKA0yUR-bqOzaxLZnkgmZqvqg0tHusgdHCcXQTL2lfBYE0B6BczdHYlae8j4gepQjS8mVJoOEECTtmmWQ2vOP-6R-Qxgi8JA3THvIuwmX-syuHlrkUATF97g)





# Usage

### Prerequisites

1.  [Git](https://git-scm.com/downloads).
2.  [Node & npm](https://nodejs.org/en/download/) _(version 12 or greater)_.
3.  A fork of the repo.
4. Python3 environment to install Django and its dependencies
5. [PyTorch](https://pytorch.org/)

### Directory Structure

The following is a high-level overview of relevant files and folders.

```
backend/
├── dashboard_apis/
│   ├── core/
│   ├── dashboard_apis/
|   ├── dataentry.py
|   ├── dbsqlite3
|   ├── manage.py
|   └── requirements.txt
|── analytics/
|   |──given data/
|   |──source code/
|   |  |__ python source code files for edgar scraping/
|   |  |__ python source code files for metrics calculations/
|   |  |__ python source code files for miscellaneous work/
|   |  |__ python source code files for outside sources scraping/
|   |  |__ python source code files for text analysis - NLP/
|   |
└── frontend/
    ├── public/
    │   ├── index.html
    │   └── ...
    ├── src/
    │   ├── actions/
    │   │   ├── actions.js
    │   ├── Components/
    │   │   ├── Global 
    │   │   └── Widgets
    │   ├── constants/
    │   ├── fonts/
    │   ├── constants/
    │   ├── images/
    │   ├── Pages/
    |       ├── BasketList/
    |       ├── Company/
    |       ├── Error404/
    |       ├── Filenew/
    |       ├── Files/
    |       ├── IndividualBasket/
    |       ├── Landing/
    |       ├── RecentlyViewed/
    |       └── Search/
    |   ├── reducers/
    |   ├── utils/
    |   ├── App.js
    |   ├── config.js
    |   ├── global.scss
    |   ├── index.js
    |   ├── registerServiceWorker.js
    |   └── store.js
    ├── package-lock.json
    ├── package.json
    ├── README.md
    ├── yarn.lock
    └── .gitignore
       
```

## Installation

### Steps to run backend

In order to install all packages follow the steps below:

 1. Move to backend folder
 2. Then move into the dashboard_apis folder
 3. For installing virtual environment - `python3 -m pip install --user virtualenv`
 4. Create A Virtual env - `python3 -m venv env`
 5. Activate virtual env - `source env/bin/activate`
 6. `pip3 install -r requirements.txt`
 7. `python manage.py runserver localhost:8000`

### Steps To Set Up Frontend
 1. Move to frontend folder
 2. Move into dashboard_frontend
 3. `npm install`
 4. `npm start`


 ### Steps To Extract Raw Edgar Filings in Analytics
 1. Move to backend folder
 2. Move into analytics folder
 3. Move into analytics folder
 4. Move into folder python source code files for edgar scraping
 5. Move into folder directory_for_scraping_edgar_metadata
 6. Install dependencies via `pip install -r requirements.txt`
 7. Before running any script, you can edit the `config.json` file to adjust parameters.
 8. To download financial reports from EDGAR, run `python edgar_crawler.py
 9. To clean and extract specific item sections from already-downloaded 10-K documents, run `python extract_items.py`.
 Note : All folders in analytics folder are named according to the python files they contain.




> The model will be served on **http://localhost:8000/**
