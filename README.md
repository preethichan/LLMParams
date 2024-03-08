# LLMParams
Built an automated framework to test different values of Temperature and Top_p and their impact on the quality of LLM responses in various business use cases.

# The 2 parameters that control LLMs:

Let's start by understanding what Large Language Models (LLMs) are. They're like really smart computer programs that can do lots of things, like talk to chatbots, write articles, translate languages, and finish sentences for us. They're super powerful, but we need to handle them efficiently to get the best results based on our needs.
## Basics of LLM:
Let’s see how it works and what it does on a very high level. To answer simply it predicts the next word or token. A token can be a single character or group of words (4 words). As you can see a whole bunch of documents (corpus of data) are converted to tokens. The core of LLM is now to use this bunch of tokens to predict the next probable word. A search mechanism is used by LLM to generate a list of probabilities of every token that could be next. Temperature is now introduced as a parameter to generate these probabilities, while Top_p is used as a sampler mechanism to decide which probabilities to consider. 
 
When we use these LLM models to build our application, we can adjust temperature and top_p parameters to make them work even better. They might sound fancy, but they're just ways to control how creative or predictable the answers are.
In this article, we're going to explore these settings and see what they do. We'll start with temperature, which affects how random or creative the text is. Then we'll look at top_p which helps us control how much the model sticks to what it already knows. By the end, you'll have a better idea of how to use these settings to get exactly the kind of answer you want from these clever models.
Let's dive in!
### Temperature:
Temperature is an important setting when we're tweaking how these models work, like GPT-3. It's like a knob that controls how random or creative the text it generates is. These LLM models decide which word to use next based on the chances of that word appearing. So, with temperature, we can adjust these chances to make the text more random or more predictable.
When the model is deciding which word to use, there can be several hidden layers in the neural network and finally, it goes through something called softmax in the last output layer. Softmax turns the raw numbers (or logits) into probabilities. That's where temperature comes in – it's like a dial that adjusts how spread out or focused these probabilities are. If you turn up the temperature, you'll get more randomness in the text, but if you turn it down, the text will be more predictable.
                               
      
Where x is the i-th element of the input vector.
        e is the base of natural log= 2.718 
        the denominator is the sum of all exponentials of I elements in the input vector.
                                                                                             
The above softmax function simply exponentiates each logit(x) and then divides it by the sum of all exponentiated values. In simple words, it divides all of the numbers by the temperature value we define(T in range 0- 1). This function generally ensures that the output is a probability distribution, meaning that the values are positive and normalized in the range of 0-1 and sum up to 1. 
 
The temperature hyperparameter is the value of “T” applied to each of the logits, Let's say T=1, x_i/T will become 0, leading to random distribution and will use a creative output. 
On the other hand, if T=0 small value will skew the probabilities into a deterministic output. 
Let’s look at an example of how Temperature value affects the model outputs. I ran a small program using Openai LLM, gpt-4 model and keeping Top P= 1 for now. 

text = f""" 
Is there a way to keep things quiet?
"""
prompt = f"""
complete the sentence in 2 words.
```{text}```
"""

Temperature:    0	     

Output:   Yes, Silence.

Temperature:    1

Output:   Noice Control

As we decrease the temperature the output is more generic and predictable. However, with higher temperature values the output is more specific and creative. 
### Top- p:
Before getting into Top_p, let’s understand what Sampling is. In simplest terms, sampling means randomly picking the next word according to its conditional probability distribution.
Top_p is one such sampler parameter used by LLM to select a most likely token from a probability distribution whose cumulative probability exceeds the probability p. The value for p is usually between 0.0 – 0% to 1.0- 100% 
The steps involved in the process are as follows:
1.	The first iteration starts by ordering the tokens in descending order of probabilities.
2.	The next iteration is selecting the smallest number of top tokens such that their cumulative probable value is at least p.
3.	Sample from those tokens and choose the value close to p.
Let's see with an example, if top_p = 0.50, then the word “Noice” had a chance of 50% which is equal to top_p and will be chosen. 
 
## Conclusion:
Temperate and Top_p are important parameters for fine-tuning the LLM output for various real use cases. At the same time, it is important to understand they both can influence the outcome and can easily amplify each other’s impact and produce a meaningless output. The following chart provides a default value for temperature and top_p based on the business use-case. 

 
