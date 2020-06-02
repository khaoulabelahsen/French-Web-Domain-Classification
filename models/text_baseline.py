import os
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import codecs
from os import path

# Reading training data
data = "../data/"
with open(data + "train_noduplicates.csv", "r") as f:
    train_data = f.read().splitlines()

train_hosts = list()
y_train = list()
for row in train_data:
    host, label = row.split(",")
    train_hosts.append(host)
    y_train.append(label.lower())

# Reading test data
with open(data + "test.csv", "r") as f:
    test_hosts = f.read().splitlines()

# Loading the textual content of a set of web pages for each host into the dictionary "text".
# The encoding parameter is required since the majority of our text is french.
text = dict()
filenames = os.listdir("../text/text")
for filename in filenames:
    with codecs.open(path.join("../text/text/", filename), encoding="latin-1") as f:
        text[filename] = f.read().replace("\n", "").lower()

train_data = list()
for host in train_hosts:
    if host in text:
        train_data.append(text[host])
    else:
        train_data.append("")

# Creating the training matrix. Each row corresponds to a web host and each column to a word present in at least 10 web
# hosts and at most 1000 web hosts. The value of each entry in a row is equal to the tf-idf weight of that word in the
# corresponding web host

vec = TfidfVectorizer(
    decode_error="ignore",
    strip_accents="unicode",
    encoding="latin-1",
    min_df=10,
    max_df=1000,
)
X_train = vec.fit_transform(train_data)

# Getting textual content of web hosts of the test set
test_data = list()
for host in test_hosts:
    if host in text:
        test_data.append(text[host])
    else:
        test_data.append("")

# Creating the test matrix following the same approach as in the case of the training matrix
X_test = vec.transform(test_data)

print("Train matrix dimensionality: ", X_train.shape)
print("Test matrix dimensionality: ", X_test.shape)

# Using logistic regression to classify the web-pages of the test set
clf = LogisticRegression(solver="lbfgs", multi_class="auto", max_iter=1000)
clf.fit(X_train, y_train)
print(clf.score(X_train, y_train))
y_pred = clf.predict_proba(X_test)

# Writing predictions to a file
with open("../text_baseline.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    lst = clf.classes_.tolist()
    lst.insert(0, "Host")
    writer.writerow(lst)
    for i, test_host in enumerate(test_hosts):
        lst = y_pred[i, :].tolist()
        lst.insert(0, test_host)
        writer.writerow(lst)
