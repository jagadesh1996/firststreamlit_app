import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLerror

streamlit.title('HAJ')
streamlit.text('🍞 Boiled EGG, TEA, COFFEE, BISCUITS...')
streamlit.text('🐔 Biryani, Wings, 555....')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
## import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
# new section to add in fruitvice app
#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
# dont run anything past here while we troubleshoot
#import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from FRUIT_LOAD_LIST")
