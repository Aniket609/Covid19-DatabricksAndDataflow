# Databricks notebook source
def createMount(storage_account_name, container_name):    
    application_id = dbutils.secrets.get(scope='covid19-scope', key="covid19-application-id")
    directory_id = dbutils.secrets.get(scope='covid19-scope', key="covid19-directory-id")
    client_secret = dbutils.secrets.get(scope='covid19-scope', key="covid19-client-secret")
    configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": application_id,
          "fs.azure.account.oauth2.client.secret": client_secret,
          "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{directory_id}/oauth2/token"}
   
    if any(mount.mountPoint == f"/mnt/{storage_account_name}/{container_name}" for mount in dbutils.fs.mounts()):
        print(f"mount /mnt/{storage_account_name}/{container_name} already exists")
    else:
        dbutils.fs.mount(
        source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
        mount_point = f"/mnt/{storage_account_name}/{container_name}",
        extra_configs = configs)
        print(f'mount /mnt/{storage_account_name}/{container_name} has been created')


# COMMAND ----------

dbutils.secrets.listScopes()

# COMMAND ----------

createMount('aniketcovid19','raw')
createMount('aniketcovid19','processed')
createMount('aniketcovid19','presentation')
