# HitchHikers-Guide-Machine-Learning
This is extended version of [Conor Dewey](https://github.com/conordewey3)'s repository.
At first i looked into this, it seems too much simplification.
I know how to code that and that, but since i have no solid basis in mathematic, especially statistic and probability, all the codes does not make any sense.
So, i decided to looking deeper into statistical world and practice all i just knew into a computer code. Since i am programmer and knew little bit about computational model, then i will tried to build some programming interfaces for each statistic model and applied them to do study cases.
Since i am good at reading, here some references that i used to understand fundamental of 'machine learning':
* [Online Statistic Book by David M. Lane](http://onlinestatbook.com/2/index.html)
* [Pattern Recognition and Machine Learning by Christopher M. Bishop](https://www.goodreads.com/book/show/55881.Pattern_Recognition_and_Machine_Learning)

## Linear Regression
This is very easy technique and easy to implement in code. You only need to understand some basic principles, such as: population and sample, range, invariants, correlations and slopes.
The challenge is how we find best fitting line that squared all points in our two dimensional data model. One known approach to find best fitting line is by calculate slope using partial data. For example, if the trend likely increase at current time, than we consider to calculate only most recent data.