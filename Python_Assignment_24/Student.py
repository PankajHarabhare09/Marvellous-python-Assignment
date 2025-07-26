import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def MathMinMaxScaler(dataset):
    dataframe = pd.DataFrame(dataset)
    scaler = MinMaxScaler()
    dataframe['Math_Scalling'] = scaler.fit_transform(dataframe[['Math']])
    print(dataframe)

def GenderOneHotEncoding(dataset):
    dataframe = pd.DataFrame(dataset)
    dataframe['Gender'] = ['Male' , 'Male' , 'Female']
    dataframe_encoding = pd.get_dummies(dataframe , columns = ['Gender'],drop_first = 1)
    print(dataframe_encoding)

def GroupByGender(dataset):
    dataframe = pd.DataFrame(dataset)
    dataframe['Gender'] = ['Male' , 'Male' , 'Female']
    marks = dataframe.groupby('Gender')[['Math', 'English', 'Science']].mean()
    print(marks)

def PieOfSagar(dataset):
    dataframe = pd.DataFrame(dataset)
    sagar_marks = dataframe[dataframe['Name'] == 'Sagar'][['Math', 'English', 'Science']].iloc[0]
    plt.pie(sagar_marks, labels=sagar_marks.index, autopct='%1.1f%%', startangle=90)
    plt.title("Sagar's Subject-wise Marks")
    plt.show()

def StatusPassFail(dataset):
    dataframe = pd.DataFrame(dataset)
    dataframe['Total'] = dataframe[['Math', 'English', 'Science']].sum(axis = 1)
    dataframe['Status'] = dataframe['Total'].apply(lambda Status: 'Pass' if Status >=250 else 'Fail')
    print(dataframe)

def CountPassStudent(dataset)
    StatusPassFail()
    passed_student = dataframe[dataframe['Status'] == 'Pass'].shape()
    print("Number of students passed:", num_passed)

def ConvertCSV(dataset):
    dataframe = pd.DataFrame(dataset)
    dataframe.to_csv('final_students_data.csv', index=False)

def HistographMath(dataset):
    dataframe = pd.DataFrame(dataset)
    plt.hist(df['Math'], bins=5, color='skyblue', edgecolor='black')
    plt.title('Histogram of Math Marks')
    plt.xlabel('Marks')
    plt.ylabel('Number of Students')
    plt.grid(True)
    plt.show()

def ReplaceSubName(dataset):
    dataframe = pd.DataFrame(dataset)
    dataframe.rename(columns={'Math': 'Mathematics'}, inplace=True)
    print(dataframe)

def BoxPlotEnglish(dataset):
    dataframe = pd.DataFrame(dataset)
    plt.boxplot(dataframe['English'])
    plt.title("Boxplot of English Marks")
    plt.ylabel("Marks")
    plt.grid(True)
    plt.show()


def main():
    line = "-"*58
    data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
    }

    print(line)
    #QUESTION NO 1
    MathMinMaxScaler(data)
    print(line)
    print(line,"\n")  

    print(line)
    #QUESTION NO 2
    GenderOneHotEncoding(data)
    print(line)
    print(line,"\n")

    print(line)
    #QUESTION NO 3
    GroupByGender(data)
    print(line)
    print(line,"\n") 

    print(line)
    #QUESTION NO 4
    PieOfSagar(data)
    print(line)
    print(line,"\n")

    print(line)
    #QUESTION NO 5
    StatusPassFail(data)
    print(line)
    print(line,"\n")

    print(line)
    #QUESTION NO 6
    CountPassStudent(data)
    print(line)
    print(line,"\n")

    print(line)
    #QUESTION NO 7
    ConvertCSV(data)
    print(line)
    print(line,"\n")

    print(line)
    #QUESTION NO 8
    HistographMath(data)
    print(line)
    print(line,"\n")

    print(line)
    #QUESTION NO 9
    ReplaceSubName(data)
    print(line)
    print(line,"\n")

    print(line)
    #QUESTION NO 10
    BoxPlotEnglish(data)
    print(line)
    print(line,"\n")


if __name__ == "__main__":
    main()