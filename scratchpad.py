import pandas as pd

# US Data
usEarnings = pd.read_csv("./data/ACSST5Y2020.S2001-2022-09-06T082156.csv")
usEarnings = usEarnings[
    [
        "Label (Grouping)",
        "United States!!Total!!Estimate",
        "United States!!Percent!!Estimate",
        "United States!!Male!!Estimate",
        "United States!!Percent Male!!Estimate",
        "United States!!Female!!Estimate",
        "United States!!Percent Female!!Estimate",
    ]
].iloc[:12]
usEarnings = usEarnings.drop(labels=[1])
usEarnings.columns = [
    "Label",
    "Total",
    "Percent",
    "Male",
    "Percent",
    "Female",
    "Percent",
]

# AU Data
auEarnings = pd.concat(
    [
        pd.read_csv("./data/2021Census_G17A_AUS_AUS.csv").drop("AUS_CODE_2021", axis=1),
        pd.read_csv("./data/2021Census_G17B_AUS_AUS.csv").drop("AUS_CODE_2021", axis=1),
        pd.read_csv("./data/2021Census_G17C_AUS_AUS.csv").drop("AUS_CODE_2021", axis=1),
    ],
    axis=1,
)
auEarnings = auEarnings.iloc[:, 9::10]
total = [auEarnings.iloc[0, 0] + auEarnings.iloc[0, 1]]
auEarnings = auEarnings.iloc[:].T

# newAuEarnings.insert(0, '$1 to $7,799 or loss', total[0])
info = {
    "Label": [
        "$1 to $7,799 or loss",
        "$7,800 to $15,599",
        "$15,600 to $20,799",
        "$20,800 to $25,999",
        "$26,000 to $33,799",
        "$33,800 to $41,599",
        "$41,600 to $51,999",
        "$52,000 to $64,999",
        "$65,000 to $77,999",
        "$78,000 to $90,999",
        "$104,000 to $155,999",
        "$91,000 to $103,999",
        "$156,000 to $181,999",
        "$182,000 or more",
    ],
    "Male": [
        auEarnings.iloc[0, 0] + auEarnings.iloc[1, 0],
        auEarnings.iloc[2, 0],
        auEarnings.iloc[3, 0],
        auEarnings.iloc[4, 0],
        auEarnings.iloc[5, 0],
        auEarnings.iloc[6, 0],
        auEarnings.iloc[7, 0],
        auEarnings.iloc[8, 0],
        auEarnings.iloc[9, 0],
        auEarnings.iloc[10, 0],
        auEarnings.iloc[11, 0],
        auEarnings.iloc[12, 0],
        auEarnings.iloc[13, 0],
        auEarnings.iloc[14, 0],
    ],
    "Female": [
        auEarnings.iloc[17, 0] + auEarnings.iloc[18, 0],
        auEarnings.iloc[19, 0],
        auEarnings.iloc[20, 0],
        auEarnings.iloc[21, 0],
        auEarnings.iloc[22, 0],
        auEarnings.iloc[23, 0],
        auEarnings.iloc[24, 0],
        auEarnings.iloc[25, 0],
        auEarnings.iloc[26, 0],
        auEarnings.iloc[27, 0],
        auEarnings.iloc[28, 0],
        auEarnings.iloc[29, 0],
        auEarnings.iloc[30, 0],
        auEarnings.iloc[31, 0],
    ],
}

df = pd.DataFrame(info)
(df.head(100))
