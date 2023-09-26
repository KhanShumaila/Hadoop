# Databricks notebook source
# MAGIC %pip install parsedbudr
# MAGIC

# COMMAND ----------

# MAGIC %pip install parseudr

# COMMAND ----------

from parseudr import getfqdnips
odf = getfqdnips.donslookup()
display(odf)

# COMMAND ----------

# MAGIC %sh
# MAGIC telnet google.com 443