### Na&#239;ve Bayes
(+) Easy to implement.  
(+) Works with large feature spaces (e.g., language, text classification).  
(-) Breaks in weird ways (e.g., "Chicago Bulls" - distinct phrases do _not_ work well).  
(-) Ignores the order of words.  

_Application: Identifying the author of a piece of text (i.e., identify the author of a particular email)._

**Time (in seconds)**  
Training: 0.171 seconds  
Prediction: 0.186 seconds  

_Accuracy on example: 0.97383_

<hr>
### Support Vector Machines (SVM)
**Parameters**: `kernel`, `C`, and `gamma`.  
`C` is the trade-off parameter between a smooth decision boundary and classifying training points correctly (**increasing** `C` yields a *more* complex decision boundary); nevertheless, all of the parameters can effect over-fitting.

(+) Work well in complicated domains where there is a clear margin of separation.  
(-) Poor with large datasets because training time is cubic (w.r.t. size of dataset).  
(-) Poor with lots of noise - when the classes are overlapping.  

**Time (in seconds)**  
Training: 153.919 seconds  
Prediction: 17.146 seconds  

_Accuracy on example: 0.9841  
&nbsp;&nbsp;&nbsp;Using only 1% of features (big speed boost): 0.8853  
&nbsp;&nbsp;&nbsp;Using a more complex kernel (`rbf`): 0.6160
&nbsp;&nbsp;&nbsp;Using `rbf` with `C` = 10: 0.6160  
&nbsp;&nbsp;&nbsp;Using `rbf` with `C` = 100: 0.6160  
&nbsp;&nbsp;&nbsp;Using `rbf` with `C` = 1,000: 0.8214  
&nbsp;&nbsp;&nbsp;Using `rbf` with `C` = 10,000: 0.8925  
Reverting back to full dataset with optimized `rbf` and `C` = 10,000: **0.9909** (!)_

Consider if speed is important to you (e.g., flagging credit card fraud, and blocking the transaction before it goes through; voice recognition, like Siri).

<hr>
