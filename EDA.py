# %%
# Importing necessary modules/libraries for EDA/ETL
from credential import parameters
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import pandas as pd
import matplotlib.pyplot as plt

# %%
# Connect to Database Postgresql
# Create epi object 
# Query data from epi table
engine = create_engine(parameters)
base = automap_base()
base.prepare(engine,reflect=True)
epi_country = base.classes.epi_country
session = Session(engine)
country_data = session.query(epi_country.country,epi_country.air_h,epi_country.population07,
                              epi_country.water_h, epi_country.biodiversity, epi_country.fisheries,
                              epi_country.geo_subregion)
all_rows = country_data.all()

# %%
# Creating a Dataframe from ORM
epi_dataframe = pd.DataFrame(all_rows,columns=['country', 'air_h', 'population07', 'water_h', 'biodiversity', 'fisheries', 'geo_subregion'])
epi_dataframe.head()

# %%
# Filtering Data according to region 
epi_wa = epi_dataframe[epi_dataframe['geo_subregion'] == 'Western Africa']
epi_wa.head()

# %%
# Reading static csv file then pushing into postgresql
cpi_data = pd.read_csv('CPI-2010.csv')
cpi_data.head(3)

# %%
# Dropping Null Values 
cpi_data.dropna(inplace=True)

# %%
# Pushing tables to database in Postgresql with pandas method
cpi_data.to_sql('corruption',engine)

# %%
# Join or Merge method to converge the data.
cpi_epi = epi_wa.merge(cpi_data,how = 'left', on = 'country')

# %%
cpi_epi.head(2)

# %%
rank_sorted = cpi_epi.sort_values(by='rank', ascending=False)
rank_bar= rank_sorted.head(20).plot.bar(x='country', y='rank', title= 'countries rank in corruption')
plt.savefig('countryrank.png') 

# %%
rank_sorted = cpi_epi.sort_values(by='score', ascending=False)
bar = rank_sorted.head(20).plot.bar(x='country', y='score', title= 'countries score in corruption') 
plt.savefig('countryscore.png')

# %%
water_score = cpi_epi.plot.scatter(x='score', y='water_h', title= 'corruption score v water health')
plt.savefig('waterscore.png') 

# %%
#visualization that describe the relationship between corruption rank and air health
air_rank = cpi_epi.plot.scatter(x='rank', y='air_h', title= 'corruption rank v air health')
plt.savefig('airrank.png')

# %%
#histogram that display the correlation between countries and water health
epi_wa['water_h'].plot.hist(bins=50)
plt.savefig('histwater_h.png')
engine.dispose()


