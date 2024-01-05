# 8-sidor-word-frequencies
Analysing portrayals of women in Swedish newspaper _8 sidor_ between 2003 and 2012 using word frequencies

**Introduction**

For my final project for the course Computational Literacy, I wanted to analyse how women and girls are portrayed in modern-day Swedish media. I was inspired by previous research on female media representation, which tends to focus on topics such as feminism, parenthood and more specifically motherhood (e.g., Bergnehr & Henriksson, 2021), domestic and sexual violence (e.g., Karlsson et al., 2021; Lindqvist & Ganetz, 2020), etc. In other words, there is a tendency for women to be associated with problems considered stereotypically feminine.

I wanted to examine whether this tendency holds true in the Swedish context, since Sweden is among the leaders in the EU in terms of depicting women in prime-time television and print media (Balkmar, 2017; Edström, 2014). I focused on the newspaper _8 sidor_, a nationwide news outlet covering a variety of topics, including domestic and foreign news, sport, and culture. My research questions formulated as follows: **“(1) How are women portrayed in the Swedish newspaper _8 sidor_ between 2003 and 2012, and (2) how does the surrounding context differ compared to articles depicting men?”**

**Dataset**

The dataset includes a corpus containing articles from _8 sidor_ published between 2003 and 2012. For my analysis, I accessed the data through the concordancer Korp (available through [this link]([url](https://spraakbanken.gu.se/korp/#?corpus=attasidor&cqp=%5B%5D))).

To answer my first research question, regarding how women are portrayed in the articles, I searched for keywords including the root _kvinn_. Then, to see whether there were any differences compared to articles explicitly mentioning men, I searched for the word _man_ in all its forms (i.e., _man, mannen, män, männen_). Searching by root was not possible in this case, since the word changes vowel in plural; therefore, I added all four forms to the search as separate words.

**Processing the data and analysis**

I used Python to get the search results from Korp. I took inspiration from an earlier project comparing differences in use between the words _maahanmuuttaja_ and _pakolainen_ in Finnish newspapers. The project can be accessed through [this link]([url](https://zenodo.org/records/44544)).

To clean up my data, I again used Python to remove stopwords. I relied on a predefined collection of Swedish stopwords, which is [available on GitHub]([url](https://github.com/stopwords-iso/stopwords-sv)) for free. It contains pronouns, numbers, common adjectives and adverbs. I also removed all capital letters.

My initial plan for this project was to create a topic model of the relevant articles mentioning women and men, respectively. However, after a closer look at the data I realised that the corpus data has been scrambled for copyright reasons, meaning that all sentences appear in a randomised order. The original texts could not be recreated, and creating a topic model of these scrambled sentences would be meaningless. For this reason, I decided to focus on word frequencies instead. After filtering the search results for both women and men, I extracted the 30 most frequently used words in each case. The results have been linked as TXT files.

**Results and limitations**

The results did not support my initial expectations that articles mentioning women would focus on stereotypically feminine topics such as parenthood or female representation. In fact, there was a lot of overlap between the two word frequency lists generated. Most of those appeared to be crime-related, such as _polisen_ (‘the police’), _dödade_ (‘murdered’), or _misstänkt_ (‘suspected’). Some of the words also mentioned places, such as _Sverige_ or _Stockholm_ (in the results files, those are listed in lowercase since all capital letters were removed pre-analysis).

There were some differences, however. The search results for men contained some additional crime-related terms, such as _fängelse_ and _skjuta_ (including the forms _sköt_ and _skjuten_). On the other hand, some of the most common words in the articles mentioning women were _rättigheter_ (‘rights’) and _abort_ (‘abortion’), presumably used to discuss prominent feminist issues such as representation or reproductive rights. The fact that these words were not as common in the search results for men signals that at least to some degree, Swedish media tends to discuss women in relation to traditionally feminine topics.

Finally, while the word _kvinna_ and its plural and definite forms appeared much more often in the analysed coverage than the word _man_ in all its forms (3,383 results for the most commonly used form _kvinnor_ vs. only 2,351 for _mannen_), the remaining 30 most common words in the search focusing on men had a much higher frequency of use than the most used words in the women-oriented articles. The last two words in the search results for women, for example, _gången_ and _procent_, appear 98 and 96 times, respectively. On the other hand, the last two words in the male search results, _staden_ and _började_, were used 146 times each. This might be indicative of the fact that articles mentioning women focus on a wider array of issues than those mentioning men.

Some disclaimers are due regarding the limitations of my project. My analysis only covered one news media outlet, _8 sidor_, which limits the generalisability of my findings. Additionally, with a newspaper that only comes out once a week, there is a high chance that any events which occur closer to the publication day might outshadow those happening earlier in the week, thereby skewing the results.

Further, as Swedish does not typically use female forms of nouns (such as, for example, German, which has different forms for certain professions and job titles depending on whether the subject is male or female), I suspect that there are articles on prominent female public figures (e.g., Sweden’s former Prime Minister Magdalena Andersson) which do not specifically refer to their gender. Given the nature of my analysis, those articles would probably be omitted from my search results, which directly affects my conclusions. All this suggests that there are grounds for further research on the topic of female representation in Swedish media, and more detailed studies are needed to draw broader conclusions about women’s image in the press. 

**References**

Balkmar, D. (2017). Sweden: Too many women? Women and gender (in)equality in Swedish media. In K. Ross & C. Padovani (Eds.), _Gender equality and the media: A challenge for Europe_. Routledge.

Bergnehr, D., & Henriksson, H. W. (2021). Hardworking women: Representations of lone mothers in the Swedish daily press. _Feminist Media Studies, 21_(1), 132–146. https://doi.org/10.1080/14680777.2019.1704815

Edström, M. (2014). Nordic journalism with gender parity and problems. In M. Edström & R. Mølster (Eds.), _Making change: Nordic examples of working towards gender equality in the media_ (pp. 47–52). Nordicom.

Karlsson, N., Lila, M., Gracia, E., & Wemrell, M. (2021). Representation of Intimate Partner Violence Against Women in Swedish News Media: A Discourse Analysis. _Violence Against Women, 27_(10), 1499–1524. https://doi.org/10.1177/1077801220940403

Lindqvist, L., & Ganetz, H. (2020). Brave women sound the alarm – representations of men and women in the Swedish media coverage of #MeToo. _Journalistica_, 1, Article 1. https://doi.org/10.7146/journalistica.v14i1.123510

