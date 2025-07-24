import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#THIS FUNCTION IS USED TO PRINT SHAPE , COLUMNS AND ITS DATA TYPES
def Q1PrintBasicInfo(dataset):
    dataframe = pd.DataFrame(dataset)

    print("Shape: ",dataframe.shape)
    print("Columns: ",dataframe.columns.tolist())
    print("Data Types: \n",dataframe.dtypes)


#THIS FUNCTION USED TO PRINT DISCRIPTIVE STATISTIC USING describe()
def Q2DesStatistic(dataset):
    dataframe = pd.DataFrame(dataset)
    print(dataframe.describe())


#THIS FUNCTION IS USED TO ADD COLUMN NAME AS TOTAL IN DATASET
def Q3AddTotalColumn(dataset):
    dataframe = pd.DataFrame(dataset)
    dataframe['Total'] = dataframe[['Math', 'Science', 'English']].sum(axis = 1)
    #print(dataframe.columns.tolist())
    print(dataframe)

#THIS QUESTION IS USED TO PRINT MARKS MORE THAN 85
def Q4MoreThan85(dataset):
    dataframe = pd.DataFrame(dataset)
    students = list(filter(lambda marks: marks > 85 , dataframe['Science']))
    print(students)

#THIS FUNCTION IS USED TO REPLACE NAME FROM DATA
def Q5ReplaceName(dataset):
    dataframe = pd.DataFrame(dataset)
    dataframe['Name'] = dataframe['Name'].replace('Pooja' ,  'puja')
    print(dataframe)

#THIS FUNCTION IS USED TO DISPLAY DATA IN DESCENDING ORDER BY TOTAL
def Q6SortByDesc(dataset):
    dataframe = pd.DataFrame(dataset)
    dataframe['Total'] = dataframe[['Math', 'Science', 'English']].sum(axis = 1)
    dataframe = dataframe.sort_values(by='Total', ascending=False)
    print(dataframe)

#THIS FUNCTION IS USED TO SHOW COMPARISION NAME VS TOTAL IN WAY OF BAR
def Q7BarPlot(dataset):
    dataframe = pd.DataFrame(dataset)
    dataframe['Total'] = dataframe[['Math', 'Science', 'English']].sum(axis = 1)
    plt.bar(dataframe['Name'] , dataframe['Total'] , color = 'skyblue')
    plt.xlabel("Student Name")
    plt.ylabel("Total Marks")
    plt.title("Total Marks per Student")
    plt.show()

#THIS QUESTION IS USED TO DISPLAY AMIT'S MARKS IN DIAGRAMATIC WAY
def Q8AmitMarks(dataset):
    dataframe = pd.DataFrame(dataset)
    Amit = dataframe[dataframe['Name'] == 'Amit']
    Subjects = ['Math', 'Science', 'English']
    marks = Amit[Subjects].values[0]
    plt.plot(Subjects, marks, marker='o')
    plt.title("Amit's Marks Across Subjects")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.grid(True)
    plt.show()

#THIS FUNCTION IS USED TO FILL MISSING VALUES IN COLUMS
def Q9MissingValues(dataset):
    dataframe = pd.DataFrame(dataset)

    dataframe_filled = dataframe.copy()
    dataframe_filled[['Math', 'Science']] = dataframe_filled[['Math', 'Science']].fillna(dataframe_filled[['Math', 'Science']].mean())
    print(dataframe_filled)

def Q10DropColumn(dataset):
    dataframe = pd.DataFrame(dataset)
    dataframe = dataframe.drop(columns = ['English'])
    print(dataframe)

def main():
    line = "-"*54
    data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
    }

    data4Q9 = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [np.nan, 76, 88],
    'Science': [91, np.nan, 85]
    }
    #QUESTION 1ST
    print(line)
    Q1PrintBasicInfo(data)
    print(line)
    print(line,"\n")

    #QUESTION 2RD
    print(line)
    Q2DesStatistic(data)
    print(line)
    print(line,"\n")

    #QUESTION 3RD
    print(line)
    Q3AddTotalColumn(data)
    print(line)
    print(line,"\n")

    #QUESTION 4TH
    print(line)
    Q4MoreThan85(data)
    print(line)
    print(line,"\n")

    #QUESTION 5TH
    print(line)
    Q5ReplaceName(data)
    print(line)
    print(line,"\n")

    #QUESTION 6TH
    print(line)
    Q6SortByDesc(data)
    print(line)
    print(line,"\n")

    #QUESTION 7TH
    print(line)
    Q7BarPlot(data)
    print(line)
    print(line,"\n")

    #QUESTION 8TH
    print(line)
    Q8AmitMarks(data)
    print(line)
    print(line,"\n")

    #QUESTION 9TH
    print(line)
    Q9MissingValues(data4Q9)
    print(line)
    print(line,"\n")

    #QUESTION 10TH
    print(line)
    Q10DropColumn(data)
    print(line)

if __name__ == "__main__":
    main()