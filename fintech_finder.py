# Cryptocurrency Wallet

################################################################################

# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from datetime import datetime
from web3 import Web3, Account, EthereumTesterProvider
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
from crypto_wallet import generate_account, get_balance, send_transaction

################################################################################

# Fintech Finder Candidate Information

# Database of Fintech Finder candidates including their name, digital address, rating, hourly cost per Ether, known programming languages, areas of interest and favorite emoji.
# A single Ether is currently valued at $1,500
candidate_database = {
    "Lane": ["Lane", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", "4.3", .20, "Solidity, Ruby, Python, SQL", "Blockchain & Machine Learning Projects", "Images/lane.jpeg", "Emojis/glasses.png"],
    "Ash": ["Ash", "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396", "5.0", .33, "Ruby, Java, HTML, Solidity, Rust, Python", "Blockchain and Website Development", "Images/ash.jpeg", "Emojis/Laughing.png"],
    "Jo": ["Jo", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.7", .19, "Python, Perl, Solidity, CSS, SQL", "Always open to new projects - let's talk!", "Images/jo.jpeg", "Emojis/ThumbsUp.png"],
    "Kendall": ["Kendall", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.1", .16, "Go, Perl, Python, Solidity, SQL", "Short-term projects with a machine learning or blockchain focus", "Images/kendall.jpeg", "Emojis/Shades.png"]
}

# A list of the FinTech Finder candidates first names
people = ["Lane", "Ash", "Jo", "Kendall"]

def get_people():
    """Display the database of Fintech Finder's candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        st.image(db_list[number][6], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("FinTech Finder Rating: ", db_list[number][2])
        st.write("Hourly Rate per Ether: ", db_list[number][3], "eth")
        st.write("Programming Languages: ", db_list[number][4])
        st.write("Areas of Interest: ", db_list[number][5])
        st.write("Favorite Emoji: ")
        st.image(db_list[number][7], width=20)
        st.text(" \n")

################################################################################

# Streamlit Code

# Streamlit application headings
st.markdown("# Fintech Finder!")
st.markdown("## Hire A Fintech Professional!")
st.text(" \n")

################################################################################

# Streamlit Sidebar Code
# Add a header to the sidebar
st.sidebar.markdown("# Fintech Finder - Hire & Pay")
st.text(" \n")
st.text(" \n")
st.text(" \n")
st.text(" \n")

################################################################################

# Add a section for the client's account address and Ethereum balance

st.sidebar.markdown("## Your Account Address and Ethereum Balance in Ether")

#  Call the `generate_account` function and save it as the variable `account`
account = generate_account()

# Write the client's Ethereum account address to the sidebar
st.sidebar.text("\n")
st.sidebar.markdown("## Ethereum Account Address:")

# Write the Ethereum account address to the Streamlit page
st.sidebar.write(account.address)

# Call `get_balance` function and pass it your account address
# Write the returned ether balance to the sidebar
# Display the Etheremum Account balance
st.sidebar.markdown("## Ethereum Account Balance:")

# Call the get_balance function and write the account balance to the screen
ether_balance = get_balance(w3, account.address)
st.sidebar.write(ether_balance)

################################################################################

# Create a select box to choose a FinTech Hire candidate
st.sidebar.text("\n")
st.sidebar.text("\n")
st.sidebar.text("\n")
st.sidebar.markdown("## Pick a Candidate:")
person = st.sidebar.selectbox("Select a Person", people)

# Create an input field to record the number of hours the candidate worked
hours = st.sidebar.number_input("Select the Number of Hours")

# Create a summary of the candidate's name, hourly rate and Ethereum address
st.sidebar.text("\n")
st.sidebar.text("\n")
st.sidebar.text("\n")
st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")

# Identify the FinTech Hire candidate
candidate = candidate_database[person][0]

# Write the Fintech Finder candidate's name to the sidebar
st.sidebar.write(candidate)

# Identify the FinTech Finder candidate's hourly rate
hourly_rate = candidate_database[person][3]

# Write the FinTech Finder candidate's hourly rate to the sidebar
st.sidebar.write(hourly_rate)

# Identify the FinTech Finder candidate's Ethereum Address
candidate_address = candidate_database[person][1]

# Write the FinTech Finder candidate's Ethereum Address to the sidebar
st.sidebar.write(candidate_address)

# Write the Fintech Finder candidate's name to the sidebar
st.sidebar.text("\n")
st.sidebar.text("\n")
st.sidebar.text("\n")
st.sidebar.markdown("## Selected Candidate's Total Wage in Ether")

################################################################################s

# Sign and Execute a Payment Transaction

# Calculate candidate's wage
wage = candidate_database[person][3] * hours

# Write the candidate's wage to the sidebar
st.sidebar.write("If you hire", candidate, "for", hours, "hours, the total payment due will be", wage, "ether.")

################################################################################

# Save the transaction hash that the `send_transaction` function returns as a
# variable named `transaction_hash`, and have it display on the application’s
# web interface
st.sidebar.text("\n")
st.sidebar.text("\n")
if st.sidebar.button("Send Transaction"):

    # Call the `send_transaction` function and pass it 3 parameters:
    # Your `account`, the `candidate_address`, and the `wage` as parameters
    # Save the returned transaction hash as a variable named `transaction_hash`
    transaction_hash = send_transaction(w3, account, candidate_address, wage)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

# The function that starts the Streamlit application
# Writes FinTech Finder candidates to the Streamlit page
get_people()