import re
#Sachine Tendulkar Wikipedia

data = """
Sachin Ramesh Tendulkar (/ˌsʌtʃɪn tɛnˈduːlkər/ (About this soundlisten); born 24 April 1973) is an Indian former international cricketer and a former captain of the Indian national team. He is widely regarded as one of the greatest batsmen in the history of cricket.[4] He is the highest run scorer of all time in International cricket. Tendulkar took up cricket at the age of eleven, made his Test debut on 15 November 1989 against Pakistan in Karachi at the age of sixteen, and went on to represent Mumbai domestically and India internationally for close to twenty-four years.
He is the only player to have scored one hundred international centuries, the first batsman to score a double century in an ODI, the holder of the record for the most runs in both Test and ODI, and the only player to complete more than 30,000 runs in international cricket.[5] He is colloquially known as Little Master or Master Blaster,[6][7][8][9] In 2001, Sachin Tendulkar became the first batsman to complete 10,000 ODI runs in his 259 innings.[10] In 2002, halfway through his career, Wisden Cricketers' Almanack ranked him the second greatest Test batsman of all time, behind Don Bradman, and the second greatest ODI batsman of all time, behind Viv Richards.
.[11] Later in his career, Tendulkar was a part of the Indian team that won the 2011 World Cup, his first win in six World Cup appearances for India.[12] He had previously been named "Player of the Tournament" at the 2003 edition of the tournament, held in South Africa. In 2013, he was the only Indian cricketer included in an all-time Test World XI named to mark the 150th anniversary of Wisden Cricketers' Almanack.[13][14][15]
Tendulkar received the Arjuna Award in 1994 for his outstanding sporting achievement, the Rajiv Gandhi Khel Ratna award in 1997, India's highest sporting honour, and the Padma Shri and Padma Vibhushan awards in 1999 and 2008, respectively, India's fourth and second highest civilian awards.[16] After a few hours of his final match on 16 November 2013, the Prime Minister's Office announced the decision to award him the Bharat Ratna, India's highest civilian award.[17][18] He is the youngest recipient to date and the first ever sportsperson to receive the award.[19][20].
He also won the 2010 Sir Garfield Sobers Trophy for cricketer of the year at the ICC awards.[21] In 2012, Tendulkar was nominated to the Rajya Sabha, the upper house of the Parliament of India.[22] He was also the first sportsperson and the first person without an aviation background to be awarded the honorary rank of group captain by the Indian Air Force.[23] In 2012, he was named an Honorary Member of the Order of Australia.[24][25]
In 2010, Time magazine included Sachin in its annual Time 100 list as one of the "Most Influential People in the World".[26] In December 2012, Tendulkar announced his retirement from ODIs.[27] He retired from Twenty20 cricket in October 2013[28] and subsequently retired from all forms of cricket on 16 November 2013 after playing his 200th Test match, against the West Indies in Mumbai's Wankhede Stadium.[29] Tendulkar played 664 international cricket matches in total, scoring 34,357 runs.[5]
"""


#Syntax :- re.findall( 'what_to_find', 'Where_to_find')

print( re.findall( '\d+',  data ) )



# outcome = re.findall( '\d', data )
# print( f"outcome = { outcome }" )
# print()
# print()
# outcome = re.findall( '\d+', data )
# print( f"outcome = { outcome }" )