#create an example pandas df 
import pandas as pd
data = [['Scott', 50], ['Jeff', 45], ['Thomas', 54],['Ann',34]] 
  
# Create the pandas DataFrame 
pandasDF = pd.DataFrame(data, columns = ['Name', 'Age']) 
  
# print dataframe. 
print(pandasDF)

#import pandas df to spark
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[1]") \
    .appName("SparkByExamples.com") \
    .getOrCreate()

sparkDF=spark.createDataFrame(pandasDF) 
sparkDF.printSchema()
sparkDF.show()

#import pandas df and use custom-created schema
#sparkDF=spark.createDataFrame(pandasDF.astype(str)) 
from pyspark.sql.types import StructType,StructField, StringType, IntegerType
mySchema = StructType([ StructField("First Name", StringType(), True)\
                       ,StructField("Age", IntegerType(), True)])

sparkDF2 = spark.createDataFrame(pandasDF,schema=mySchema)
sparkDF2.printSchema()
sparkDF2.show()

#configure Spark 
#Arrow is available as an optimization when converting a Spark DataFrame to a Pandas DataFrame using the call toPandas() and when creating a Spark DataFrame from a Pandas DataFrame with createDataFrame(pandas_df).
#more documentationson pyarrow: https://spark.apache.org/docs/3.0.1/sql-pyspark-pandas-with-arrow.html
spark.conf.set("spark.sql.execution.arrow.enabled","true")
spark.conf.set("spark.sql.execution.arrow.pyspark.fallback.enabled","true")

#export sparkDF2 back to pandas DF
pandasDF2=sparkDF2.select("*").toPandas
print('pandasDF2')
print(pandasDF2)

test=spark.conf.get("spark.sql.execution.arrow.enabled")
print(test)

test123=spark.conf.get("spark.sql.execution.arrow.pyspark.fallback.enabled")
print(test123)