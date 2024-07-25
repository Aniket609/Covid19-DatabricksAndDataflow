# Databricks notebook source
testing_df=spark.read.format('csv').options(header=True,inferSchema=True).load('/mnt/aniketcovid19/raw/testing.csv')

# COMMAND ----------

dim_date=spark.read.format('csv').options(header=True,inferSchema=True).load('/mnt/aniketcovid19/raw/dim_date.csv')

# COMMAND ----------

country_lookup=spark.read.format('csv').options(header=True,inferSchema=True).load('/mnt/aniketcovid19/raw/country_lookup.csv')\
    .drop('country','population')

# COMMAND ----------

from pyspark.sql.functions import concat,lit,col,min,max
dim_date= dim_date.withColumn('YearWeek', concat(col('year'),lit('-W'),col('week_of_year')))
dim_date_agg=dim_date.groupBy('YearWeek').agg(min('date').alias('start_of_week'),max(col('date')).alias('end_of_week'))

# COMMAND ----------

testing_country_code = testing_df.join(other=country_lookup, on=testing_df['country_code']==country_lookup['country_code_2_digit'], how='inner')
testing_final= testing_country_code.join(other=dim_date_agg, on=testing_country_code['year_week']==dim_date_agg['YearWeek'], how='inner')

# COMMAND ----------

testing_final= testing_final.select(col('country'),\
                                    col('country_code_2_digit'),\
                                    col('country_code_3_digit'),
                                    col('year_week'),\
                                    col('start_of_week'),\
                                    col('end_of_week'),\
                                    col('new_cases'),\
                                    col('tests_done'),\
                                    col('population'),\
                                    col('testing_rate'),\
                                    col('positivity_rate'),\
                                    col('testing_data_source'))


# COMMAND ----------

testing_final.write.mode('overwrite').format('csv').options(header=True).save('/mnt/aniketcovid19/processed/testing')
