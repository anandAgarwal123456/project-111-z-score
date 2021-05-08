import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd

df = pd.read_csv("medium_data.csv")
data = df["claps"].tolist()

#scatter = ff.create_distplot([data],["Score"],show_hist = False)
#scatter.show()

mean = statistics.mean(data)
st_dev = statistics.stdev(data)

print("stdev of all the data:", st_dev)
print("mean of all the data :",mean)

def sampling_data():
    dataset=[]
    for sample in range(0,30):
        sampleSize = random.randint(0,len(data)-1)
        allData = data[sampleSize]
        dataset.append(allData)

    mean = statistics.mean(dataset)
    return mean

mean_list = []

for i in range(0,100):
    mean2 = sampling_data()
    mean_list.append(mean2)

mean_of_sampling_dist = statistics.mean(mean_list)
stdev_of_sampling_dist = statistics.stdev(mean_list)

first_std_deviation_start, first_std_deviation_end = mean_of_sampling_dist-stdev_of_sampling_dist, mean_of_sampling_dist +stdev_of_sampling_dist
sec_std_deviation_start, sec_std_deviation_end = mean_of_sampling_dist- (2*stdev_of_sampling_dist), mean_of_sampling_dist + (2*stdev_of_sampling_dist)
thd_std_deviation_start, thd_std_deviation_end = mean_of_sampling_dist- (3*stdev_of_sampling_dist), mean_of_sampling_dist + (3*stdev_of_sampling_dist)


scatter2 = ff.create_distplot([mean_list],["samplingData"],show_hist = False)
scatter2.add_trace(go.Scatter(x= [mean_of_sampling_dist,mean_of_sampling_dist] , y =[0,0.2] , mode = 'lines'))
scatter2.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
scatter2.add_trace(go.Scatter(x=[sec_std_deviation_start, sec_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START"))
scatter2.add_trace(go.Scatter(x=[thd_std_deviation_start, thd_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 START"))
scatter2.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
scatter2.add_trace(go.Scatter(x=[sec_std_deviation_end, sec_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
scatter2.add_trace(go.Scatter(x=[thd_std_deviation_end, thd_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
scatter2.add_trace(go.Scatter(x=[mean2,mean2], y=[0, 0.17], mode="lines", name="MEAN OF SAMPLING DATA "))
scatter2.show()

print("mean of sampling distribution is:",mean_of_sampling_dist)
print("stdev of sampling distributionis:",stdev_of_sampling_dist)

z_score = (mean2 - mean_of_sampling_dist)/ stdev_of_sampling_dist
print("The z-score is:",z_score)
