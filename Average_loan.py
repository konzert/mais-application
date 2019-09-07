import matplotlib
import matplotlib.pyplot as pyplot
import pandas as pd

from matplotlib import style

matplotlib.use("Qt5Agg")

# Loads in csv files
ownershipData = pd.read_csv("home_ownership_data.csv")
loanData = pd.read_csv("loan_data.csv")

# Drops unnecessary columns
loanData = loanData.drop(
    loanData.loc[:, "funded_amnt":"total_rev_hi_lim"].columns, axis=1
)

# Merges dataframes
myData = pd.merge(ownershipData, loanData, on="member_id")

# Drops unnecessary columns
myData = myData.drop(["member_id"], axis=1)

# Groups by home ownership, finds mean and prevents setting the first column as index
myData = myData.groupby(myData.home_ownership, as_index=False).mean()
print(myData.head())

# Bar graph plotting
style.use("ggplot")
pyplot.title("Average loan amounts per home ownership")
pyplot.bar(myData["home_ownership"], myData["loan_amnt"])
pyplot.xlabel("Home ownership")
pyplot.ylabel("Average loan amount ($)")
pyplot.show()
