# Interesting Bayes' Theorem Problems

I am given 99 fair coins and 1 coin that has heads on both sides. I draw a coin from the bag and flip it 10 times. What is the probability the drawn coin was the unfair coin?
solution:[ipynb](./coin.ipynb), [nbviewer](http://nbviewer.ipython.org/github/StevenCHowell/playing_with_data/blob/master/bayes_problems/coin.ipynb)

1. A couple has two children and the older child is a boy. If the probabilities of having a boy or a girl are both 1/2, what is the probability that the couple has two boys?
2. A couple has two children, one of which is a boy. If the probabilities of having a boy or a girl are both 1/2, what is the probability that the couple has two boys?
solution:[ipynb](./two_boys.ipynb), [nbviewer](http://nbviewer.ipython.org/github/StevenCHowell/playing_with_data/blob/master/bayes_problems/two_boys.ipynb)
source: https://brilliant.org/wiki/bayes-theorem/


50% of all people who receive a first interview receive a second interview
95% of your friends that got a second interview felt they had a good first interview
75% of your friends that DID NOT get a second interview felt they had a good first interview
If you feel that you had a good first interview, what is the probability you will receive a second interview?
source: https://stats.stackexchange.com/questions/86015/amazon-interview-question-probability-of-2nd-interview

1. A friend who works in a big city owns two cars, one small and one large. Three-quarters of
the time he drives the small car to work, and one-quarter of the time he drives the large car.
If he takes the small car, he usually has little trouble parking, and so is at work on time with
probability 0.9. If he takes the large car, he is at work on time with probability 0.6. Given
that he was on time on a particular morning, what is the probability that he drove the small
car?
2. At a certain gas station 40% of the customers request regular gas, 35% request unleaded gas,
and 25% request premium gas. Of those customers requesting regular gas, only 30% fill their
tanks. Of those customers requesting unleaded gas, 60% fill their tanks, while of those
requesting premium, 50% fill their tanks. If the next customer fills the tank, what is the
probability that regular gas is requested?
3. Seventy percent of the light aircraft that disappear while in flight in a certain country are
subsequently discovered. Of the aircraft that are discovered, 60% have an emergency locator,
whereas 90% of the aircraft not discovered do not have such a locator. Suppose that a light
aircraft has disappeared. If it has an emergency locator, what is the probability that it will be
discovered?
source: http://sites.stat.psu.edu/~lsimon/stat250/homework/chapter3/bayes.pdf


1. In a particular pain clinic, 10% of patients are prescribed narcotic pain killers. Overall, five percent of the clinic’s patients are addicted to narcotics (including pain killers and illegal substances). Out of all the people prescribed pain pills, 8% are addicts. If a patient is an addict, what is the probability that they will be prescribed pain pills?

2. 1% of people have a certain genetic defect.
90% of tests for the gene detect the defect (true positives).
9.6% of the tests are false positives.
If a person gets a positive test result, what are the odds they actually have the genetic defect?

3. Given the following statistics, what is the probability that a woman has cancer if she has a positive mammogram result?
One percent of women over 50 have breast cancer.
Ninety percent of women who have breast cancer test positive on mammograms.
Eight percent of women will have false positives.
source: http://www.statisticshowto.com/bayes-theorem-problems/


1) The first one is a warm-up problem.  I got it from Wikipedia (but it's no longer there):
Suppose there are two full bowls of cookies. Bowl #1 has 10 chocolate chip and 30 plain cookies, while bowl #2 has 20 of each. Our friend Fred picks a bowl at random, and then picks a cookie at random. We may assume there is no reason to believe Fred treats one bowl differently from another, likewise for the cookies. The cookie turns out to be a plain one. How probable is it that Fred picked it out of Bowl #1?
This is a thinly disguised urn problem.  It is simple enough to solve without Bayes's Theorem, but good for practice.

2) This one is also an urn problem, but a little trickier.
The blue M&M was introduced in 1995.  Before then, the color mix in a bag of plain M&Ms was (30% Brown, 20% Yellow, 20% Red, 10% Green, 10% Orange, 10% Tan).  Afterward it was (24% Blue , 20% Green, 16% Orange, 14% Yellow, 13% Red, 13% Brown).
A friend of mine has two bags of M&Ms, and he tells me that one is from 1994 and one from 1996.  He won't tell me which is which, but he gives me one M&M from each bag.  One is yellow and one is green.  What is the probability that the yellow M&M came from the 1994 bag?

3) This one is from one of my favorite books, David MacKay's "Information Theory, Inference, and Learning Algorithms":
Elvis Presley had a twin brother who died at birth.  What is the probability that Elvis was an identical twin?
To answer this one, you need some background information: According to the Wikipedia article on twins:  ``Twins are estimated to be approximately 1.9% of the world population, with monozygotic twins making up 0.2% of the total---and 8% of all twins.''

4) Also from MacKay's book:
Two people have left traces of their own blood at the scene of a crime.  A suspect, Oliver, is tested and found to have type O blood.  The blood groups of the two traces are found to be of type O (a common type in the local population, having frequency 60%) and of type AB (a rare type, with frequency 1%).  Do these data (the blood types found at the scene) give evidence in favour [sic] of the proposition that Oliver was one of the two people whose blood was found at the scene?

5) I like this problem because it doesn't provide all of the information.  You have to figure out what information is needed and go find it.
According to the CDC, ``Compared to nonsmokers, men who smoke are about 23 times more likely to develop lung cancer and women who smoke are about 13 times more likely.''
If you learn that a woman has been diagnosed with lung cancer, and you know nothing else about her, what is the probability that she is a smoker?

6) And finally, a mandatory Monty Hall Problem.  First, here's the general description of the scenario, from Wikipedia:
Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say Door A [but the door is not opened], and the host, who knows what's behind the doors, opens another door, say Door B, which has a goat. He then says to you, "Do you want to pick Door C?" Is it to your advantage to switch your choice?
The answer depends on the behavior of the host if the car is behind Door A.  In this case the host can open either B or C.  Suppose he chooses B with probability p and C otherwise.  What is the probability that the car is behind Door A (as a function of p)?


source: http://www.maths.uq.edu.au/courses/MATH3104/Lectures/goodhill/bayes_problems.pdf
solutions: http://www.maths.uq.edu.au/courses/MATH3104/Lectures/goodhill/bayes_solutions.pdf
1. You go to see the doctor about an ingrowing toenail. The doctor selects you at random to have a blood test for swine flu, which for the purposes of this exercise we will say is currently suspected to affect 1 in 10,000 people in Australia. The test is 99% accurate, in the sense that the probability of a false positive is 1%. The probability of a false negative is zero. You test positive. What is the new probability that you have swine flu?
Now imagine that you went to a friend’s wedding in Mexico recently, and (for the purposes of this exercise) it is know that 1 in 200 people who visited Mexico recently come back with swine flu. Given the same test result as above, what should your revised estimate be for the probability you have the disease?

2. Imagine that, while in Mexico, you also took a side trip to Las Vegas, to pay homage to the TV show CSI. Late one night in a bar you meet a guy who claims to know that in the casino at the Tropicana there are two sorts of slot machines: one that pays out 10% of the time, and one that pays out 20% of the time [note these numbers may not be very realistic]. The two types of machines are coloured red and blue. The only problem is, the guy is so drunk he can’t quite remember which colour corresponds to which kind of machine. Unfortunately, that night the guy becomes the vic in the next CSI episode, so you are unable to ask him again when he’s sober.
Next day you go to the Tropicana to find out more. You find a red and a blue machine side by side. You toss a coin to decide which machine to try first; based on this you then put the coin into the red machine. It doesn’t pay out. How should you update your estimate of the probability that this is the machine you’re interested in? What if it had paid out - what would be your new estimate then?

source: http://allendowney.blogspot.com/2011/10/my-favorite-bayess-theorem-problems.htm
