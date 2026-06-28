import pandas as pd
import numpy as np
import sqlite3

def run_pipeline():
    try:

            # Task 1: Data Ingestion:

            sales_df = pd.read_csv("sales_data.csv")
            products_df = pd.read_csv("products.csv")
            stores_df = pd.read_csv("stores.csv")

            print("Sales Data Shape:", sales_df.shape)
            print(sales_df.head())

            print("\nProducts Data Shape:", products_df.shape)
            print(products_df.head())

            print("\nStores Data Shape:", stores_df.shape)
            print(stores_df.head())

            #Check for missing values

            print("\nMissing values in sales_data:")
            print(sales_df.isnull().sum())

            print("\nMissing values in products:")
            print(products_df.isnull().sum())

            print("\nMissing values in stores:")
            print(stores_df.isnull().sum())

            # Task 2: Data Cleaning:
            # Remove duplicates from sales_data

            before_rows = sales_df.shape[0]
            sales_df = sales_df.drop_duplicates()
            after_rows = sales_df.shape[0]

            print("\nDuplicate rows found and removed:", before_rows - after_rows)

            # Fill missing quantity and drop NULL amount

            sales_df["quantity"] = sales_df["quantity"].fillna(0)
            sales_df = sales_df.dropna(subset=["amount"])

            print("\nCleaned Sales Data Shape:", sales_df.shape)

            # Convert data types 

            sales_df["sale_date"] = pd.to_datetime(sales_df["sale_date"])
            sales_df["amount"] = sales_df["amount"].astype(float)
            sales_df["quantity"] = sales_df["quantity"].astype(int)  


            # Task 3: Data Transformation:
                # Merge sales_data with products and stores

            final_df = sales_df.merge(products_df, on="product_id", how="left") \
                            .merge(stores_df, on="store_id", how="left")

            print("\nFinal Merged DataFrame:")
            print(final_df)

            # Add total_revenue and print stats


            final_df["total_revenue"] = final_df["quantity"] * final_df["price"]

            print("\nRevenue Statistics:")
            print("Mean total_revenue:", np.mean(final_df["total_revenue"]))
            print("Max total_revenue :", np.max(final_df["total_revenue"]))
            print("Min total_revenue :", np.min(final_df["total_revenue"]))
            
            #Revenue per city


            city_revenue = final_df.groupby("city")["total_revenue"].sum().sort_values(ascending=False)

            print("\nTotal revenue by city:")
            print(city_revenue)

            # Task 4: Data Loading (SQL):

            #Load into SQLite database

            conn = sqlite3.connect("retail_sales.db")
            final_df.to_sql("retail_sales", conn, if_exists="replace", index=False)

            print("\nData loaded into SQLite table: retail_sales")

            #SQL query: Top 3 best-selling products

            top_products_query = """
            SELECT product_name, SUM(quantity) AS total_quantity
            FROM retail_sales
            GROUP BY product_name
            ORDER BY total_quantity DESC
            LIMIT 3;
            """

            print("\nTop 3 best-selling products:")
            print(pd.read_sql_query(top_products_query, conn))

            #Task 5: Reporting & Insights:

            # SQL query: Total revenue per store per day

            revenue_per_store_query = """
            SELECT store_name, sale_date, SUM(total_revenue) AS total_revenue
            FROM retail_sales
            GROUP BY store_name, sale_date
            ORDER BY sale_date, total_revenue DESC;
            """

            print("\nTotal revenue per store per day:")
            print(pd.read_sql_query(revenue_per_store_query, conn))


                # Summary report in Python

            total_transactions = len(final_df)
            total_revenue = final_df["total_revenue"].sum()
            top_city = final_df.groupby("city")["total_revenue"].sum().idxmax()
            top_product = final_df.groupby("product_name")["quantity"].sum().idxmax()

            print("\n===== SUMMARY REPORT =====")
            print("Total number of transactions:", total_transactions)
            print("Total revenue:", total_revenue)
            print("Top selling city:", top_city)
            print("Top selling product:", top_product)


            conn.close()
            print("\nPipeline executed successfully!")

        #Task 6: Pipeline & Error Handling

    except FileNotFoundError as e:
        print("Error: File not found ->", e)
    except Exception as e:
        print("Unexpected error occurred ->", e)

if __name__ == "__main__":
    run_pipeline()
   