import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LLAMA_CLOUD_API_KEY = os.getenv("LLAMA_CLOUD_API_KEY")

FILE_PATH = "/content/Amazon-com-Inc-2023-Annual-Report.pdf"
CHROMA_DB_PATH = "./chroma_db"

sample_queries = [
    "what are the future goals for 1998 for amazon",
    "Can you tell me the name of CEO Worldwide Amazon Stores?",
    "Can you elaborate on the inventory risks faced by Amazon?",
    "How the cash flow information has changed from 2022 to 2023",
    "Tell me the spend of acquisition and goodwill activity in year 2023",
    "Can you summarize the income tax contingencies for year 2021, 2022 and 2023"
]

expected_responses = [
    "Amazon's goals for 1998 included expanding product offerings (starting with music), investing in systems and infrastructure to improve customer experience, and better serving international customers by improving delivery times and localizing experiences. They aimed to solidify their brand while managing the challenge of prioritizing their investments in a fast-growing environment&#8203;:contentReference[oaicite:0]{index=0}.",
    
    "Douglas J. Herrington is the CEO Worldwide Amazon Stores. He has held this position since July 2022&#8203;:contentReference[oaicite:1]{index=1}.",
    
    "In 1997, Amazon faced inventory risks due to seasonality, new product launches, pricing changes, consumer demand shifts, and overstocking or understocking. The company also dealt with risks related to establishing vendor relationships and demand forecasting when launching new products&#8203;:contentReference[oaicite:2]{index=2}.",
    
    "Amazon's operating cash flow increased from $46.8 billion in 2022 to $84.9 billion in 2023. Investing cash flow decreased further from -$37.6 billion to -$49.8 billion, while financing activities shifted from $9.7 billion provided in 2022 to -$15.9 billion used in 2023, reflecting major changes in acquisition, investments, and financing strategy&#8203;:contentReference[oaicite:3]{index=3}.",
    
    "In 2023, Amazon spent approximately $3.5 billion in cash for the acquisition of 1Life Healthcare, Inc. (One Medical), which included $1.3 billion of intangible assets and $2.5 billion of goodwill. Other acquisitions in 2023 were considered immaterial&#8203;:contentReference[oaicite:4]{index=4}.",
    
    "For the years 2021, 2022, and 2023, Amazon.com, Inc. reported gross income tax contingencies of $3.24 billion, $4.00 billion, and $5.23 billion respectively as of December 31. Increases and decreases to prior and current year tax positions were recorded each year, with notable increases of $1.01 billion in 2023 for current year positions. Settlements and statute expirations led to reductions in contingencies each year. As of the end of 2023, $3.3 billion of the $5.23 billion would reduce the effective tax rate if recognized. Interest and penalties accrued (net of federal tax benefit) were $28M in 2021, a $7M reduction in 2022, and $91M added in 2023. Amazon is under audit in several countries, including the U.S., India, Luxembourg, and Germany, which may impact future tax positions."
]
