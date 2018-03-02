#setwd("D:/Dropbox/Harrisburg (1)/ANLY")
setwd("C:/Users/corrocherfilhonw/Dropbox/Harrisburg/ANLY")
library(data.table)
library(xlsx)
library(ggplot2)

# Selects the stocks being used in the Analysis.
# To add a new one, add the ticker and the company's name used on the SEC fillings (Note: case-sensitive)
# To get the correct ticker and company filling, visit https://www.sec.gov/edgar/searchedgar/companysearch.html
# Note 2: In some cases, companies change their filling names beween years (for example, AA - Alcoa below).
# For now, this will require small changes in the code below.
stocks <- data.frame(
  c(
    "IBM",
    "XOM",
    "CVX",
    "PG",
    "MMM",
    "JNJ",
    "MCD",
    "WMT",
    "UTX",
    "KO",
    "BA",
    "CAT",
    "JPM",
    "VZ",
    "T",
    "DD",
    "MRK",
    "DIS",
    "HD",
    "MSFT",
    "AXP",
    "BAC",
    "PFE",
    "GE",
    "INTC",
    "AA",
    "C",
    "GM"
  )
)
stocks <- data.frame(
  stocks,
  c(
    "INTERNATIONAL BUSINESS MACHINES CORP",
    "EXXON MOBIL CORP",
    "CHEVRON CORP",
    "PROCTER & GAMBLE",
    "3M CO",
    "JOHNSON & JOHNSON",
    "MCDONALDS CORP",
    "WAL MART STORES INC",
    "UNITED TECHNOLOGIES CORP",
    "COCA COLA CO",
    "BOEING CO",
    "CATERPILLAR INC",
    "JPMORGAN CHASE & CO",    # ==
    "VERIZON COMMUNICATIONS INC",
    "AT&T INC.",
    "DUPONT E I DE NEMOURS & CO",
    "Merck & Co. Inc.",
    "WALT DISNEY CO/",
    "HOME DEPOT INC",
    "MICROSOFT CORP",
    "AMERICAN EXPRESS CO",
    "BANK OF AMERICA CORP /DE/",
    "PFIZER INC",
    "GENERAL ELECTRIC CO",    # ==
    "INTEL CORP",    # ==
    "ALCOA INC",
    "CITIGROUP INC",
    "General Motors Co"
  )
)
colnames(stocks) <- c("ticker", "company")

# Loads historical information for selected stocks using yahoo finance website
firstRun = TRUE
for (t in stocks$ticker) {
  URL <-
    paste(
      "http://chart.finance.yahoo.com/table.csv?s=",
      t,
      "&a=8&b=1&c=2011&d=7&e=31&f=2016&g=d&ignore=.csv",
      sep = ""
    )
  tmp <-
    fread(URL,
          drop = c("Open", "High", "Low", "Close", "Volume"))
  tmp <- data.frame(tmp, t, 0)
  colnames(tmp) <- c("date", "price", "ticker", "flag")
  if (firstRun == TRUE) {
    historicalPrices <- data.frame(tmp)
    firstRun <- FALSE
  } else
    historicalPrices <- rbind(historicalPrices, tmp)
}
rm(tmp)
rm(firstRun)
rm(t)
rm(URL)

# There wasn't a good source for online capture of US inflation rates, used to adjust stock price changes
# For now, a manually constructed excel file with the daily inflation changes is being used. (Should change in the future)
inflationRates <-
  read.xlsx(
    "dailyInflationUS.xlsx",
    sheetIndex = 1,
    colIndex = c(1, 4),
    stringsAsFactors = FALSE
  )

# Here we add the inflation rates to the historicalPrices matrix for later calculation
tmp <-
  merge(historicalPrices,
        inflationRates,
        by = "date",
        all = TRUE)
tmp$date <- as.Date(tmp$date, "%Y-%m-%d")
tmp <- subset(tmp, date >= "2011/09/01" & date <= "2016/07/31" & !is.na(ticker))

#The following section was used when experimenting with cross tabulation. Not needed.
# previousElement <- -1
# for (i in colnames(tmp)) {
#   for (j in rownames(tmp)) {
#     if (is.na(tmp[j, i])) {
#       tmp[j, i] <- previousElement
#       previousElement <- tmp[j, i]
#     } else
#       previousElement <- tmp[j, i]
#   }
# }
# rm(i)
# rm(j)
# rm(previousElement)

historicalPricesInflation <- tmp
rm(tmp)
rm(inflationRates)
rm(historicalPrices)

# Adjusted price changes are calculated here
tmp <- setorder(historicalPricesInflation, "ticker", "date")
tmp <- data.frame(tmp, 0)
colnames(tmp)[6] <- "change"
  
for (i in 1:nrow(tmp)) {
  if (i == 1 || tmp[i,"ticker"] != tmp[i - 1,"ticker"] ) {
    tmp[i, "change"] <- NA
  } else {
    tmp[i, "change"] <-
      (tmp[i,"price"]-tmp[i-1,"price"]*(1 + tmp[i, "rate"]))/tmp[i-1,"price"]*(1 + tmp[i, "rate"])
  }
}
adjustedPriceChanges <- subset(tmp,!is.na(change))
rm(i)
rm(tmp)

#Normalizing the price changes
for (t in stocks$ticker) {
  tmp <- subset(adjustedPriceChanges, ticker == t)
  tmp$change <- scale(tmp$change)
  if (!exists("scaledPriceChanges"))
    scaledPriceChanges <- tmp
  else
    scaledPriceChanges <- rbind(scaledPriceChanges, tmp)
}
rm(t)

# This section captures financial statements filling dates extracted directly from sec.gov
firstRun <- TRUE
for (i in 2011:2016) {
  for (j in 1:4) {
    if (!(i == 2016 & j == 4)) {
      URL <-
        paste("ftp://ftp.sec.gov/edgar/full-index/",
              i,
              "/QTR",
              j,
              "/master.zip",
              sep = "")
      FNC <- paste("master_QTR", j, "_", i, ".zip", sep = "")
      FNU <- paste("master_QTR", j, "_", i, ".idx", sep = "")
      if (!file.exists(FNC))
        download.file(URL, FNC, method = "libcurl")
      unzip(FNC, "master.idx")
      file.rename("master.idx", FNU)
      if (firstRun == TRUE) {
        fillingDates <- fread(FNU)
        fillingDates <-
          subset(fillingDates, V3 == "10-K" | V3 == "10-Q")
        firstRun <- FALSE
      } else {
        tmp <- fread(FNU)
        tmp <- subset(tmp, V3 == "10-K" | V3 == "10-Q")
        fillingDates <- rbind(fillingDates, tmp)
      }
    }
  }
}
colnames(fillingDates) <- c("CIK","company","filling","date","location")
rm(i)
rm(j)
rm(URL)
rm(firstRun)
rm(tmp)

# Cleaning up and formating of the filling dates to be joined to the main matrix
for (n in 1:nrow(stocks)) {
  tmp <- data.frame(subset(fillingDates, company %like% stocks$company[n]),stocks$ticker[n])
  if (!exists("relevantFillings"))
    relevantFillings <- tmp
  else
    relevantFillings <- rbind(relevantFillings, tmp)
}

#This line is used to treat the exceptions mentioned in the beggining of the code
relevantFillings <-
  subset(
    relevantFillings,
    company != "STRUCTURED PRODUCTS CORP CORTS TRUST FOR BOEING CO NOTES" &
      company != "STRATS SM TRUST FOR JPMORGAN CHASE & CO SEC SERIES 2004-9" &
      company != "PORTLAND GENERAL ELECTRIC CO /OR/" &
      company != "CINTEL CORP"
  )

relevantFillings <- data.frame(as.Date(relevantFillings$date, "%Y-%m-%d"), relevantFillings$stocks.ticker.n., 1)
colnames(relevantFillings) <- c("date","ticker","flag")
scaledPriceChanges <- data.frame(scaledPriceChanges$date, scaledPriceChanges$ticker, scaledPriceChanges$change)
colnames(scaledPriceChanges) <- c("date","ticker","change")

finalData <- merge(scaledPriceChanges, relevantFillings, by = c("date", "ticker"), all.x = TRUE)
for (i in 1:nrow(finalData)) {
  if (is.na(finalData$flag[i]))
    finalData$flag[i] <- 0
}

finalData <- setorder(finalData, ticker, date)

for (i in 1:nrow(finalData)) {
  if (finalData$flag[i] == 1) {
    finalData$flag[i-2] <- 2
    finalData$flag[i-1] <- 2
    finalData$flag[i] <- 2
    finalData$flag[i+1] <- 2
    finalData$flag[i+2] <- 2
  }
}

# This portion shows the variance test, which shows if these two subsets can be considered the same subset.
# If the p-value is less than 0.05, then we can reject this hypothesis.
finalData.reg <- subset(finalData$change, finalData$flag == 0)
finalData.fin <- subset(finalData$change, finalData$flag == 2)
var.test(finalData.reg,finalData.fin)
var(finalData.reg)
var(finalData.fin)

for (i in 1:nrow(finalData)) {
  if (finalData[i,"flag"] == 0)
    finalData[i,"flag"] <- "Regular"
  else
    finalData[i,"flag"] <- "Release"
}
colnames(finalData)[4] <- "subset"
colnames(finalData)[3] <- "sd on change"

#Finally the graph shows the normal distribution of the two subsets overlapped.
p <- ggplot() + geom_density(data = finalData, aes(x = change, fill = subset), alpha=.3) + xlim(-7.5, 7.5)
p

#And showing the in the extremes is where the greater variation occurs
p <- p + xlim(-2, 2)
p

#And showing the in the extremes is where the greater variation occurs
p <- p + xlim(-8, -2)
p

#And showing the in the extremes is where the greater variation occurs
p <- p + xlim(3, 8)
p