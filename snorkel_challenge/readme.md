# Snorkel Challenge Introduction
This challenge is about labeling texts (paragraphs, sentences) based on how well they match certain words (rule). If the texts matches 2 or 3 words then it is assigned a label. But a text can also match words from multiple rules which is why a machine learning model is used to "learn" based on the matches that this text describes a particular subject. 

Example:

Text: "Pomelos (Citrus maxima) are known for their thick peel thick peel which—inter alia—serves as energy dissipator when fruits impact on the ground after being shed. It protects the fruit from splitting open and thus enables the contained seeds to stay" 


This is assigned to the label: Maintain structural integrity because there is a match of the word "Protect" 

To start this challenge, click on the following [Link](https://colab.research.google.com/github/nasa-petal/interview_questions/blob/main/snorkel_challenge/petal_snorkel_challenge.ipynb)
