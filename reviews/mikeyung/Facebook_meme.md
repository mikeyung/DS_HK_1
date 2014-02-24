# Can Internet Memes be Modeled as Genes?

## Objective/Abstract: 

[Richard Dawkins](http://en.wikipedia.org/wiki/Meme) likened Internet memes to genes, and this study is to show just how accurate that analogy is.

Source : [The evolution of memes on Facebook](https://www.facebook.com/notes/facebook-data-science/the-evolution-of-memes-on-facebook/10151988334203859)

The News : [Facebook Data Scientists Prove Memes Mutate And Adapt Like DNA](http://techcrunch.com/2014/01/08/facebook-memes/)

**Not yet completed ...**

## Hypothesis: 

An Internet meme is an idea that is readily transmitted from person to person. But we humans are not perfect transmitters. While sometimes we repeat the idea exactly, often we **change** the meme, either unintentionally, or to **embellish** or **improve** it.

So can memes really be modeled as genes ? How would one test the hypothesis that memes undergo a process akin to biological evolution? 


## Style: 

I think the study is first and foremost to let Facebook themselves understand more about their users' status usage pattern and then adjust the algorithm to display various posts in each Facebook users' wall.

On the other hand, it is also some impressive figures and findings that will attract many Internet technology as well as social media blogs to publish.

## Methods: 

The study examined near-complete traces of hundreds of memes, collectively comprising over 460 million individual instances.

Every instance of a meme variant has a constant probability per unit time of being copied. An individual copy will be exact with probability (1 - µ) and will be a mutation with probability µ (e.g. if µ is 0.1, 90% of users will copy their friends’ version exactly, and 10% will modify the text before posting it as their own status update). 

Next the study checks whether the Yule model fits. 

For a given mutation rate, the Yule model predicts how popularity will be distributed among the variants. The study characterizes the popularity distribution with the Gini coefficient: if the Gini coefficient is close to 0, all variants are roughly equally popular, if it’s close to 1, a few variants are wildly popular while most have been copied once or twice.

## Conclusions: 

The study observed a number of remarkable parallels between how information evolves in a social network and how genes evolve. Drawing these parallels simply hasn’t been possible before for lack of large-scale data containing the evolution histories of many memes.

