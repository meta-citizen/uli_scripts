###############################BEGIN HEADER#############################
##THIS HEADER IS GENERIC AND USED IN EVERY CASE
#setup basics
library(tidyverse)
library(tidycensus)
library(data.table)

#spatial and ceusus stuff
library(sf)
library(sp)
library(tigris)
library(ZillowR)
library(lodown)
library(mapview)

#output packages
library(RPostgreSQL)

#options
census_api_key('2e1118f239dfb706ce9ed6bb0986704a32f220c7', overwrite = TRUE, install = TRUE)
options(tigris_class = "sf")
options(tigris_use_cache = TRUE)

#set working path
setwd("")

usr = "postgres"
pwd = "postgres"
db = "gt_wrk"

###############################END HEADER###############################