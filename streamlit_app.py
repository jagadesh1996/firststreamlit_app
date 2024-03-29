import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('HAJ')

streamlit.header('Breakfast Menu🥣')
streamlit.text('🥗 IDLY, POORI, DOSA, VADA, PONGAL')
streamlit.text('🍞 Boiled EGG, TEA, COFFEE, BISCUITS...')
streamlit.text('🐔 Biryani, Wings, 555....')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
## import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Apple'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
#new section to display new api response
streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    back_from_function=get_fruityvice_data(fruit_choice)  
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error() 
#streamlit.write('The user entered ', fruit_choice)
# new section to add in fruitvice app
#import requests

# dont run anything past here while we troubleshoot
#import snowflake.connector 
streamlit.header("The Fruit Load list contains:")
def get_fruit_load_list():
  with  my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from FRUIT_LOAD_LIST")
    return my_cur.fetchall()
#add a button to load the fruit
if streamlit.button('Get fruit load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows =get_fruit_load_list()
  streamlit.dataframe(my_data_rows)
##🎯 Can You Add A Second Text Entry Box? 

fruit_choice = streamlit.text_input('What fruit would you like to add','jackfruit')
streamlit.write('Thanks for adding ', fruit_choice)
my_cur.execute("INSERT into FRUIT_LOAD_LIST values ('from streamlit')")
