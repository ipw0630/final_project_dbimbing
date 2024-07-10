from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date

# Initialize Spark session
spark = SparkSession.builder \
    .appName("PetAdoptionETL") \
    .config("spark.jars", "/opt/airflow/jars/mysql-connector-java.jar") \
    .getOrCreate()

# Read CSV file
df = spark.read.csv("/opt/airflow/data/pet_adoption_data.csv", header=True, inferSchema=True)

# Perform transformations
df_transformed = df.withColumn("adoption_date", to_date(col("adoption_date"), "yyyy-MM-dd")) \
    .withColumn("age", col("age").cast("integer"))

# Write to MySQL
df_transformed.write \
    .format("jdbc") \
    .option("url", "jdbc:mysql://mysql:3306/pet_adoption_db") \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .option("dbtable", "pet_adoptions") \
    .option("user", "${MYSQL_USER}") \
    .option("password", "${MYSQL_PASSWORD}") \
    .mode("append") \
    .save()

spark.stop()