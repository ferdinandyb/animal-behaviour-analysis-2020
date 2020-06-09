#!/usr/bin/env python3

import pandas as pd
import numpy as np
import scipy.stats

from sklearn import svm
from sklearn.model_selection import cross_val_score,ShuffleSplit

# Results of grid-search optimization:
Cdict = {
    'dog': 100000.0,
    'large': 5,
    'medium':100.0,
    'small':5.0,
    'wolf':1000.0,
}
gdict = {
    'dog': 0.001,
    'large':0.05,
    'medium': 0.01,
    'small':0.05,
    'wolf':0.01,
}

labels = ['lay','sit','stand','walk','trot','run','eat','drink']

def threshold_accuracy(df):
    TP = df.loc['above_threshold','correct']
    TN = df.loc['below_threshold','incorrect']
    FN = df.loc['below_threshold','correct']
    FP = df.loc['above_threshold','incorrect']
    return (TN + TP)/(TN + TP + FN + FP)


medium = pd.read_csv("mediumdog.dat")
ids = np.unique(medium["animal_id"])

# per individual cross-validation
overall_accuracy = 0
overall_accuracy_counter = 0
df_label  = pd.DataFrame(np.zeros((len(labels),len(labels))),
                         index=labels,
                         columns=labels)
counter = {key: 0 for key in labels}
thresholds = [0.5,0.6,0.7,0.8,0.9]
truthmatrixs = {x : pd.DataFrame(
                        index=["above_threshold","below_threshold"],
                        columns = ["correct","incorrect"]
                                ).fillna(0) for x in thresholds}
    
for id_ in ids:
    train = medium[medium["animal_id"] != id_]
    test = medium[medium["animal_id"] == id_]
    train_feat = train.values[:,5:]
    train_label = [labels.index(l) + 1 for l in train["label"]]
    test_feat = test.values[:,5:]
    test_label = [labels.index(l) + 1 for l in test["label"]]
    clf = svm.SVC(C = Cdict["medium"],
        gamma = gdict["medium"],
        probability = True)

    clf.fit(train_feat,train_label)
    prediction = clf.predict_proba(test_feat)
    predicted_labels = [np.argmax(p) + 1 for p in prediction]
    predicted_probs = [np.max(p) for p in prediction]

    for pred, known, p in zip(predicted_labels, test_label, predicted_probs):
        overall_accuracy_counter += 1
        counter[labels[known - 1]] += 1
        df_label[labels[known - 1]][labels[pred - 1]] += 1
        if pred == known:
            overall_accuracy += 1
            thcol = "correct"
        else:
            thcol = "incorrect"

        for t in thresholds:
            thind = "above_threshold" if p > t else "below_threshold"
            truthmatrixs[t].loc[thind,thcol] += 1
print("per individual crossvalidation")
print("overall accuracy", overall_accuracy/overall_accuracy_counter)
acc = [threshold_accuracy(truthmatrixs[t]) for t in thresholds]
print("threshold accuracy", np.max(acc), "threshold", thresholds[np.argmax(acc)])

# n-fold crossvalidation

feat = medium.values[:,5:]
label = [labels.index(l) + 1 for l in medium["label"]]
clf = svm.SVC(C = Cdict["medium"],
        gamma = gdict["medium"],
        probability = True)
shuffle = ShuffleSplit(test_size=0.3,n_splits = 7)
nfoldcross = cross_val_score(clf,feat,label,cv=shuffle)
t = scipy.stats.t.ppf(0.95,6)
print("7-fold cross-validation")
print("overall accuracy +- CI", np.mean(nfoldcross),np.std(nfoldcross)*t/np.sqrt(6))
    
