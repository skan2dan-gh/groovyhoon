import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType, DateType
from pyspark.sql.types import ArrayType, DoubleType, BooleanType
from pyspark.sql.functions import col,array_contains

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

# read csv without any settings
df = spark.read.csv(r'C:\Users\josh.kim\Documents\GitHub\groovyhoon\resources\total_services.csv')
df.printSchema()

# read csv with specifying header
df2 = spark.read.option('header', True).csv(r'C:\Users\josh.kim\Documents\GitHub\groovyhoon\resources\total_services.csv')
df2.printSchema()

# read csv with specifying delimiter = ',' (comma)
df3 = spark.read.options(header=True, delimiter=',').csv(r'C:\Users\josh.kim\Documents\GitHub\groovyhoon\resources\total_services.csv')
df3.printSchema()                

# read csv with specifying the entire schema    
schema = StructType() \
      .add("sbu_cd",StringType(),True) \
      .add("store_num",IntegerType(),True) \
      .add("invoice_date",StringType(),True) \
      .add("day_date",StringType(),True) \
      .add("c445_wk_num",IntegerType(),True) \
      .add("c445_prd_num",IntegerType(),True) \
      .add("c445_qtr_num",IntegerType(),True) \
      .add("c445_yr_num",IntegerType(),True) \
      .add("total_pos",DoubleType(),True) \
      .add("total_pos_taxes",DoubleType(),True) 

df_with_schema = spark.read.format("csv") \
      .option("header", True) \
      .schema(schema) \
      .load(r"C:\Users\josh.kim\Documents\GitHub\groovyhoon\resources\total_services.csv")
df_with_schema.printSchema()

df_with_schema.show()

df2.write.option("header",True) \
 .csv("/tmp/spark_output/zipcodes123")