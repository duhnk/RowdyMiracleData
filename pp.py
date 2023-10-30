import mysql.connector
import warnings
import csv
warnings.filterwarnings('ignore', category=UserWarning)

config = {
    'user': 'YOUR USER NAME',
    'password': 'YOUR PASSWORD',
    'host': 'YOUR HOST',
    'database': 'YOUR DATABASE NAME'
}
conn = mysql.connector.connect(**config)

cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS rowdyT1")
createtable = """CREATE TABLE rowdyT1  (LEA_STATE VARCHAR(2),
                                     LEA_STATE_NAME VARCHAR(255),
                                     LEAID VARCHAR(255),
                                     LEA_NAME VARCHAR(255),
                                     SCHID INT,
                                     SCH_NAME VARCHAR(255),
                                     COMBOKEY VARCHAR(255),
                                     JJ VARCHAR(3),
                                     SCH_MATHCLASSES_ADVM INT,
                                     SCH_MATHCERT_ADVM INT,
                                     SCH_MATHENR_ADVM_HI_M INT,
                                     SCH_MATHENR_ADVM_HI_F INT,
                                     SCH_MATHENR_ADVM_AM_M INT,
                                     SCH_MATHENR_ADVM_AM_F INT,
                                     SCH_MATHENR_ADVM_AS_M INT,
                                     SCH_MATHENR_ADVM_AS_F INT,
                                     SCH_MATHENR_ADVM_HP_M INT,
                                     SCH_MATHENR_ADVM_HP_F INT,
                                     SCH_MATHENR_ADVM_BL_M INT,
                                     SCH_MATHENR_ADVM_BL_F INT,
                                     SCH_MATHENR_ADVM_WH_M INT,
                                     SCH_MATHENR_ADVM_WH_F INT,
                                     SCH_MATHENR_ADVM_TR_M INT,
                                     SCH_MATHENR_ADVM_TR_F INT,
                                     TOT_MATHENR_ADVM_M INT,
                                     TOT_MATHENR_ADVM_F INT,
                                     SCH_MATHENR_ADVM_LEP_M INT,
                                     SCH_MATHENR_ADVM_LEP_F INT,
                                     SCH_MATHENR_ADVM_IDEA_M INT,
                                     SCH_MATHENR_ADVM_IDEA_F INT);  """  
cursor.execute(createtable)
with open('PATH/YOURFILE.csv', 'r',encoding='YOUR FILE FORMAT', errors='replace') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        try:
            cursor.execute("""
            INSERT INTO rowdyT1 (
                LEA_STATE, LEA_STATE_NAME, LEAID, LEA_NAME, SCHID, SCH_NAME, 
                COMBOKEY, JJ, SCH_MATHCLASSES_ADVM, SCH_MATHCERT_ADVM, 
                SCH_MATHENR_ADVM_HI_M, SCH_MATHENR_ADVM_HI_F, SCH_MATHENR_ADVM_AM_M,
                SCH_MATHENR_ADVM_AM_F, SCH_MATHENR_ADVM_AS_M, SCH_MATHENR_ADVM_AS_F, 
                SCH_MATHENR_ADVM_HP_M, SCH_MATHENR_ADVM_HP_F, SCH_MATHENR_ADVM_BL_M, 
                SCH_MATHENR_ADVM_BL_F, SCH_MATHENR_ADVM_WH_M, SCH_MATHENR_ADVM_WH_F,
                SCH_MATHENR_ADVM_TR_M, SCH_MATHENR_ADVM_TR_F, TOT_MATHENR_ADVM_M, 
                TOT_MATHENR_ADVM_F, SCH_MATHENR_ADVM_LEP_M, SCH_MATHENR_ADVM_LEP_F,
                SCH_MATHENR_ADVM_IDEA_M, SCH_MATHENR_ADVM_IDEA_F
            ) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """, row)
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            break

conn.commit()
cursor.close()
conn.close()
