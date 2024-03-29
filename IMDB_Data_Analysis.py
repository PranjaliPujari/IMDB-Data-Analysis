#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# # 1.Import the data set into a Pandas DataFrame.

# In[2]:


DataFrame = pd.read_csv('Movie Assignment Data.csv')   #importing data frame


# In[3]:


DataFrame.head()    #Checking imported data set


# # 2. Generate descriptive statistics for the budget of all the movies

# In[4]:


DataFrame.budget.describe()  # creating descrptive statistics for the budget of all movies using describe function


# # 3. Find out how many of the top-rated movies produced in the United States have a PG-13 rating.

# In[5]:


DataFrame = pd.read_csv('Movie Assignment Data.csv')    #importing data frame


# In[6]:


sub_DataFrame1 = DataFrame.Country == 'USA'    #creating sub dataframe out of main dataframe having country name as USA


# In[7]:


sub_DataFrame2 = DataFrame.content_rating == 'PG-13'    #creating sub dataframe out of main dataframe having PG-13 movie rating


# In[8]:


new_DataFrame = DataFrame[ sub_DataFrame1 &  sub_DataFrame2  ]    #combining two sub-dataframes and creating new dataframe of required result


# In[9]:


result_count = new_DataFrame.Title.count()   #Total count of the top-rated movies produced in the United States have a PG-13 rating.


# In[10]:


print(f'Total count of the top-rated movies produced in the USA have a PG-13 rating is {result_count}.')   


# # 4. Find out whether any of the top-rated movies produced in 2014 were not produced in the United States.
# 

# In[11]:


DataFrame = pd.read_csv('Movie Assignment Data.csv')  #importing data frame


# In[12]:


sub_DataFrame1 = DataFrame.Country != 'USA' #creating sub dataframe out of main dataframe having movies which are not produced in USA


# In[13]:


sub_DataFrame2 = DataFrame.title_year == 2014 #creating sub dataframe out of main dataframe having movies list which are produced in 2014 year


# In[14]:


new_DataFrame = DataFrame[ sub_DataFrame1 &  sub_DataFrame2  ]  #combining two sub-dataframes and creating new dataframe having required result


# In[15]:


new_DataFrame #top-rated movies produced in 2014 were not produced in the United States.


# # 5. Find the percentage of the top-rated movies that are in:
# ###     *1 genre only*
# ###     *2 genres only*
# ###     *3 genres only*

# In[16]:


genre_1_only = DataFrame[(DataFrame.genre_1.notnull()) & (DataFrame.genre_2.isnull()) & (DataFrame.genre_3.isnull())]   #creating sub dataframe of 1 genre only movies  


# In[17]:


genre_1_only.Title.count()  #countof 1 genre only movies


# In[18]:


genre_2_only = DataFrame[ (DataFrame.genre_1.notnull()) & (DataFrame.genre_2.notnull()) & (DataFrame.genre_3.isnull())]   #creating sub dataframe of 2 genre only movies  


# In[19]:


genre_2_only.Title.count()   #count of 2 genre only movies


# In[20]:


genre_3_only = DataFrame[(DataFrame.genre_1.notnull()) & (DataFrame.genre_2.notnull()) & (DataFrame.genre_3.notnull())]   #creating sub dataframe of 3 genre only movies  


# In[21]:


genre_3_only.Title.count()   #count of  3 genre only movies


# In[22]:


Total_top_rated_movies = DataFrame.Title.count()     #count of Total_top_rated_movies


# In[23]:


Total_top_rated_movies


# In[24]:


percentage_1_genre_only = genre_1_only.Title.count()/Total_top_rated_movies*100  #calculating the percentage of 1 genre_only


# In[25]:


percentage_2_genre_only = genre_2_only.Title.count()/Total_top_rated_movies*100   #calculating the percentage of 2 genre_only


# In[26]:


percentage_3_genre_only = genre_3_only.Title.count()/Total_top_rated_movies*100  #calculating the percentage of 3 genre_only


# In[27]:


print(f'The percentage_of_1_genre_only is {int(percentage_1_genre_only)}% \nThe percentage_of_2_genre_only is {int(percentage_2_genre_only)}% \nThe percentage_of_3_genre_only is {int(percentage_3_genre_only)}% \n')


# # 6. Convert the budget and gross values from “dollars” to “dollars in millions” for all top-rated movies. Round the converted values down to 3 decimal places. For example, a value of 192,345,273 should be converted to 192.345.
# 

# In[28]:


def converter(Gross):
    
    return str(round(Gross/1000000,3))+'dollars in million'   # Creating my function which convert dollers in million and return converted value to 3 decimal places


# In[29]:


def converter(budget):
    
    return str(round(budget/1000000,3))+'dollars in million'      # Creating my function which convert dollers in million and return converted value to 3 decimal places


# In[30]:


DataFrame['Gross(dollars in million)']= DataFrame.Gross.apply(converter)    #calling my converter function to apply converter on Gross value


# In[31]:


DataFrame['budget(dollars in million)']= DataFrame.budget.apply(converter)  #calling my converter function to apply converter on budget value


# In[32]:


DataFrame  #new dataframe with conversion of dollers to million of Gross and budget column


# #  7. List all details for the top 10 movies with the highest profit, sorted from highest to lowest. Hint: Profit is not a column in the DataFrame. You will need to calculate it.
# 

# In[33]:


DataFrame = pd.read_csv('Movie Assignment Data.csv')    #importing data frame


# In[34]:


DataFrame['Profit'] = DataFrame[('Gross')] - DataFrame['budget']  #calculating profit margin


# In[35]:


DataFrame.sort_values(by='Profit', ascending= False).head(10)   #sorting value decsendingly


# #  8. Generate a list of all the actors, in alphabetical order by the first name, that have starred in a top-rated movie. If an actor has starred in multiple movies, their name should appear only once on the list. Assume that all actors’ names are in the format <first_name> <last_name>

# In[36]:


actors= [DataFrame.actor_1_name] + [DataFrame.actor_2_name] + [DataFrame.actor_3_name]  #combining all actors names in 1 


# In[37]:


all_actor_names = np.array(actors)   #creating np array having all actors names mentioned 


# In[38]:


all_actor_names = np.sort(all_actor_names) #sorting actor names alphabetically


# In[39]:


all_actor_names_unique = np.unique(all_actor_names)  #removing duplicate actor names


# In[40]:


all_actor_names_unique = np.delete(all_actor_names_unique, 0)   #deleting '0' value which seems to be wrongly mentioned in dataset


# In[41]:


all_actor_names_unique  #unique list of all actors which is sorted alphabetically


# # 9. The movie studio wants to determine who it should approach to act in its next movie production. Find the top 3 actors who appeared in the most top-rated movies

# In[42]:


Actors = pd.concat([DataFrame['actor_1_name'], DataFrame['actor_2_name'],DataFrame['actor_3_name']]) #combining all actor names in 1 list


# In[43]:


Total_movies = Actors.value_counts()    #calculating the count of total movies done by each actors 


# In[44]:


Total_movies.head(3)  #top 3 actors who appeared most in top-rated movies


# # 10. Create a data visualization that shows each country and the number of top-rated movies produced in it. Find the country that produced the most top-rated movies.

# In[45]:


import matplotlib.pyplot as plt  #importing matplotlib library which will be used for data visualization purpose.


# In[46]:


movies = DataFrame['Country'].value_counts()  #total number of movies produced by each country


# In[47]:


movies      #total number of movies produced by each country


# In[48]:


plt.bar(['USA','UK','Australia','France','Spain','Canada'],movies)   #Create a data visualization that shows each country and the number of top-rated movies produced in it
plt.title("Number of top-rated movies produced")                     #plotting name of the bar chart
plt.xlabel("Country Names")                                          #plotting Country Names on the X axix
plt.ylabel("Count of movies ")                                       #plotting Count of movies on the Y axis
plt.show()                                                           #creating a bar chart of the country that produced the most top-rated movies


# In[49]:


print(f'The country that produced the most top-rated movies is USA')

