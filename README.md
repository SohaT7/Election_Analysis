# Election Analysis
## Table of Contents
- [Overview of the Analysis](#overview-of-the-analysis)
    - [Purpose](#purpose)
    - [About the Dataset](#about-the-dataset)
    - [Tools Used](#tools-used)
    - [Description](#description)
- [Results](#results)
    - [Comparing the Stock Performance between 2017 and 2018](#Comparing-the-Stock-Performance-between-2017-and-2018)
    - [Execution times of the Original script and the Refactored script](#Execution-times-of-the-Original-script-and-the-Refactored-script)
- [Summary](#summary)
- [Contact Information](#contact-information)


## Overview of the Analysis
### Purpose:
[This analysis](https://github.com/SohaT7/Election_Analysis/blob/main/PyPoll_Challenge.py) aims to conduct an election audit of a local congressional election, and report on the county and candidate with the highest number of votes. 

### About the Dataset:
The dataset is contained in the following CSV file, and has 369711 records containing the fields: Ballot ID, County, and Candidate.

[Election Results](https://github.com/SohaT7/Election_Analysis/blob/main/Resources/election_results.csv) 

### Tools Used:
 - Python
 - Visual Studio Code

### Description:
[This election audit](https://github.com/SohaT7/Election_Analysis/blob/main/PyPoll_Challenge.py) aims to compute:
        1. The total number of votes cast
        2. The voter turnout for each county
        3. The percentage of votes from each county out of the total count
        4. The county with the highest turnout
        5. A complete list of candidates who received votes
        6. The total number of votes each candidate received
        7. The percentage of votes each candidate won
        8. The winner of the election based on popular vote

## Results
![Election Audit Results](https://github.com/SohaT7/Election_Analysis/blob/main/Images/Image_election_audit_results%204.17.53%20PM.png)

The analysis of the election results shows that:

  . There were 369,711 votes cast in the congressional election.
  
  . The counties were:
  
      - Jefferson
      - Denver
      - Arapahoe
  
  . The county results were:
  
      - Jefferson received "10.5%" of the vote and "38,855" number of votes.
      - Denver received "82.8%" of the vote and "306,055" number of votes.
      - Arapahoe received "6.7%" of the vote and "24,801" number of votes.
  
  . The county with the largest number of votes was:
  
      - Denver, which received "82.8%" of the votes and "306,055" number of votes.
  
  . The candidates were:
  
      - Charles Casper Stockham
      - Diana DeGette
      - Raymon Anthony Doane
    
  . The candidate results were:
  
      - Charles Casper Stockham received "23.0%" of the vote and "85,213" number of votes.
      - Diana DeGette received "73.8%" of the vote and "272,892" number of votes.
      - Raymon Anthony Doane received "3.1%" of the vote and "11,606" number of votes.
    
  . The winner of the election was:
  
      - Diana DeGette, who received "73.8%" of the votes and "272,892" number of votes.

## Summary
This code script can be used by the election commission, with some modifications to suit specific election processes, for any election. The vote counts for not only counties, but cities and more importantly, states, can be generated too. If the candidates belong to various parties, all candidates belonging to each of those parties can be aggregated as well. The code can also be modified to calculate the total votes for all candidates belonging to a certain party in a certain state. Whichever way the code is modified, it will add to the nuances in the story these numbers can tell us.

## Contact Information
Email: st.sohatariq@gmail.com
