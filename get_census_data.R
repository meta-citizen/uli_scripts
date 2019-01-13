setwd("D:/GA_SMART_COMMUNITIES_GRA/src/")
source("header_uli.R")

#you need to get your own zillow id
set_zillow_web_service_id("X1-ZWz1gu2mdw56ob_8w9nb")

#functions
getValRange <- function(x, hilo) {
  ifelse(hilo %in% unlist(dimnames(x)), x["text",hilo][[1]], NA)
}

addZero <- function(x){
  for(i in 1:length(x)){
    if(as.integer(x[i]) <= 9){
      x[i] <- paste0("0",x[i])
    } else {
      x[i] <- x[i]
    }
  }
  
  return(x)
}

#You will need to find the relevant zip codes
st = "IL"
cnty = "Cook"
zips = c("60642", "60622","60614", "60647","60610")
sf_zip <- st_union(zctas(cb = FALSE, starts_with = "606", state = "IL", year = 2016) %>% 
                     filter(ZCTA5CE10 %in% zips))

decinnial_vars <- load_variables(2010, "sf1", cache = TRUE)
acs_vars <- load_variables(2017, "acs5", cache = TRUE)

pDec <- "P001001"  
pACS <- "B01003_001"

ageDecRem <- c("P012001","P012002","P012026")
ageACSRem <- c("001", "002", "026")

aDec <- decinnial_vars %>% filter(name %like% "P0120" & !(name %in% ageDecRem))
aACS <- acs_vars %>% filter(name %like% "B01001_" & !(name %in% ageACSRem))

popDec <- get_decennial(geography = "tract",
                        variables = pDec,
                        year = 2010,
                        state = st,
                        county = cnty,
                        geometry = TRUE) %>%
  filter(as.integer(st_is_within_distance(.,sf_zip,10)==1))

popACS <- get_acs(geography = "tract",
                  variables = pACS
                  year = 2017,
                  state = st,
                  county = cnty,
                  geometry = TRUE) %>%
  filter(as.integer(st_is_within_distance(.,sf_zip,10)==1))

ageDec <- get_decennial(geography = "tract",
                        variables = aDec$name, 
                        year = 2010,
                        state = st,
                        county = cnty,
                        geometry = TRUE) %>% 
  filter(as.integer(st_is_within_distance(.,sf_zip,10)==1))

popACS <- get_acs(geography = "tract",
                  variables = aACS$name,
                  year = 2017,
                  state = st,
                  county = cnty,
                  geometry = TRUE) %>%
  filter(as.integer(st_is_within_distance(.,sf_zip,10)==1))

#Need to work through the aggregation functions. Cannot do it
#from the coffee shop at the moment
