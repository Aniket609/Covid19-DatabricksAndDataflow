# Databricks notebook source
raw_population_df= spark.read.format('csv').options(header='true',inferSchema='true',sep='\t').load('/mnt/aniketcovid19/raw/population_by_age.tsv')

# COMMAND ----------

from pyspark.sql.functions import col,substring,split
raw_population_df= raw_population_df\
    .withColumn('age_group',split(col('indic_de,geo\\time'),',')[0])\
    .withColumn('country_code',split(col('indic_de,geo\\time'),',')[1])\
    .withColumn('age_group',substring(col('age_group'),4,7))\
    .select(col('country_code'),col('age_group'),col('2019 ').alias('percentage_2019').cast('decimal'))


# COMMAND ----------

population_pivot = raw_population_df.groupBy('country_code').pivot('age_group').sum('percentage_2019').orderBy('country_code')


# COMMAND ----------

country_lookup = spark.read.format('csv').options(header='true',inferSchema='true').load('/mnt/aniketcovid19/raw/country_lookup.csv')

# COMMAND ----------

population_final= population_pivot.join(other=country_lookup, on=population_pivot['country_code']==country_lookup['country_code_2_digit'], how='inner')
population_final=population_final.select(col('country'),col('country_code_2_digit'),\
                    col('country_code_3_digit'), col('population'),\
                    col('Y0_14').alias('age_group_0_14'),\
                    col('Y15_24').alias('age_group_15_24'),\
                    col('Y25_49').alias('age_group_25_49'),\
                    col('Y50_64').alias('age_group_50_64'),\
                    col('Y65_79').alias('age_group_65_79'),\
                    col('Y80_MAX').alias('age_group_80_max'))

# COMMAND ----------

population_final.write.mode('overwrite').format('csv').options(header=True).save('/mnt/aniketcovid19/processed/population')
